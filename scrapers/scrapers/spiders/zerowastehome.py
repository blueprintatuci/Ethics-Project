import scrapy


class ZeroWasteHomeSpider(scrapy.Spider):
    name = "zerowastehome"

    def start_requests(self):
        urls = [
            'https://zerowastehome.com/blog/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for art in response.css("div.post-content"):
            yield {
                'link' : art.css("a.entire-meta-link::attr(href)").get(),
                'title' : art.css("div.post-header a::text").get(),
                'author' : art.css("div.text a::text").get(),
                'date' : art.css("div.text span::text").get(),
            }
