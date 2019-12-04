import scrapy
from scrapy import Request
import re
from scrapy.loader import ItemLoader

#pierwszy wynik przejscia po 100 stronach  koniec: 16:02:35 poczatek: 16:01:47 przejscie    50 stron bez zadnych warunkow przy szukaniu, ilość pobranych recordów - w chuj
#to_do: dodaj z pliku starego webscrapera multitasking i loggin
#zmiana na spiderCrawl===> czy ja nie robie na okolo tego

 # 'price': article.css("div._906bb92 span::text").get(),
                # 'decimal' : article.css("div._906bb92 span:nth-child(2)::text").get(),
				# 'url_to_img': article.css("img::attr(data-src)").get(),
				# 'article_url': article.css('h2 a::attr(href)').get()
# jeden=response.css('div._9a071_1LGgN')
# dwa=jeden.css('div::text').getall()
# trzy=dwa[2]                                           #OPINIA ale po wejsciu na ULR produktu
# produkty ze strony glownej
# pobierz adres url zdjecia


#global haslo
#haslo = input("Enter a name of the article:")
# print((title))
# key = re.compile(haslo)
# if key.search(title):
#     print("TITLLE!!!  {} is matching to key {} ".format(title, key))


class Product(scrapy.Item):
    title = scrapy.Field()


class ElectronicsSpider(scrapy.Spider):
    name = 'allegro_spider'
    allowed_domains = ["www.allegro.com.pl"]


    def start_requests(self): # jest uniwersalny dla kazdej podstrony dla kategorii Elektronika
        #tutaj trzeba doprecyowac przez ktore podkategorie ma przejsc pajak
        #multitasking przy zapytaniu o kilka produktow

        urls=['https://allegro.pl/kategoria/konsole-i-automaty?bmatch=baseline-cl-dict42-ele-1-1-1024']    #telefony i akcesoria

        for url in urls:
            yield Request(url,callback=self.parse)   

    def parse(self,response):

        for item in self.scrape(response):  #iterator
              yield item

        paths = response.css('section._5a7713f')
        articles = paths.css('article')
        for article in articles:
            next = article.css('h2 a::attr(href)').get()
            print("Found url: {}".format(next))
            yield Request(response.urljoin(next), callback=self.parse, dont_filter=True)

    def scrape(self,response):   # trzeba przekazac do itemu
        item = Product()
        jeden = response.css('div._9a071_1LGgN')
        title=jeden.css('h1::text').get()
        item['title']=title
        yield item


















