from base_spider import BaseSpider

## We need to wait for ajax requests here

class MovieSpider(BaseSpider):
    name = 'movies'
    start_urls = [
        'https://scrapethissite.com/pages/ajax-javascript/#2015'
    ]

    def parse(self, response):
        for movie in response.css('tr.film'):
            yield {
                'title': movie.css('td.film_title::text')
            }
