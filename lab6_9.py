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
s5 = "test124"

r = re.compile('\d')  # 숫자만 찾아 반환
print(r.search(s1))
print(r.search(s5))

r = re.compile('\D')  # 숫자 아닌 것 만 찾아 반환
print(r.search(s1))
print(r.search(s5))


r = re.compile('[a-zA-Z]')  # 알파벳만 찾아 반환
print(r.search(s1))
print(r.search(s5))