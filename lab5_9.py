"""
챕터 : Day5
주제 : call by reference
문제 :
1. list를 받아서 마지막에 리스트의 요소의 개수를 요소로 추가하는 함수 addnum을 정의. 반환 노놉
2. [5,9,14,3]을 저장하는 list변수 l를 정의
3. l를 인수로 addnum함수를 호출한 후 l출력
작성자 : 이호민
작성일 : 18.10.11
"""

global_v = 100  # 전역 변수


# 매개변수 수정 여부 확인을 위한 함수 정의
def addnum(lst):
    global global_v  # global 변수라 정의 / 정의하지 않는다면 기본적으로 local변수로 인
    global_v = 200
    lst.append(len(lst))


# call-by-reference 방식으로 매개변수 값 전달
l = [5, 9, 14, 3]
addnum(l)
print(l)
print(global_v)
