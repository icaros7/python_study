class cont:
    name = "Homin Rhee"
    age = 21

    def __init__(self,inname):
        self.name = inname

    def say(self):
        print("저는 %d살 %s 입니다." % (self.age, self.name))


homin = cont("H0min Rhee")
homin.say()

yi = cont("Yijun Park")
yi.age = 22
yi.say()