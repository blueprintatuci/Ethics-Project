import scrapy


class ZeroWasteHomeSpider(scrapy.Spider):
    name = "zerowastehome"

    def start_requests(self):
        urls = [
            'https://zerowastehome.com/blog/',
            'https://zerowastehome.com/blog/page/2/',
            'https://zerowastehome.com/blog/page/3/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for art in response.css("div.post-content"): 
            yield {
                'url' : art.css("a.entire-meta-link::attr(href)").get(),
                'title' : art.css("div.post-header a::text").get().strip(),
                'author' : art.css("div.text a::text").get(),
                'image_url' : art.css('div.post-featured-img-wrap span.post-featured-img::attr(style)').re(r'http.*jpg')[0],
                'content' : art.css("div.excerpt::text").get(),
                'publish_date' : art.css("div.text span::text").get(),
            }
