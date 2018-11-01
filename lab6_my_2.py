"""
챕터 : Day 6
주제 : Class
문제 :  과제 11에 아래와 같은 것들을 추가하라

        - 음수가 작동됨을 보장하라
        - +, -, *, /, ==, !=, <, <=, >, >= 을 재정의하라.
        - __str__ 함수를 정의하라.

        아래 값들을 보기 좋게 출력하라. 약분된 결과가 나와야 한다.
        (-4/5) * (3/2) =
        (8/31)-(2/3) =
        (3/5)+(3/7) =
        (4/8) == (1/2) 의 결과
        (2/81) >= (3/9) 의 결과

작성자 : 이호민
작성일 : 2018.11.01
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

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def setNumer(self, n):
        self.numer = n

    def setDenom(self, d):
        self.denom = d

    def __add__(self, o: object):
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
            r = Fraction(int(n / tong), int(d / tong))  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def __sub__(self, o: object):
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
            r = Fraction(int(n / tong), int(d / tong))  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def __mul__(self, o: object):
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
            r = Fraction(int(n / tong), int(d / tong))  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def __truediv__(self, o:object):
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
            r = Fraction(int(n / tong), int(d / tong))  # 결과값을 통분 한 뒤 해당 값으로 Fraction 분수 생성
        else:
            r = Fraction(n, d)  # 결과 값을 포함하는 Fraction 분수 생성
        return r

    def __str__(self):
        """
        if (self.numer < 0) and (self.denom > 0):
            return "-(" + str(abs(self.numer)) + "/" + str(self.denom) + ")"
        elif (self.numer > 0) and (self.denom < 0):
            return "-(" + str(self.numer) + "/" + str(abs(self.denom)) + ")"
        elif (self.numer < 0) and (self.denom < 0):
            return "-(" + str(abs(self.numer)) + "/" + str(abs(self.denom)) + ")"
        else:"""
        return "(" + str(self.numer) + "/" + str(self.denom) + ")"

    def __eq__(self, other):
        """
        통분 해야하는가?
        """
        g1 = gcd(self.numer, self.denom)
        g2 = gcd(other.numer, other.denom)
        if (self.numer//g1 == other.numer//g2) and (self.denom//g1 == other.denom//g2):
            return True
        else:
            return False

    def __ne__(self, other):
        """
        두 분수가 같으면 참, 다르면 거짓
        """
        if self == other:
            return True
        else:
            return False


f1 = Fraction(-1, -2)  # Fraction 인스턴스 생성
f2 = Fraction(-5, -4)  # Fraction 인스턴스 생성

print(f1, "+", f2, "=", f1 + f2)
print(f1, "-", f2, "=", f1 - f2)
print(f1, "*", f2, "=", f1 * f2)
print(f1, "/", f2, "=", f1 / f2)
