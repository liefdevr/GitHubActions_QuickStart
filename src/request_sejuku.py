from bs4 import BeautifulSoup
from urllib import request

url = 'https://www.atmarkit.co.jp/ait/subtop/di/'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

topstories = soup.find('div', class_='colBoxTopstories')
print(topstories)
