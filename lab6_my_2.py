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
        # 결과의 분모 계산
        d = self.denom * o.denom
        # 결과의 분자 계산
        n = self.numer * o.numer
        tong = gcd(n, d)  # 곱셈의 경우 분자와 분모의 최대 공략수를 구해 저장
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
        # 이쁘게 보여주기 위한 음수 괄호 묶음
        if (self.numer < 0) and (self.denom > 0):
            return "-(" + str(abs(self.numer)) + "/" + str(self.denom) + ")"
        elif (self.numer > 0) and (self.denom < 0):
            return "-(" + str(self.numer) + "/" + str(abs(self.denom)) + ")"
        elif (self.numer < 0) and (self.denom < 0):
            return "-(" + str(abs(self.numer)) + "/" + str(abs(self.denom)) + ")"
        else:
        """
        # 음수 괄호 묶지 않은채 각개 출력
        return "(" + str(self.numer) + "/" + str(self.denom) + ")"

    def __eq__(self, o):  # == 연산자 계산
        n1 = self.numer * o.denom
        n2 = o.numer * self.denom
        if n1 == n2:
            return True
        else:
            return False

    def __lt__(self, o):  # < 연산자 계산
        n1 = self.numer * o.denom
        n2 = o.numer * self.denom
        if n1 < n2:
            return True
        else:
            return False

    def __le__(self, o):  # <= 연산자 계산
        n1 = self.numer * o.denom
        n2 = o.numer * self.denom
        if n1 <= n2:
            return True
        else:
            return False

    def __ne__(self, o):  # != 연산자 계산
        n1 = self.numer * o.denom
        n2 = o.numer * self.denom
        if n1 != n2:
            return True
        else:
            return False

    def __ge__(self, o):  # >= 연산자 계산
        n1 = self.numer * o.denom
        n2 = o.numer * self.denom
        if n1 >= n2:
            return True
        else:
            return False

    def __gt__(self, o):  # > 연산자 계산
        n1 = self.numer * o.denom
        n2 = o.numer * self.denom
        if n1 > n2:
            return True
        else:
            return False


# 조건에서 주어진 각 분수 생성
f1_1 = Fraction(-4, 5)
f1_2 = Fraction(3, 2)

f2_1 = Fraction(8, 31)
f2_2 = Fraction(2, 3)

f3_1 = Fraction(3, 5)
f3_2 = Fraction(3, 7)

f4_1 = Fraction(4, 8)
f4_2 = Fraction(1, 2)

f5_1 = Fraction(2, 81)
f5_2 = Fraction(3, 9)

print(f1_1 * f1_2)
print(f2_1 - f2_2)
print(f3_1 + f3_2)
print(f4_1 == f4_2)
print(f5_1 >= f5_2)