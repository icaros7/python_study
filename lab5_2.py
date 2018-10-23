"""
챕터 : Day 5
주제 : 함수
문제 : 문자열의 투플을 매개변수로 받아서, 해당 문자열들을 ', '로 한줄에 연결하여 출력하는 함수 print_string을 정의
소프, 정통, 글티, 컴공을 요소로 가지는 튜플을 매개변수로 해서 print_string을 출력
작성자 : 이호민
작성일 : 18.10.02
"""


def print_string(*a):  # print_string 정의
    s = ""
    for i in range(0, len(a)):
        if i != len(a) - 1:
            s = s + a[i] + ", "  # 마지막 요소 전까지 , 를 포함해 문자열 스텍
            # print(a[i], end=", ")  # 마지막 요소 전까지 , 를 포함해 출력
        else:
            # print(a[i])  # 마지막 요소는 , 없이 출력 후 개행
            s = s + a[i]  # 마지막 요소는 , 없이 문자열 스텍
    return s  # 문자열 반환


print(print_string("소프트웨어공학과", "정보통신공학과", "글로컬IT학과", "컴퓨터공학과"))
