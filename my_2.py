"""
입력된 문자열에서 bob이 몇 번 나타나는지 계산하여 출력하시오.
주어진 문자열 : azcbobobegghakl
"""


s = input("input : ")  # 사용자로부터 문자열 입력 받음
cnt = 0  # 횟수 카운터 초기화
for i in range(0,len(s)-2):  #문자열 탐색
    tmp = s[i] + s[i+1] + s[i+2]  #bobob도 구분하기 위하여 현 인덱스 값으로부터 뒤 2글자까지 조합하여 탐색
    if tmp == "bob":  # 해당 조합이 bob이라면 카운터 +1
        cnt += 1
print("Number of times bob occurs is: ", cnt)  # 카운터 출력
