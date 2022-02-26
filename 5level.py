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

# atomic_content = [[(2, 4)], [(1, 14), (10, 5), (3, 70), (5, 5), (101, 1)]]

# for i in atomic_content:
#     for j,k in i:
#         print(j * k)


# for i in atomic_content:
#     print("".join(str(j * k) for j,k in i))


