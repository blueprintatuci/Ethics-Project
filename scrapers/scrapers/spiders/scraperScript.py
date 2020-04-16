import requests
import json
from treehugger import *
from zerowastehome import *
from twisted.internet import reactor,defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# RUN SCRAPERS
print ("\n------ Starting scrapers ------ \n")
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(TreehuggerSpider)
    yield runner.crawl(ZeroWasteHomeSpider)
    # add new spiders  here
    reactor.stop()

crawl()
reactor.run() 

print ("\n------ Scrapers completed ------ \n")
# DEFINE ENDPOINT PARAMETERS
API_ENDPOINT = 'http://ethic-blueprint.herokuapp.com/add_article'
header = {
    'Content-type' : 'application/json'
}

# SEND SCRAPER TO BACKEND
treehugger = open("treehugger.json", 'r')
zerowastehome = open("zerowastehome.json", 'r')
## add new jsons from new scrapers here

print ("\n------ Sending to backend ------ \n")
for article in treehugger.readlines():
    r = requests.post(url = API_ENDPOINT, headers = header, data = article) 
    
    pastebin_url = r.text 
    print("The pastebin URL is:%s"%pastebin_url) 

for article in zerowastehome.readlines():
    r = requests.post(url = API_ENDPOINT, headers = header, data = article) 
    
    pastebin_url = r.text 
    print("The pastebin URL is:%s"%pastebin_url) 

## add new loops here to send to endpoint
print ("------ Script finished ------ ")
