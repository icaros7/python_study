"""
챕터 : day 6
주제 : 정규식
문제 : 정규식 기호 연습
작성자 : 이호민
작성일 : 2018.11.15
"""

import re  # regular expression 모듈을 수입

s1 = "teeeeest"
s2 = "tetst"
s3 = "tst"
s4 = "apple"
s5 = "test124TEST"
s6 = "나는 \"왕\"이다"
# re라는 모듈에 컴파일을 수입

r = re.compile('\d')  # 숫자만 찾아 반환
print(r.search(s1))
print(r.search(s5))

r = re.compile('\D')  # 숫자 아닌 것 만 찾아 반환
print(r.search(s1))
print(r.search(s5))

r = re.compile('[a-zA-Z]')  # 알파벳만 찾아 반환
print(r.search(s1))
print(r.search(s5))

# 26~28까지 코드를 함수인 search를 이용하여 다시 쓰기
print("\nGoTo Method\n")
print(re.search("[a-zA-Z]", s1))
print(re.search("[a-zA-Z]", s5))

# s5에서 알파벳 또는 숫자 찾기
print(re.search("[a-zA-Z0-9]", s5))

# s5에서 숫자 찾기
print(re.search("[0-9]", s5))

# s5에서 대문자 찾기
print(re.search("[A-Z]", s5))

# s5에서 소문자 찾기
print(re.search("[a-z]", s5))

# s6에서 "의 위치를 찾기
print(re.search('\"', s6))

print(re.search('\W', s6))  # \W 문자나 숫자가 아닌것 반환. 공백 등