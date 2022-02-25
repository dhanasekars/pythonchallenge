from urllib.request import urlopen
import requests,re

def nothing(fivedigit = 8022,i = 0):
    
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(fivedigit)
    r1 = requests.get(url).text
    try:
        r = re.search("and the next nothing is (\d+)", r1).group(1)
    except AttributeError:
        exit(r1)
    print(f"{r1} <> {r}")
    return(nothing(r,i))

nothing()

