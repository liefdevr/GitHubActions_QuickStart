from bs4 import BeautifulSoup
from urllib import request

response = request.urlopen('https://www.jleague.jp/standings/j1/')
soup = BeautifulSoup(response)
response.close()

header = soup.find('tr')
print(header)
