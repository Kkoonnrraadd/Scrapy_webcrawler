from requests_oauthlib import OAuth1Session as oauth

import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
import json
# Dla ułatwienia, definiujemy domyślne wartości (tak zwane stałe), są one uniwersalne
DEFAULT_OAUTH_URI = 'https://allegro.pl/auth/oauth'
DEFAULT_REDIRECT_URI = 'http://localhost:8000'
client_id = "xxx"
client_secret = "xxx"
api_key = "xxx:xxx"


# Implementujemy funkcję, której parametry przyjmują kolejno:
#  - client_id (ClientID), api_key (API Key) oraz opcjonalnie redirect_uri i oauth_uri
# (jeżeli ich nie podamy, zostaną użyte domyślne zdefiniowane wyżej)


def get_access_code(client_id=client_id, api_key=api_key, redirect_uri=DEFAULT_REDIRECT_URI,
                    oauth_uri=DEFAULT_OAUTH_URI):
    # zmienna auth_uri zawierać będzie zbudowany na podstawie podanych parametrów URL do zdobycia kodu
    auth_uri = '{}/authorize' \
               '?response_type=code' \
               '&client_id={}' \
               '&api-key={}' \
               '&redirect_uri={}'.format(oauth_uri, client_id, api_key, redirect_uri)

    # uzywamy narzędzia z modułu requests - urlparse - służy do spardowania podanego url
    # (oddzieli hostname od portu)
    parsed_redirect_uri = requests.utils.urlparse(redirect_uri)

    # definiujemy nasz serwer - który obsłuży odpowiedź allegro (redirect_uri)
    server_address = parsed_redirect_uri.hostname, parsed_redirect_uri.port

    # Ta klasa pomoże obsłużyć zdarzenie GET na naszym lokalnym serwerze
    # - odbierze żądanie (odpowiedź) z serwisu allegro
    class AllegroAuthHandler(BaseHTTPRequestHandler):
        def __init__(self, request, address, server):
            super().__init__(request, address, server)

        def do_GET(self):
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            self.server.path = self.path
            self.server.access_code = self.path.rsplit('?code=', 1)[-1]

        def do_POST(self):
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.server.path = self.path
            self.server.access_code = self.path.rsplit('?code=', 1)[-1]

    # Wyświetli nam adres uruchomionego lokalnego serwera
    print('server_address:', server_address)

    # Uruchamiamy przeglądarkę, przechodząc na adres zdefiniowany do uzyskania kodu dostępu
    # wyświetlić się powinien formularz logowania do serwisu Allegro.pl
    webbrowser.open(auth_uri)

    # Uruchamiamy nasz lokalny web server na maszynie na której uruchomiony zostanie skrypt
    # taki serwer dostępny będzie pod adresem http://localhost:8000 (server_address)
    httpd = HTTPServer(server_address, AllegroAuthHandler)
    print('Waiting for response with access_code from Allegro.pl (user authorization in progress)...')

    # Oczekujemy tylko jednego żądania
    httpd.handle_request()

    # Po jego otrzymaniu zamykamy nasz serwer (nie obsługujemy już żadnych żądań)
    httpd.server_close()

    # Klasa HTTPServer przechowuje teraz nasz access_code - wyciągamy go
    _access_code = httpd.access_code
    # Dla jasności co się dzieje - wyświetlamy go na ekranie
    print('Got an authorize code: ', _access_code)

    # i zwracamy jako rezultat działania naszej funkcji
    return _access_code


def sign_in(client_id=client_id, client_secret=client_secret, api_key=api_key, redirect_uri=DEFAULT_REDIRECT_URI, oauth_url=DEFAULT_OAUTH_URI):
    access_code = get_access_code()
    token_url = oauth_url + '/token'

    access_token_data = {'grant_type': 'authorization_code',
                         'code': access_code,
                         'api-key': api_key,
                         'redirect_uri': redirect_uri}

    response = requests.post(url=token_url,
                             auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
                             data=access_token_data)
    print(response.json())
    return response.json()

def do_smt(
        access_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzU0MTU1NjMsInVzZXJfbmFtZSI6IjYwNDU5MTQ5IiwianRpIjoiNjQwYjRjNDgtOWEzMi00NjA4LWJlYzEtNTNhZjA5MjI4Y2M3IiwiY2xpZW50X2lkIjoiYmM0OTViY2I5NjY4NDFlNTk1NzQ1YmU2ZGQ0YmZkZjkiLCJzY29wZSI6WyJhbGxlZ3JvX2FwaSJdfQ.dGkQEp5VyYb7tuhiR3gIBJMmuHX-y1rHDzcc4i6XA0z-Z8mvsgzOyFZPuwVC35WE2a0D_5Ajx5q_d5IWAHt46eAC4KZuFRNEJUFwwLX3H7svIuix-qCRsmSiPzBb0qFVKYYCfyz18khmZWE4HhHwKVzltl8uDmrqtY4RdCXMxoiHeHQCzjQr_s3m8Xqdr2etu5RPsaxXxcY8dLpXtx-G35au0D5sOUPpnrj6thpcjqf8NUeWT_pzaOJvndHgan2H1D878deGtyNyqTC-r_-ry8okl3h-Os1RufldyrM84aPyM7uYdlUr-m8VK7dNA5cJMxFylDLH7EJOONzSXd5UFw'):
    headers = {}
    headers['charset'] = 'utf-8'
    headers['Accept-Language'] = 'pl-PL'
    headers['Content-Type'] = 'application/json'
    headers['Api-Key'] = api_key
    headers['Accept'] = 'application/vnd.allegro.public.v1+json'
    headers['Authorization'] = "Bearer {}".format(access_token)

    # Inicjujemy naszą sesję (przechowuje nagłówki itd.)
    # konstrukcja with pozwala na użycie sesji tylko w jej obrębie
    # kiedy wyczerpią się instrukcje wewnątrz niej
    # straci ona ważność (zostanie zamknięta)
    with requests.Session() as session:

        session.headers.update(headers)
        DEFAULT_API_URL='https://api.allegro.pl'
# randomowy jakis url z przykladu
        response = session.get(DEFAULT_API_URL + '/after-sales-service-conditions/warranties',
                               params={'sellerId': '60459149'})
#params i headers
        #print(response.headers)
        print(response.url)
        print(response.status_code)
        # Wypisz odpowiedź w formacie JSON
        print(response.json())


#get_access_code()
#sign_in()
#refresh_token()