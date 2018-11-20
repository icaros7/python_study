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
