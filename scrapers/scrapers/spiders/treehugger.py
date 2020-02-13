import scrapy


class TreehuggereSpider(scrapy.Spider):
    name = "treehugger"

    def start_requests(self):
        urls = [
            'https://www.treehugger.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for art in response.css("article"): 
            yield {
                'url' : 'https://www.treehugger.com' + art.css('div.c-article__image a::attr(href)').get(),
                'title' : art.css('div.c-article__summary a::text').get().strip(),
                'author' : art.css('div.c-article__summary div.c-article__byline a::text').get(),
                'image_url' : art.css('div.c-article__image img::attr(src)').get(),
                'content' : art.css('div.c-article__summary div.c-article__excerpt::text').get(),
                'publish_date' : art.css('div.c-article__byline span a::text')[-1].get(),
            }
