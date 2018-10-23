"""
챕터 : Day5
주제 : 매개변수의 전달 방식 비교
문제 :
작성자 : 이호민
작성일 : 18.10.04
"""


# 매개변수의 수정 여부를 확인 할수 있는 함수 정의
# Python 은 기본적으로 call-by-value 방식
def modify1(s):
    s += " to u :)"
    return s


msg = "Happy birthday"
print("msg =", msg)  # 호출 전 문자열
re = modify1(msg)
print("msg =", msg)  # 호출 후 문자열
print("re  =", re)



s="가나다라마바사아자차카타파하"

print(s[3:10:2])#5
print(len(s))#6
print(s[10::-1])#7
