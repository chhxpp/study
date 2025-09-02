from random import sample,randint

姓=['赵','钱','孙','李']
名 =['慧','芝','雅','琳','秋','月','虹','云']*2

名单=[]
i=0
while i<20:
    人物=''.join(sample(姓,1)+sample(名,randint(1,2)))
    if 人物 not in 名单:
        名单.append(人物)
        i+=1

print(list(set(名单)))