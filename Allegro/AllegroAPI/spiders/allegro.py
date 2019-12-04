import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader

# zeby zabrac link do produktu path.css('h2 a').attrib['href']
# response.css('div._e219d_jjqRf a::attr(href)').get()
# paths=response.css('div.opbox-listing-layout')  # caly layout

#pierwszy wynik przejscia po 100 stronach  koniec: 16:02:35 poczatek: 16:01:47 przejscie    50 stron bez zadnych warunkow przy szukaniu, ilość pobranych recordów - w chuj


class ElectronicsSpider(scrapy.Spider):
    name = 'allegro_spider'
    allowed_domains = ["www.allegro.com.pl", "www.allegro.pl"]
    def start_requests(self): # jest uniwersalny dla kazdej podstrony dla kategorii Elektronika
        #tutaj trzeba doprecyowac przez ktore podkategorie ma przejsc pajak
        #multitasking przy zapytaniu o kilka produktow

        urls=['https://allegro.pl/kategoria/konsole-i-automaty?bmatch=baseline-cl-dict42-ele-1-1-1024']    #telefony i akcesoria

        for url in urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        loader = ItemLoader()
        for item in self.scrape(response):  #iterator
              yield item

        next = response.css('a[rel="next"]::attr(href)').get()  # link na nastepna strone
        print("Found url: {}".format(next))
        yield Request(response.urljoin(next), callback=self.parse, dont_filter=True)     #POST requests byly przekierowywane, dont filter ratuje sutyacje

    def scrape(self, response):   # trzeba przekazac do itemu

        #brakuje automatycznego wchodzenia w link artykulu i pobiwrania oceny
        paths = response.css('section._5a7713f')
        articles = paths.css('article')
        for article in articles:
            article_url = article.css('h2 a::attr(href)').get()              #link do artykulu
            jeden=response.css('div._9a071_1LGgN')
            dwa=jeden.css('div::text').getall()
            trzy=dwa[2]                                           #OPINIA ale po wejsciu na ULR produktu

            yield {  #produkty ze strony glownej
                'title': article.css('h2 a::text').get(),
                'price': article.css("div._906bb92 span::text").get(),
                'decimal' : article.css("div._906bb92 span:nth-child(2)::text").get()
            }
