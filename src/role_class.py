from random import  randint
from inputimeout import inputimeout, TimeoutOccurred
import time
import sys
import threading

class Role:
    def __init__(self,nm,pwr,bld):
        self.name=nm
        self.power=pwr
        self.blood=bld
        self.power_out=self.power

    def attack(self,enemy):
        print(f'【{self.name}】对【{enemy.name}】发起{self.power}点攻击')
        enemy.hurt(self)

    def hurt(self,attacker):
        self.blood-=attacker.power_out
        if self.blood<=0: self.blood=0
        暴力 = '暴力' if attacker.power_out>attacker.power else ''  # 三元表达式
        print(f'【{self.name}】受到【{attacker.name}】{attacker.power_out}点{暴力}攻击,血量->{self.blood}', end='')
        self.die() if self.blood <= 0 else print()  # 三元表达式

    def die(self):
        print(f'------【{self.name}】卒')

class Player(Role):
    def attack(self, enemy):
        # 倒计时显示函数
        def countdown():
            initial_prompt = f"请玩家【{self.name}】选择对【{enemy.name}】的攻击方式：1-常规、2-疯狗"
            for i in range(3, 0, -1):
                sys.stdout.write(f"\r{initial_prompt}  {i}秒{' ' * 10}")
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write(f"\r{initial_prompt} 自动选择疯狗模式！{' ' * 10}\n")
            sys.stdout.flush()

        # 启动倒计时线程
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.daemon = True
        countdown_thread.start()

        try:
            # 注意这里不再重复打印提示，因为倒计时线程已经在显示了
            s = inputimeout(prompt='', timeout=3)
        except TimeoutOccurred:
            s = '2'  # 超时默认选择2

        # 确保倒计时线程结束
        countdown_thread.join(timeout=0.1)

        if s == '2':
            self.power_out = randint(0, 3) * self.power
            self.blood -= 1
            enemy.hurt(self)
        elif s == '1':
            self.power_out = self.power
            enemy.hurt(self)
        else:
            print(f'{self.name}操作失误，错过本次攻击')