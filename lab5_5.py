"""
챕터 : Day5
주제 : 함수
문제 : 두개의 정수를 매개변수로 받아서, 두 수의 차를 반환하는 함수 sub를 정의.
      4, 8을 매개변수로 sub를 호출 한 후 결과 출력
작성자 : 이호민
작성일 : 18.10.04
"""


# 두 수의 차를 반환하는 sub 정의
def sub(a, b):
    return a - b


print(sub(4, 8))
print(sub(b = 8, a = 4))

a = 10
b = True
c = "김치"


print(type(a))
print(type(b))
print(type(c))