"""
과제 번호 : 19
작성자 : 이호민
작성일 : 2018.11.14
"""

import sys


class Shape:  # Shape 클래스를 정의한다. 메쏘드로 area(), perimeter()를 가지고 있다.
    def area(self):
        """
        area()는 면적, perimeter()는 둘레를 반환한다.
        :return: Shape 클래스는 0을 반환한다.
        """
        return 0

    def perimeter(self):
        """
        area()는 면적, perimeter()는 둘레를 반환한다.
        :return: Shape 클래스는 0을 반환한다.
        """
        return 0

    def __str__(self):
        """
        __str__()을 정의한다.
        :return: “도형”을 반환
        """
        return "도형"


class Circle(Shape):
    PI = 3.1415  # 클래스변수 PI=3.1415로 정의한다.

    def __init__(self, ra):
        """
        Circle 함수 초기화 선언
        :param ra: 반지름 값 매개변수로 받아 저장
        """
        Shape.__init__(self)
        self.ra = ra

    def area(self):
        """
        원의 넓이를 반환함
        :return: πr^2 을 반환함
        """
        return self.ra * self.ra * self.PI

    def perimeter(self):
        """
        원의 둘래를 반환함
        :return: 2πr 을 반환함
        """
        return (self.ra * 2) * self.PI

    def getRadius(self):
        """
        원의 반지름을 반환함
        :return: ra를 반환
        """
        return self.ra

    def __str__(self):
        """
        원 형태를 string 형태로 반환
        :return:
        """
        return "<원> 반지름 : " + str(self.ra)


class Rectangle(Shape):
    def __init__(self, n1, n2):
        Shape.__init__(self)
        self.Width = n1
        self.Height = n2

    def area(self):
        """
        직사각형의 넓이를 반환함
        :return: 가로*세로 를 반환함
        """
        return self.Width * self.Height

    def perimeter(self):
        """
        직사각형의 둘래를 반환
        :return: 2(가로+세로)를 반환
        """
        return (self.Height + self.Width) * 2

    def getHeight(self):
        """
        직사각형의 세로 길이를 반환
        :return: Height
        """
        return self.Height

    def getWidth(self):
        """
        직사각형의 가로 길이를 반환
        :return: Width
        """
        return self.Width

    def getSides(self):
        """
        Triangle, Rectangle 클래스에는 변의 길이를 시계방향으로 list 형태로 반환하는 getSides() 메쏘드를 정의
        :return: list
        """
        tmp = [self.Width, self.Height, self.Width, self.Height]
        return tmp

    def __str__(self):
        """
        직사각형 형태를 string 형태로 반환
        :return:
        """
        return "<직사각형> 밑변 : " + str(self.Width) + " 높이 : " + str(self.Height)


class Triangle(Shape):
    def __init__(self, n1, n2, n3, n4):
        Shape.__init__(self)
        self.Width = n1
        self.n2 = n2
        self.n3 = n3
        self.Height = n4

    def area(self):
        """
        삼각형의 넓이를 반환
        :return: (Width * Height) / 2
        """
        return (self.Width * self.Height)/2

    def perimeter(self):
        """
        삼각형의 둘레의 길이를 반환
        :return: Width + n2 + n3
        """
        return self.Width + self.n2 + self.n3

    def getHeight(self):
        """
        삼각형의 높이를 반환
        :return: Height
        """
        return self.Height

    def getWidth(self):
        """
        삼각형의 밑변 길이를 반환
        :return: Width
        """
        return self.Width

    def getSides(self):
        """
        Triangle, Rectangle 클래스에는 변의 길이를 시계방향으로 list 형태로 반환하는 getSides() 메쏘드를 정의
        :return: list
        """
        tmp = [self.n3, self.Width, self.n2]
        return tmp

    def __str__(self):
        """
        삼각형 형태를 string 형태로 반환
        :return:
        """
        return "<삼각형> 밑변 : " + str(self.Width) + " 높이 : " + str(self.Height)


# s 변수는 도형이다.
s = Shape()
# 반지름이 5인 원을 정의하여 c 변수에 저장한다.
c = Circle(5)
# 가로, 세로가 5, 10인 직사각형을 정의하여 r에 저장한다.
r = Rectangle(5, 10)
# 세변이 3(밑변), 4, 5이고, 높이가 4인 삼각형을 정의하여 t에 저장한다.
t = Triangle(3, 4, 5, 4)

# c의 면적과 둘레를 출력한다.
print(c.area(), ", ", c.perimeter())
# r의 면적과 둘레를 출력한다.
print(r.area(), ", ", r.perimeter())
# t의 면적과 둘레를 출력한다.
print(t.area(), ", ", t.perimeter())
# t의 변들을 리스트로 받아 출력한다.
print(t.getSides())
"""
# 리스트 l을 정의하여, s, c와 r을 요소로 추가한다.
l = [s, c, r]
# l의 각 요소에 대해, 해당 요소를 출력하고, 면적과 둘레를 계산하여 출력한다.

for i in range(0,len(l)):
    print(l[i])
    print(l[i].area())
    print(l[i].perimeter())

# for문 안에서 테스트: getRadius() 메쏘드를 수행한다.(오류 발생)
#for i in l:
#    print(l[i].getRadius())
"""