from bs4 import BeautifulSoup
from urllib import request

response = request.urlopen('https://www.jleague.jp/standings/j1/')
soup = BeautifulSoup(response, 'html.parser')
response.close()

table = soup.find_all('tr')

standing = []
for row in table:
    tmp = []
    for item in row.find_all('td'):
        if item.a:
            tmp.append(item.text[0:len(item.text) // 2])
        else:
            tmp.append(item.text)
    del tmp[0]
    del tmp[-1]
    standing.append(tmp)

for item in standing:
    print(item)
