"""
챕터 : Day 6
주제 : Class
문제 : Fraction 메서드의 4칙 연산을 완성하라
작성자 : 이호민
작성일 : 2018.10.24
"""

# 최대공략수를 찾아주는 math.gcd 를 쓰기위해 math 모듈 중 gcd import
from math import gcd


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

    def print(self, inp: object, o: object, calc):
        print("%d/%d %s %d/%d = %d/%d" % (inp.numer, inp.denom, calc, o.numer, o.denom, self.numer, self.denom))  # 보기 좋게 출력

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def setNumer(self, n):
        self.numer = n

    def setDenom(self, d):
        self.denom = d

    def add(self, o: object):
        """
        덧셈
        :param o: self에 더할 분수
        :return: 더한 결과 값을 반환
        """
        tong = gcd(self.denom, o.denom)  # 최대공약수 값을 구해 저장
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.denom + self.denom * o.numer
        if (n % tong == 0) and (d % tong == 0):  # 통분해야할 것이 있다면
            r = Fraction(n / tong, d / tong)  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def minus(self, o: object):
        """
        뺄셈
        :param o: self에 뺄 분수
        :return: 뺄 결과 값을 반환
        """
        tong = gcd(self.denom, o.denom)  # 최대공약수 값을 구해 저장
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.denom - self.denom * o.numer
        if (n % tong == 0) and (d % tong == 0):  # 통분해야할 것이 있다면
            r = Fraction(n / tong, d / tong)  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def times(self, o: object):
        """
        곱셈
        :param o: self에 곱할 분수
        :return: 곱한 결과 값을 반환
        """
        tong = gcd(self.denom, o.denom)  # 최대공약수 값을 구해 저장
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.numer
        if (n % tong == 0) and (d % tong == 0):  # 통분해야할 것이 있다면
            r = Fraction(n / tong, d / tong)  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def div(self, o: object):
        """
        나눗셈
        :param o: self에 나눌 분수
        :return: 나눈 결과 값을 반환
        """
        tong = gcd(self.denom, o.denom)  # 최대공약수 값을 구해 저장
        # 결과의 분모 계산
        d = self.denom * o.numer
        # 결과의 분자 계산
        n = self.numer * o.denom
        if (n % tong == 0) and (d % tong == 0):  # 통분해야할 것이 있다면
            r = Fraction(n / tong, d / tong)  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r


f1 = Fraction(1, 2)  # Fraction 인스턴스 생성
f2 = Fraction(5, 4)  # Fraction 인스턴스 생성

f1.add(f2).print(f1, f2, "+")
f1.minus(f2).print(f1, f2, "-")
f1.times(f2).print(f1, f2, "*")
f1.div(f2).print(f1, f2, "/")
