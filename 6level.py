# welcome to my zipped list.

# hint1: start from 90052
# hint2: answer is inside the zip

# http://www.pythonchallenge.com/pc/def/channel.zip

import re,zipfile
comments = []

def nothing(new = "90052"):

    new_filename = 'channel/' + new + '.txt'
    f = open(new_filename, 'r')
    content = f.read()
    archive = zipfile.ZipFile('channel.zip')
    comments.append(archive.getinfo(new + '.txt').comment.decode('utf-8'))
    try:
        new = re.search("Next nothing is (\d+)", content).group(1)
    except AttributeError:
        f.close()
        exit(print("".join(comments)))
    f.close()
    return nothing(new)


nothing()
    

new = ['*', '\n', '*', '*', '\n','*','*','*','\n' ]
print("".join(new))