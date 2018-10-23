"""
챕터: Day 3
주제: 문자열 함수
작성자: 이호민
작성일: 2018.9.6
"""

s = "   Test your Python debugging skills    "
print(s.upper())  # 대문자로 변환
print(s.lower())  # 소문자로 변환

# 문자열 안의 t의 개수를 출력
print("소문자 t 개수 :", s.count('t'))
print("대문자 t 개수 :", s.count('T'))

# 사용자로부터 문자를 입력 받아, 대소문자 구분 없이 해당 문자의 개수를 출력
user_in = 'g'  # input()  # 사용자로부터 문자 입력받기
buffer = [user_in.upper(), user_in.lower()]  # 배열에 입력받은 문자 대문자와 소문자 저장
print("문자열에 있는", user_in, "개수 :", s.count(buffer[0]) + s.count(buffer[1]))  # 소문자 개수와 대문자 개수 합쳐 출력

"""
user_in = user_in.upper() 를 사용할 경우 user_in 에 대문자 값이 반환.
"""

# t가 있는 위치를 출력
print(s.index('t'))
print(s.index('t', 4))  # 두번째 매개변수는 검색 시작 위치


# index() 함수는 찾으려는 문자가 없으면 오류 발생
# print(s.index('x))

# 대상 문자를 찾을 수 있는 또 다른 함수
print(s.find('t'))
print(s.find('x'))  # 찾으려는 문자가 없는 경우 -1 반환

# strip()함수 테스트
print(s)

# 왼쪽 공백 제거 후 출력
print(s.lstrip())
# 오른쪽 공백 제거 후 출력
print(s.rstrip())
# 양쪽 공백 제거 후 출력
print(s.strip())
print('\n')

# 내용 바꾸기
# 문장에서 Python 을 Java로 바꾸어 출력
print(s.replace('Python','Java'))
print(s)  # s replace() 함수는 직접 반환만 하지 직접 바꾸진 않는다.

# 문장에서 e를 i로 모두 바꾸어 출력
print(s.replace('e','i',1))  # 3번째 매개변수는 변경할 최대 개수를 지정

# 문자열 나누기
# split. 빈칸을 기준으로 단어를 모두 나누기
print(s.split(' '))

# 앞 뒤 공백을 제거 한 후 빈칸을 기준으로 단어를 모두 나누기
print(s.strip().split(' '))  # strip() 함수 호출시 공백 제거. 같은 s를 타깃으로 하는 경우 그 뒤에 그대로 적으면 됨.
# 다만 strip의 반환은 문자열이 아닌 문자열의 배열.
print(s.strip().split(" ", 2))  # 두개만 떼어 내기

# s의 길이를 출력
print(len(s))

s = 'test'
s = '   kkk'
s = '''
Ho
min
Rhee
'''

print(s)  # '''를 적을 경우 개행해서 입력 가능

i = input("여기에 매개변수를 적으면 안내문이됨 : ")  # i의 데이터 타입은 문자열. input은 문자열을 반환하기 때문

# 변환 함수

i = int(input('문자열: '))  # i의 데이터 타입은 int.

j= 100  # j는 int
s1 = str(j)  # s1은 str 타입.
