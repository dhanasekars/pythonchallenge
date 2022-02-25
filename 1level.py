# This is level two with a text to decipher and a hint. 
# The hint and the cypher looks shift two ASCII value.

import string
from cs50 import get_string

#string = get_string("input string: ")
txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

new_string = ""
# for i in txt:
#     if i.isalpha() == True:
#         i = (ord(i)+2)  
#         if i > 122:
#             i = i - 26
#             new_string += chr(i) 
#         else:
#             new_string += chr(i)
#     else:
#         new_string += i

# print(new_string)



# Better options 

for i in txt:
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        new_string += chr((ord(i) + 2 - ord('a')) % 26 + ord('a'))
    else:
        new_string += i
print(new_string)
