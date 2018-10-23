"""
챕터 : Day5
주제 : 매개변수의 전달 방식 비교
문제 :
작성자 : 이호민
작성일 : 18.10.04
"""

# 매개변수의 수정 여부를 확인 할수 있는 함수 정의
# Python 은 기본적으로 call-by-value 방식
def modify(n):
    n+=1
    return n


k = 10  # 변수 정의
print("k=", k)  # 호출 전 변수 값 출력
re = modify(k)  # modify 함수 호출 후 결과 값 re에 저장
print("k=", k)  # 호출 후 변수 값 출력
print("re=", re)  # 리턴 받은 값 출력