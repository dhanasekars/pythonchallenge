#  url http://www.pythonchallenge.com/pc/def/peak.html 

from urllib.request import urlopen
import requests,pickle

url =  "http://www.pythonchallenge.com/pc/def/banner.p"
print(urlopen(url).read().decode())
content = pickle.load(urlopen(url))
print(content)

for i in content:
    content = "".join(j * k for j,k in i)
    print(content)