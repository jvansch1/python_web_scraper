from pprint import pprint

from scraper import Scraper

# from bs4 import BeautifulSoup
# import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}    
# page = requests.get('https://hackofalltrades.dev', headers=headers)

# soup = BeautifulSoup(page.content, 'html.parser')

# articles = soup.find_all('article')

# for article in articles:
#     article_children = article.children

#     for child in article_children:
#         print(child)    

base_url = 'http://olympus.realpython.org'

scraper = Scraper('https://scrapethissite.com/pages/simple/')

results = scraper.find_tags_by_name('h3')

print(results)

# for result in results:
#     print(result.contents)
