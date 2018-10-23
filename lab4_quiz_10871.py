l = []
n, x = input().split()
l = input().split()
n = int(n)
x = int(x)
l = [int (i) for i in l]

for i in range(0, n):
    if l[i] < x:
        print(l[i], end=" ")
