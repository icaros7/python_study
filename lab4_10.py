"""
str = input()
for i in range(0,len(str)):
    for x in range(0, i):
        print(" ", end="")
    for y in range(len(str)-i, 0, -1):
        print(str[i], end="")
    print("")
"""

str = input()
l = len(str)

for i in range(0,l):
    o = ""
    for x in range(0,i):
        o=o+" "
    for x in range(i,l):
        o=o+str[x]
    print(o)