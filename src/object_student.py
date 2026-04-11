class Student:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def study(self, time):
        print(f"{self.name}已经学习了{time}小时")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
    
xiao_ming = Student("小明", 18, 175, 120)

xiao_ming.gen = "gunship"   # 增加一个性别(gen)变量，设为“武装直升机”

xiao_ming.weight = 150      # 将体重改为150

xiao_ming.study(6)          # "小明已经学习了6小时"

if xiao_ming.is_adult():    # 小明是成年人
    print(f"{xiao_ming.name}是成年人")
else:
    print(f"{xiao_ming.name}是未成年")

