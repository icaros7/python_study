"""
챕터 : Day5
주제 : 재귀함수
문제 : 곱하기를 더하기 반복문으로 구현한 함수 prod를 정의 3,6 계산
작성자 : 이호민
작성일 : 18.10.11
"""


def prod(n1, n2):
    tmp = 0
    for i in range(0,n2):
        tmp += n1
    return tmp


def r_prod(n1, n2):
    if n2 == 1:
        return n1
    else:
        return 3+r_prod(n1, n2-1)

print(prod(3, 6))

print(r_prod(3, 6))

