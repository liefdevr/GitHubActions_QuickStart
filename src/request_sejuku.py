import requests
 
url = "http://abehiroshi.la.coocan.jp/"
 
response = requests.get(url)
response.encoding = response.apparent_encoding
 
print(response.text)
