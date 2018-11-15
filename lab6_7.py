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

r = re.compile('e.s')  # e와 s 사이에 문자가 하나 있는 경우 찾기
print(r.search(s1))  # es
print(r.search(s2))  # ets
print(r.search(s3))  # 없음

r = re.compile('e?s')  # e가 0~1번 나타난 후 s가 나타나는 경우 찾기
print(r.search(s1))  # es
print(r.search(s2))  # s
print(r.search(s3))  #s


r = re.compile('e*s')  # e가 0번 이상 존재한 후 s가 타나나는 경우 찾기
print(r.search(s1))  # eeeees
print(r.search(s2))  # s
print(r.search(s3))  # s