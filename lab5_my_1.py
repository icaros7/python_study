def what_the(*a):
    va = 0
    for i in a:
        va += i
    return va


print(what_the(1, 2, 3))
