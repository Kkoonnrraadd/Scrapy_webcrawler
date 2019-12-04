import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader

#pierwszy wynik przejscia po 100 stronach  koniec: 16:02:35 poczatek: 16:01:47 przejscie    50 stron bez zadnych warunkow przy szukaniu, ilość pobranych recordów - w chuj
#to_do: dodaj z pliku starego webscrapera multitasking i loggin
#zmiana na spiderCrawl
class Product(scrapy.Item):
    title = scrapy.Field()

class ElectronicsSpider(scrapy.Spider):
    name = 'string_spider'
    allowed_domains = ["www.allegro.com.pl"]
	#tutaj user bedzie podawal input 
    def start_requests(self):
	#tutaj usera input bedzie przez format() laczony z adresem url 
		#stringg="lala" potem format()stringg input fro user
        urls=['https://allegro.pl/listing?string=lala&bmatch=baseline-dict43-fas-1-1-1127']    
        for url in urls:
            yield Request(url,callback=self.parse)

    def parse(self,response):
        for item in self.scrape(response):  #iterator
              yield item

        nexts = response.css('h2.ebc9be2 a::attr(href)').getall()# linki produktow
        for next in nexts:
            print("Found url: {}".format(next))
            yield Request(response.urljoin(next), callback=self.parse, dont_filter=True)    

    def scrape(self, response):  # trzeba przekazac do itemu
        #ocena= response.xpath("/html/body/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[4]")
        #cena=response.xpath("/html/body/div[2]/div[4]/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[5]/div/div[1]").get()
        #cena dostawy=
        item = Product()
		#do zmiany na xpath 
		#3333333333poprzedni 
        jeden = response.css('div._9a071_1LGgN')
        title = jeden.css('h1::text').get()
        item['title'] = title
        yield item