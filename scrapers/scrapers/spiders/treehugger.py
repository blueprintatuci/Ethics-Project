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
                'publish_date' : date_convert(art.css('div.c-article__byline span a::text')[-1].get()),
            }
            # data = json.dumps({
            #     'url' : 'https://www.treehugger.com' + art.css('div.c-article__image a::attr(href)').get(),
            #     'title' : art.css('div.c-article__summary a::text').get().strip(),
            #     'author' : art.css('div.c-article__summary div.c-article__byline a::text').get(),
            #     'image_url' : art.css('div.c-article__image img::attr(src)').get(),
            #     'content' : art.css('div.c-article__summary div.c-article__excerpt::text').get(),
            #     'publish_date' : date_convert(art.css('div.c-article__byline span a::text')[-1].get()),
            # })
            # r = requests.post(url = API_ENDPOINT, headers = header, data = data) 
   
            # pastebin_url = r.text 
            # print("The pastebin URL is:%s"%pastebin_url)
