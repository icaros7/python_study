"""
챕터 : Day 7
주제 : os 모듈 사용
문제 : 현재 디렉토리 아래 과일.txt 를 생성하여, 사용자가 입력하는 과일을 한 줄에 하나씩 3개를 저장하라
작성자 : 이호민
작성일 : 2018.12.06
"""

f=open("과일.txt", "at")  # wt 덮어쓰기, at 추가
for i in range(0,3):
    s = input("과일 : ")
    f.write(s)
    f.write(":")  # 같은 줄에 과일이름과 저장
    price = int(input("가격 : "))  # 가격을 받음
    f.write(str(price))  # 가격을 저장
    f.write("\n")
f.close()