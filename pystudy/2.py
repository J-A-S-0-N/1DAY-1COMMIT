import scrapy

class PostSpider(scrapy.Spider):
    name = "posts"

start_url = {
    'https://www.amazon.com/Microsoft-Surface-Laptop-Touch-Screen-Alcantara/dp/B084SR345X/ref=sr_1_1?crid=36USKEXD37TEB&dchild=1&keywords=surface+laptop+3&qid=1586306606&sprefix=surface+laptop%2Caps%2C412&sr=8-1'
    'https://www.amazon.com/Apple-MacBook-Retina-2-4GHz-Quad-core/dp/B07SKPVDFQ/ref=sr_1_6?crid=3RWZND2S5LB0M&dchild=1&keywords=macbook+air&qid=1586306556&sprefix=macboo%2Caps%2C395&sr=8-6'
}

def parse(self, response):
    page = response.url.slit(' / ')[-1]
    film = 'posts-%s.html' % page
    with open(film,'wb') as f:
        f.write(response.body)
