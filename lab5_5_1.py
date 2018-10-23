"""
챕터 : Day5
주제 : 함수
문제 : min 함수 이용
작성자 : 이호민
작성일 : 18.10.04
"""

# l 변수에 [4,7,9,11,-5]를 저장
# l에서 최소값 출력

l = [4, 7, 9, 11, -5]
print(max(l))
print(min(l))

# fruits 뱐수에 사과 오렌지 파나나를 튜플로 ㄲ
# 이거에서 최대 최소 출력

fruits = ("apple", "Orange", "banana")
print(max(fruits))
print(min(fruits))


# 대소문자를 구분하지 않고 최대, 최소를 얻기 위해
# max ,min 함수의 마지막 key 매개변수로 str.low를 전달

print(max(fruits, key=str.lower))
print(min(fruits, key=str.lower))


# 1부터 50까지 최대, 최소값 출력

ll = range(1, 51)
print(max(ll))
print(min(ll))

# min 함수에 직접 1,3,6 을 전달하여 출력
print(min(1,3,6))