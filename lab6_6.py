"""
챕터 : day 6
주제 : 정규식
문제 : 정규식 연습
작성자 : 이호민
작성일 : 2018.11.15
"""

import re  # regular expression 모듈을 수입
r = re.compile('p.')  # re 모듈의 compile 을 호출. p를 찾고싶음. 해당 문자열을 찾을때 사용하는 regualr
                      # expression 객체가 반환됨. "."은 임의의 한 문자를 의미
print(r.search("pizza"))  # pizza 문자열에서 해당 하는 부분에 대한 정보 반환
print(r.match("pizza"))  # pizza 문자열에서 맨 앞에 [z]에 매칭되눈 부분에 대한 정보가 반환

r = re.compile('[z]')  # [] 안에 찾고 싶은 문자 열거
print(r.search("pizza"))  # pizza 문자열에서 해당 하는 부분에 대한 정보 반환
print(r.match("pizza", 2))  # pizza 문자열에서 맨 앞에 [z]에 매칭되눈 부분에 대한 정보가 반환