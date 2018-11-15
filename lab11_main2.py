# 파이썬 파이레엇 필요한 플래스만 수입
from lab11_my_shape import Shape, Circle, Rectangle, Triangle

s = Shape()

c = Circle(5)
r = Rectangle(5, 10)
t = Triangle(3, 4, 4, 5)

print(c.area())
print(c.perimeter())
print(r.area())
print(r.perimeter())
print(t.area())
print(t.perimeter())
print(r.getSides())

l = []
l.append(s)
l.append(c)
l.append(r)
l.append(t)
for e in l:
    print(e)