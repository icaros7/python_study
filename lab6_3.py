"""
챕터 : Day 6
주제 : Class
문제 : fraction 클래스는 애트리뷰트로 numer와 denom (분자와 분모)를 가진다. 초기화하는 메서드를 정의하라
작성자 : 이호민
작성일 : 2018.10.18
"""


# 분수 클래스 정의
class Fraction:
    def __init__(self, n, d):
        """
        초기화 함수
        :param n: 분자
        :param d: 분모
        """
        self.numer = n
        self.denom = d

    def print(self):
        print("%d/%d" % (self.numer, self.denom))

    # 분자를 반환하는 메서드
    def getNumer(self):
        return self.numer

    # 분모를 반환하는 메서드
    def getDenom(self):
        return self.denom

    # 분자 설정
    def setNumer(self, n):
        self.numer = n

    # 분모 설정
    def setDenom(self, d):
        self.denom = d

    def add(self, o: object):
        """
        self에 o를 더하여 결과 값 반환
        self 값을 변경하지 않는다.
        :param o: self에 더할 분수
        :return: 더한 결과 값을 반환
        """
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer*o.denom + self.denom*o.numer
        r = Fraction(n,d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r


# 클래스 정의 끝
half = Fraction(1, 2)
half.print()  # self 매개변수에는 half가 직접 전달된다.

# 분수 2/7을 저장하는 변수 f1을 정의
f1 = Fraction(2,7)

# f1 출력
f1.print()

# 분수 1/8을 저장하는 변수 f2를 정의
f2 = Fraction(1,8)

# f2의 분자 분모를 return을 통해 출력
print("분자 : ", f2.getNumer())
print("분모 : ", f2.getDenom())

# f2의 타입 출력
print(type(f2))

# 어떤 타입의 인스턴스인지 불리언 값을 반환하는 isinstance 함수를 호출하여 출력
print(isinstance(f2, Fraction))

# f2를 2/8로 수정
f2.setNumer(2)
f2.print()

# f1과 f2를 더한 결과를 출력
f1.add(f2).print()  # f1.add()의 반환 타입이 FRaction이므로 Fraction의 메쏘드인 print() 수행 가능
