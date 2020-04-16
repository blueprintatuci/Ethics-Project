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

class TemplateSpider(scrapy.Spider):    #change 'Template' to match website name
    name = "template"   #change name
    fileName = name + ".json"

    def start_requests(self):
        output = open(self.fileName, 'w')
        output.close()
        urls = [    #change url
            'https://www.example.com/',   
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for art in response.css("article"): 
            output = open(self.fileName, 'a')
            data = json.dumps({
                'url' : "urlQuery",
                'title' : "titleQuery",
                'author' : "authorQuery",
                'image_url' : "image_urlQuery",
                'publish_date' : "publish_dateQuery",
                'source': self.name,
            })
            output.write(data + '\n')
            output.close()
