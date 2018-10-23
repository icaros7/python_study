"""
챕터 : Day 5
주제 : 함수
문제 : 문자열이 몇 개 들어올 지 예상할 수 없다고 자정하자. 여러 개의 문자열을 매개변수로 받아서, 해당 문자열들을 ','로 연결하여
출력하는 함수 print_string을 재 정의 한다. 사과,오렌지, 딸기를 매개변수로 ㅇㅇㅇㅇ
작성자 : 이호민
작성일 : 18.10.02
"""


def print_string(*a):  # print_string 정의
    s = ""
    for i in range(0, len(a)):
        if i != len(a) - 1:
            s = s + a[i] + ", "  # 마지막 요소 전까지 , 를 포함해 문자열 스텍
        else:
            s = s + a[i]  # 마지막 요소는 , 없이 문자열 스텍
    return s  # 문자열 반환


print(print_string("사과", "오렌지", "딸기"))
