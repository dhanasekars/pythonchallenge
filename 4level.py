from urllib.request import urlopen
import requests,re

def nothing(fivedigit = 12345,i = 0):
    
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(fivedigit)
    content = requests.get(url).text
    try:
        r = re.search("and the next nothing is (\d+)", content).group(1)
    except AttributeError:
        exit(content)
    print(f"{content} <> {r}")
    return(nothing(r,i))

nothing()

