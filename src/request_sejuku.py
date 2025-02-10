from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.atmarkit.co.jp/ait/subtop/di/'
response = request.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
response.close()

topstories = soup.find('div', class_='colBoxTopstories')
colboxindexes = topstories.find_all('div', class_='colBoxIndex')
print(colboxindexes[0])
