from pprint import pprint

from scraper import Scraper 

scraper = Scraper('https://scrapethissite.com/pages/forms/?q=Bruins')

results = scraper.get_table_contents()

pprint(results)
