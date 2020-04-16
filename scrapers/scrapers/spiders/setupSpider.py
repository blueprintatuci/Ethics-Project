import scrapy


class SetupSpider(scrapy.Spider):
    name = "setup"

    def start_requests(self):
        urls = [
            'https://www.treehugger.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'example-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
       