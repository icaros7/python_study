"""
챕터 : Day5
주제 : lambda 함수의 리스트
문제 :
작성자 : 이호민
작성일 : 18.10.11
"""


l = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for f in l:
    print(f(3))