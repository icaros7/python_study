"""
챕터 : Day 6
주제 : Class
문제 : 정수집합 클래스
1. inSet 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 self.vals를 애트리뷰트로 가진다.
2. 새로우 정수 e를 추가하는 insert method. 해당 요소가 이미 있으면 추가 안함
3. e가 정수집함에 포함되어있는지 환인하는 method involve 정의 (bool)
4. e를 제거하는 remove method
5. 단, e가 해당 집합에 없다면 적당한 오류 메시지 출력
6. 집합 형식의 문자열로 반환시켜주는 __str__ magic method. 단, 정수들은 정렬되어 반환
"""


class intSet:
    def __init__(self):
        self.vals = []

    def insert(self, user_in):
        if self.involve(user_in):
            print("이미 존재하는 값 입니다.")
        else:
            self.vals.append(user_in)

    def involve(self, user_in):
        for i in range(1, len(self.vals)):
            if self.vals[i] == user_in:
                return True
            else:
                return False

    def remove(self, user_in):
        if self.involve(user_in):
            self.vals.remove(user_in)
        else:
            print("해당 하는 값은 없습니다.")

    def __str__(self):
        self.vals.sort()
        s = ""
        for i in range(0,len(self.vals)):
            s+=str(self.vals[i]) + " "
        return s


# intSet를 저장하는 변수 s를 정의
s = intSet()

# s에 insert를 이용하여 5,3,7를 삽입
s.insert(5)
s.insert(3)
s.insert(7)

# s에 8이 있는지 결과 출력
print(s.involve(8))

# s에 3이 있는지 결과 출력
print(s.involve(3))

# s에서 3을 제거
s.remove(3)

# s에서 4를 제거
s.remove(4)

# s를 정렬하여 출력
print(s)