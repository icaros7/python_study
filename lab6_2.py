"""
챕터 : Day6
주제 : 클레스
문제 : 좌표를 표현하는 클래스 loca 정의
1. __init__는 x,y자표 받아서 self의 x,y배정
2. 거리를 구하는 dist 메서드 정의. self와 다른 좌표 other를 매개변수로
거리는 x좌표 사이의 차의 제곱(**2로 계산)과 y좌표 사이 차의 제곱의 합의 제곱근이다. 제곱근(**0.5)
작성자 : 이호민
작성일 : 18.10.18
"""

class loca:
    def __init__(self, x,y):
        """
        python에서는 __init__함수를 클레스당 하나만 가능
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def dist(self,other):
        tmp = ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5
        if tmp < 0:
            return -tmp
        else:
            return tmp


a = loca(3,4)
other = loca(0,0)
print("거리 : %.2f" %a.dist(other))
cl = loca(10,9)
print("거리 : %.2f" %cl.dist(a))
print("거리 : %.2f" %loca.dist(cl, other))