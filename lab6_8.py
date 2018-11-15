"""
챕터 : day 6
주제 : 정규식
문제 : 정규식 ^$ [^] - 기호 연습
작성자 : 이호민
작성일 : 2018.11.15
"""

import re  # regular expression 모듈을 수입

s1 = "teeeeest"
s2 = "tetst"
s3 = "tst"

r = re.compile('^t')  # t로 시작하는 부분을 찾아서 반환
print(r.search(s1))
print(r.search(s2))
print(r.search(s3))

r = re.compile('t$')  # t로 끝나는 부분을 찾아서 반환
print(r.search(s1))
print(r.search(s2))
print(r.search(s3))


r = re.compile('[^te]')  # te가 아닌 것 찾기
print(r.search(s1))
print(r.search(s2))
print(r.search(s3))

r = re.compile('[a-m]')  # a에서 m까지 찾기
print(r.search(s1))
print(r.search(s2))
print(r.search(s3))