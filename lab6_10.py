"""
챕터 : day 6
주제 : 정규식
문제 : 정규식 기호 연습
작성자 : 이호민
작성일 : 2018.11.20
"""

import re

s7 = "href =     \"C:\Python35\Kim.png\""
s8 = "href=\"C:\Python35\Kim.png\""
s5 = "test124TEST"

# s7에서 공백(\t도 포함)이 나타나는 곳 찾기
print(re.search('\s', s7))

# s7에서 공백(\t도 포함)이 아닌 것이 처음 나타나는 곳 찾기
print(re.search("\S", s7))

# s7과 s8에서 "href="가 있는 곳 찾기
print("\n<공백은 걸러보기>")
r = re.compile("href=")  # 하나의 패턴을 여러 문자열에서 찾고 있으므로 compile 후 search 이용
print(r.search(s7))
print(r.search(s8))

# s7과 s8에서 'href='가 있는 곳 위치 찾기. =의 좌우에 빈 칸이 있든 없든 상관없이 찾기
print("\n<공백 유무 상관 없이>")
r = re.compile("href\s*=\s*")
print(r.search(s7))
print(r.search(s8))

# s7과 s8에서 "C:\Python\Kim.png" 찾기
print(re.search('\\\\', s7))

# group 이용하기
r = re.compile("href\s*=\s*\"")
ret = r.search(s7)
print(ret.group())

# =를 기준으로 분리
print(re.split("=", s8))

# 주어진 패턴에 일치하는 부분문자열을 다른 문자열로 치환
print(re.sub("e+", "i", s7))

# 매칭되는 모든 문자열을 리스트로 반환
print(re.findall("\d", s5))

# s7에서 =좌우의 빈칸이 있든 없든 상관없이 찾아서 두개의 subgroup으로 나누기
r = re.compile("(href\s*=\s*)(\".*\")")
ret = r.search(s8)
print(ret.group(0))  # 0은 매칭되는 전체, 디폴트 매개변수 값이 0
print(ret.group(1))  # 1은 첫번째 ()에 매칭되는 부분
print(ret.group(2))  # 2는 두번째 ()에 매칭되는 부분
print(ret.group())  # subgroup을 튜플로 반환

