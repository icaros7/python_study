"""
챕터 : Day4
주제 : 반복문
문제 : 사용자로부터 5개의 수를 입력받아, 이를 리스트에 저장한 후 합과 평균 구해 출력
작성자 : 이호민
작성일 : 2018.09.27
"""

l = input("5개의 수 입력 (공백으로 구분) : ").split()   # 5개의 수를 split을 통해 입력받음
l = [int (i) for i in l]   # 모두 int형으로 변환
sum = 0   # 합계 변수 초기화
for i in range(0, len(l)):
    sum += l[i]
print("합 : ", sum)
print("평균 : ", sum/len(l))
