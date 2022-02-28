
# Learning
#   1. List comprehension 
#   2. Image package - pillow and how to process images
#   3. map function

# http://www.pythonchallenge.com/pc/def/oxygen.png
# width 629, height 95 (W,H)

from PIL import Image
import re

with Image.open('oxygen.png') as im:
    print((im.format, im.size, im.mode ))
    px = im.load()
    # for x in range(0,im.width,7):
    #     row = px[x, im.height / 2]
    #     if row[0] == row[1] == row[2]:
    #         print(''.join(chr(row[0])))

    row = [px[x, im.height / 2] for x in range(im.width)]
    row = row[::7]
    ords = [r for r,b,g,a in row if r == g == b]
    notdoneyet = "".join(map(chr,ords))
    print(notdoneyet)
    level8 = re.findall(("\d+"),notdoneyet)
    for i in level8:
        print("".join(chr(int(i))))
