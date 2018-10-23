"""
챕터 : Day5
주제 : 함수
문제 : 이름, 학번, 학과를 매개변수로 받아서 이를 출력하는 함수 print_me 정의. 이때, 학과가 매개변수로 없으면 소프를 디폴트로
작성자 : 이호민
작성일 : 18.10.04
"""


def print_me(name, num, kind="소프트웨어공학과"):  # print_me 함수 정의 및 기본 값 설정
    print(name)
    print(num)
    print(kind)


name1 = input("이름 : ")
num1 = input("학번 : ")
print("학과 : ", end="")  # 기본값 지정을 위한 promt값 제거
kind1 = input()

print_me(name1, num1, kind1)
