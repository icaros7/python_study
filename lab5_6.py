"""
챕터 : Day5
주제 : 함수
문제 : sum 함수 이용
작성자 : 이호민
작성일 : 18.10.04
"""

# 1에서 30까지 합 출력
print(sum(range(1,31)))

# 1,3,5,7을 list로, tuple로, set으로 전달하여 출력
l = [1, 3, 5, 7]
print(sum(l))
t = (1, 3, 5, 7)
print(sum(t))
se = {1, 3, 5, 7}
print(sum(se))

# 50에 1,3,5,7의 합을 더하여 출력
print(sum(l,50))