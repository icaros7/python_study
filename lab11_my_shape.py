"""
과제 번호 : 19
작성자 : 이호민
작성일 : 2018.11.14
"""


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def __str__(self):
        return self

class Circle(Shape):
    PI = 3.1415

    def __init__(self, ra):
        Shape.__init__(self)
        self.ra = ra

    def area(self):
        return self.ra * self.PI

    def perimeter(self):
        return (self.ra * 2) * self.PI

    def getRadius(self):
        return self.ra

    def __str__(self):
        return "<원> 반지름 : " + str(self.ra)


class Rectangle(Shape):
    def __init__(self, n1, n2):
        Shape.__init__(self)
        self.Width = n1
        self.Height = n2

    def area(self):
        return self.Width * self.Height

    def perimeter(self):
        return (self.Height * 2) + (self.Width * 2)

    def getHeight(self):
        return self.Height

    def getWidth(self):
        return self.Width

    def getSides(self):
        tmp = []
        for i in len(self):
            tmp.append(self[i])
        return tmp

    def __str__(self):
        return "<직사각형> 밑변 : " + str(self.Width) + " 높이 : " + str(self.Height)


class Triangle(Shape):
    def __init__(self, n1, n2, n3, n4):
        Shape.__init__(self)
        self.Width = n1
        self.n2 = n2
        self.n3 = n3
        self.Height = n4

    def area(self):
        return self.Width * self.Height

    def perimeter(self):
        return (self.Height * 2) + (self.Width * 2)

    def getHeight(self):
        return self.Height

    def getWidth(self):
        return self.Width

    def getSides(self):
        l = []
        l.append(self)
        return l

    def __str__(self):
        return "<삼각형> 밑변 : " + str(self.Width) + " 높이 : " + str(self.Height)


s = Shape
c = Circle(5)
r = Rectangle(5, 10)
t = Triangle(3, 4, 5, 4)

print(c.area(), ", ", c.perimeter())
print(r.area(), ", ", r.perimeter())
print(t.area(), ", ", t.perimeter())
print(t.getSides())