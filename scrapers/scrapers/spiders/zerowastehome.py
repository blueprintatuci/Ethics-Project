import scrapy
import json

months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December' :12
}

def date_convert(string):
    date = string.split()
    mon = months[date[0]]
    day = date[1].strip(',')
    year = date[2]
    return "{}/{}/{}".format(mon, day, year)

class ZeroWasteHomeSpider(scrapy.Spider):
    name = "zerowastehome"
    fileName = name + ".json"

    def start_requests(self):
        output = open(fileName, 'w')
        output.close()
        urls = [
            'https://zerowastehome.com/blog/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for art in response.css("div.post-content"): 
            output = open(fileName, 'a')
            data = json.dumps({
                'url' : art.css("a.entire-meta-link::attr(href)").get(),
                'title' : art.css("div.post-header a::text").get().strip(),
                'author' : art.css("div.text a::text").get(),
                'image_url' : art.css('div.post-featured-img-wrap span.post-featured-img::attr(style)').re(r'http.*jpg')[0],
                'publish_date' : date_convert(art.css("div.text span::text").get())
                'source': name,
            })
            output.write(data + '\n')
            output.close()
