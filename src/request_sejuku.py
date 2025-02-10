from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.atmarkit.co.jp/ait/subtop/di/'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
response.close()

topstories = soup.find('div', class_='colBoxTopstories')
colboxindexes = topstories.find_all('div', class_='colBoxIndex')

top_articles = []
for item in colboxindexes:
    title = item.select('div.colBoxTitle')[0].text
    description = item.select('div.colBoxDescription')[0].text
    top_articles.append(f'{title}: {description}')

for articles in top_articles:
    print(articles)
