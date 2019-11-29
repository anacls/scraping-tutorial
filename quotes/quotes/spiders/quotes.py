import scrapy 
from scrapy import Request, Spider 

class Quotes(Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        print(quotes)

        for quote in quotes:
            quote_text = quote.xpath('./span[@class="text"]/text()').extract_first()
            print(quote_text)
            quote_author = quote.xpath('./span//small/text()').extract_first()
            print(quote_author)
            quote_author_about_link = quote.xpath('./span/a/@href').extract_first()
            print(quote_author_about_link)

            yield Request(
                url=response.urljoin(quote_author_about_link),
                callback=self.parse_biografia
            )
        
        next_page = response.xpath('//ul[@class="pager"]//li[@class="next"]//a/@href').extract_first()
        
        while(next_page):
            yield Request(
                url=response.urljoin(next_page),
                callback=self.parse
            )
            break

    def parse_biografia(self, response):
        author_details = response.xpath('//div[@class="author-details"]')
        author_name = author_details.xpath('./h3/text()').extract_first()
        author_born_date = author_details.xpath('./p//span[@class="author-born-date"]/text()').extract_first()
        author_born_location = author_details.xpath('./p//span[@class="author-born-location"]/text()').extract_first()

        yield{
            'nome': author_name,
            'data de nascimento': author_born_date,
            'local onde nasceu': author_born_location,
            'url da biografia': response.url 
        }
