class MiShu:#类名首字母大写，驼峰命名法。
    name='无'
    age=0
    def __init__(self,n='无名',a=0,i='A000'):
        self.name= n
        self.age = a
        self.id = i

    def say_hello(self):
        print(f'领导您好，我是{self.name},年龄{self.age}，工号{self.id}')
    def make_schedule(self):
        print('安排日程')
    def do_add(self,x,y):
        print(f'{self.name}算好了，计算结果是{x+y}')

if __name__=='__main__':
    a=MiShu('张三',29,'A013')
    b = MiShu()

    a.say_hello()
    b.say_hello()
    a.do_add(3,5)
    print(MiShu.name)
    print(a.name)