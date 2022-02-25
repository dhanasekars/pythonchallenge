f = open("level3.txt", "r")
txt = f.read()
newtxt = ""
for i in txt:
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        newtxt += i
print(newtxt)

