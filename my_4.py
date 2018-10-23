x = input("몇단까지? : ")
x = int(x)
y = input("몇까지? : ")
y = int(y) + 1

for i in range(2,x):
    for ii in range(1,y):
        print("%d * %d = %d" %(i, ii, x*ii))
    if i == x: break