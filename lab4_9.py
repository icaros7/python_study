"""
챕터 : Day 4
주제 : 반복문
문제 :
        밑변이 5개의 *로 구성된 직각 삼각형을 출력
        거꾸로 된 직각 삼각형을 출력
작성자 : 이호민
작성일 : 18.09.20
"""

for x in range(6, 0, -1):
    for y in range(6, x, -1):
        print("*", end=" ")
    print("")

for x in range(6, 1, -1):
    for y in range(1, x):
        print("*", end=" ")
    print("")
