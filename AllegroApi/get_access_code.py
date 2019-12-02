from requests_oauthlib import OAuth1Session as oauth
import allegro_api


import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser
from AllegroApi import config

# Dla ułatwienia, definiujemy domyślne wartości (tak zwane stałe), są one uniwersalne
DEFAULT_OAUTH_URL = 'https://allegro.pl/auth/oauth'
DEFAULT_REDIRECT_URI = 'http://localhost:8000'
client_id = config.client_id
api_key = config.api_key



# Implementujemy funkcję, której parametry przyjmują kolejno:
#  - client_id (ClientID), api_key (API Key) oraz opcjonalnie redirect_uri i oauth_url
# (jeżeli ich nie podamy, zostaną użyte domyślne zdefiniowane wyżej)
def get_access_code(client_id=client_id, api_key=api_key, redirect_uri=DEFAULT_REDIRECT_URI, oauth_url=DEFAULT_OAUTH_URL):
    # zmienna auth_url zawierać będzie zbudowany na podstawie podanych parametrów URL do zdobycia kodu
    auth_url = '{}/authorize' \
               '?response_type=code' \
               '&client_id={}' \
               '&api-key={}' \
               '&redirect_uri={}'.format(oauth_url, client_id, api_key, redirect_uri)

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

    # Wyświetli nam adres uruchomionego lokalnego serwera
    print('server_address:', server_address)

    # Uruchamiamy przeglądarkę, przechodząc na adres zdefiniowany do uzyskania kodu dostępu
    # wyświetlić się powinien formularz logowania do serwisu Allegro.pl
    webbrowser.open(auth_url)

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

get_access_code()
