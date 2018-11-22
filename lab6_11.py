"""
챕터 : day 6
주제 : 정규식
문제 : 정규식 연습
작성자 : 이호민
작성일 : 2018.11.22
"""

import re


# apple에 A가 들어있는지 확인
st1 = "apple"
print(re.search("a", st1))

# apple에 b가 들어있느닞 확인
st1 = "apple"
print(re.search("b", st1))

# 정규식을 이용하여, 사용자가 입력한 영어 문장에서 a,e,i,o,u가 포함되어 있는지 찾아서 출력하시오. 만족하는 첫번째만 출력한다.
# <입력> This is a test
st2 = input("input : ")
print(re.match("[a,e,i,o,u]", st2))

# 입력한 단어가 a로 시작하는지 확인

# 입력한 단어가 e로 끄탄는지 확인


# 입력된 문장에서 숫자부분을 모두 출력하라.
r = re.compile("\d")
inp = input("input : ")
ret = r.search(inp)
tmp = ret.group(0)
i = 0
print(tmp)

"""
<입력> 2018년 11월 22일 50000원
<출력>
2018
11
22
50000
"""

