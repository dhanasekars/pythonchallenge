import requests,json,re

link = "http://www.pythonchallenge.com/pc/def/equality.html"
r = requests.get(link).text
text = r.split("--") 
f = open("4level.txt", "w")
f.write(text[1])
f.close()

with open('4level.txt', 'r') as f:
    lines = f.read().strip()

x = "".join(re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",lines))
print(x)
