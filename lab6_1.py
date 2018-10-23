"""
챕터 : Day6
주제 : 클레스
문제 :
숫자를 하나씩 발생 시키는 Counter Class 정의
작성자 : 이호민
작성일 : 18.10.18
"""


class Counter:
    def __init__(self):
        """
        instance를 생성할때 초기화 하는 메서드
        """
        self.count = 0

    def __init__(self, start = 0):
        self.count = start

    def reset(self):
        """
        self: method가 수행되는 instance 자신을 의미
        :return:
        """
        self.count = 0  # counter는 instance variable(member)

    def incre(self):
        """
        카운터를 하나 증가시킴
        :return:
        """
        self.count += 1

    def get(self):
        """
        count 값을 반환
        :return:
        """
        return self.count


# 실행 코드 시작
a = Counter()
b = Counter(10)

a.reset()
a.incre()
a.incre()
a.incre()
a.incre()
print("a = %d" % a.get())

print("b = %d" % b.get())
