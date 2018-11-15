# 파이썬 파일에서 전체 수입
import lab11_my_shape

s = lab11_my_shape.Shape()

c = lab11_my_shape.Circle(5)
r = lab11_my_shape.Rectangle(5, 10)
t = lab11_my_shape.Triangle(3, 4, 4, 5)

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