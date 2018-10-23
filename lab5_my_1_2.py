# 두수를 입력받은 후 C값이 0이면 합을, 1이면 n1 - n2의 결과를 변수로 저장해서 가공 후 출력하기


def cal(c, n1, n2):
    if c == 0:
        return n1 + n2
    elif c == 1:
        return n1 - n2
    else:
        return -1


c, in1, in2 = input("공백을 통해 구분 : ").split()
c = int(c)
in1 = int(in1)
in2 = int(in2)

result = int(cal(c, in1, in2))
print("정답은 %d 입니다." %result)

