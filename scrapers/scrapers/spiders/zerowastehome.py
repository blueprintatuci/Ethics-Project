import scrapy
# import json
# import requests 

# API_ENDPOINT = 'http://ethic-blueprint.herokuapp.com/add_article'

# header = {
#     'Content-type' : 'application/json'
# }

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
                'publish_date' : date_convert(art.css("div.text span::text").get()),
            }

            # data = json.dumps({
            #     'url' : art.css("a.entire-meta-link::attr(href)").get(),
            #     'title' : art.css("div.post-header a::text").get().strip(),
            #     'author' : art.css("div.text a::text").get(),
            #     'image_url' : art.css('div.post-featured-img-wrap span.post-featured-img::attr(style)').re(r'http.*jpg')[0],
            #     'content' : art.css("div.excerpt::text").get(),
            #     'publish_date' : date_convert(art.css("div.text span::text").get()),
            # })

            # r = requests.post(url = API_ENDPOINT, headers = header, data = data) 
   
            # pastebin_url = r.text 
            # print("The pastebin URL is:%s"%pastebin_url)
