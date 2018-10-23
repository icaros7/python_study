class man :
    name = "homin Rhee"
    def intro(self):
        print("내이름은 %s" %self.name)

class man_child(man):
    def hello(self):
        print("내 이름은 %s 2세 입니다" %self.name)


yi=man_child()
yi.hello()