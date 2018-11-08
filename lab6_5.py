"""
챕터 : Day 6
주제 : 상속
문제 :
1. 사람 클래스 정의 이름과 나이 에트리
2. 이름과 나이를 매개변수 받는 생성자
3. 나이를 1살 더하는 겟올더
4. 문자열 반환 트린트 Method

작성자 : 이호민
작성일 : 18.11.08
"""


class human:
    def __init__(self, n, o):
        """
        생성자
        :param n: str 이름
        :param o: int 나이
        """
        self.name = n
        self.older = o

    def getOlder(self):
        """
        나이 1 증가
        :return: 리턴값 없음
        """
        self.older += 1
        print(self.name + "씨 이제 한살 더 드셨네...")  # 안내 메시지 출력

    def __str__(self):
        """
        str override magic method
        :return: 이름과 나이 출력
        """
        return self.name + ", " + str(self.older) + "살"

    def print(self):
        """
        self 내용 출력
        """
        print(self)


"""
1. 생성자 내에서 사람의 생성자 (human.__init 을 포출)
2. stduent 도 일종의 haman이다.
3. human 이라서 가지고 있는 에트리뷰트인 나이와 이름
휴먼 생성자를 통해 초기화된다.
"""


class student(human):
    def __init__(self, n, o, gra, num, school):
        """
        :param n: str 이름
        :param o: int 나이
        :param gra: int 학년
        :param num: str 학번
        :param school: str 학교
        """
        print(school + " 신입생 입학" + "\n")  # 입학 안내
        human.__init__(self, n, o)  # human 생성자 이름과 나이로 출력
        self.stnum = num
        self.grade = gra
        self.school = school

    def Upgrade(self):
        """
        학년 +1
        :return: 리턴 값 없음
        """
        self.grade += 1
        print("진학을 축하드립니다.")  # 학년 진학 안내 메시지 출력

    def __str__(self):
        """
        str overload magic method
        그리고 human 의 __Str__을 다시 Overriden
        :return: 나이 학번 이름 학교 학년 출력
        """
        s = human.__str__(self)
        return s + " " + self.stnum + self.school + " " + str(self.grade) + "학년입니다."

    def print(self):
        """
        human 클래스에서의 정의한 print()를 override
        :return:
        """
        print(self)


homin = human("Homin Rhee", 21)
homin.print()

hominlab = student("이호민", 21, 1, "201735030", "성공회대학교")
hominlab.print()
hominlab.getOlder()  # hominlab 은 human 클래스 method 를 사용가능하다.
hominlab.Upgrade()  # 하지만 homin은 human.student 클래스 method 를 사용 불가능하다.
hominlab.print()

# human 과 Stduent를 포함하는 리스트 생성
lst = [homin, hominlab, homin, hominlab]
print("\n\n")
for i in lst:
    i.getOlder()
    i.print()