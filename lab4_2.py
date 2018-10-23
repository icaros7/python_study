"""
챕터 : Day4
주제 : 조건문
문제 : 사용자로부터 3개의 수를 입력받아, 가장 작은 수를 출력하라
작성자 : 이호민
작성일 : 18.09.18
"""

temp0 = int(input())
temp1 = int(input())
temp2 = int(input())

if temp0 >= temp1:
    if temp1 >= temp2:
        print(temp0)
elif temp1 >= temp2:
    if temp1 >= temp0:
        print(temp1)
elif temp2 >= temp0:
    if temp2 >= temp1:
        print(temp2)
