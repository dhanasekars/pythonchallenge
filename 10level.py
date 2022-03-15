# http://www.pythonchallenge.com/pc/return/bull.html
# a = [1, 11, 21, 1211, 111221, 
# len(a[30]= ?)



a = '1'
b = ''
for i in range(0, 30):
    j = 0
    k = 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]: k += 1
        b += str(k-j) + a[j]
        j = k
    print(b)
    a = b
    b = ''
print(len(a))