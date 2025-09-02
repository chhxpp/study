class MiShu:
    def __init__(self):
        self.__loc=0

    def say_hello(self):
        print(f"Hello, I am  {self.name}.")
    
    def do_add(self,*x):
        print(f'{self.name}说结果是{sum(x)}')

if __name__ == "__main__":
    m1=MiShu()
    m2=MiShu()
    m1.name="张三"
    m2.name="李四"
    m1.say_hello()
    m2.say_hello()
    m1.__loc=999
    m1.do_add(1,2,3,4,5)
    m2.do_add(3,4)

