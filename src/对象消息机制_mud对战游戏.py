from mod.class_role import Role,Player
from time import sleep
from random import sample

r=[Role('王昭君',10,30),#攻击力，生命值
   Role('程咬金',5,40),
   Role('李世民',20,20),
   Player('张三',10,40)
   ]

print(f'\n**************游戏开始***************')
while len(r)>=2:
    c=sample(r,2)
    r1=c[0]
    r2=c[1]

    r1.attack(r2)

    if r2.blood<=0:
        r.remove(r2)

    sleep(0.5)

print(f'**************最终获胜者是：{r[0].name}***************')