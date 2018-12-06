"""
챕터 : Day 7
주제 : os 모듈 사용
문제 : 현재 디렉토리 아래 과일.txt에 저장되어있는 과일 이름을 출력하라. 몇 줄의 과질이 저장되어있든지 상관없이 출력됨을 보장하라
작성자 : 이호민
작성일 : 2018.12.06
"""

f=open("과일.txt", "r")  # wt 덮어쓰기, at 추가
l = f.readlines()
sum = 0
for s in l:
    fr=s.split(":")
    print("과일명 : ", fr[0])
    print("과일가격 : ", fr[1])
    sum += int(fr[1])
print("과일 가격 합 : ", sum)
