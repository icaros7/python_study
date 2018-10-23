"""
챕터 : Day5
주제 : 재귀함수
문제 : 팩토리얼 계산 함수 fact를 재귀로 정의. 5 호출
작성자 : 이호민
작성일 : 18.10.11
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))

sum = 1

print(sum)
