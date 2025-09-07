s='''
A公司，发货5000台，联系人：张三，电话 010 - 88223343,邮箱zs@a.com
B公司：联系人：李四，电话：0418-5566778, 邮箱：lisi@b.com
C公司发货200台，联系人： 王五，电话是(024)66667777, 邮箱：wangwu@c.com。 
D公司电话联系，联系人：赵六，电话0520-33227788,邮箱是 zhaoliu@d.com.
E公司联系人：田七，电话 01083232563,邮箱 tianqi@e.com
F公司，联系人：John   Willams,电话 (001)33243334,邮箱 johnw@f.com
G公司，联系人：Ken  Wang, 电话(001)56523333,邮箱 kenwang@g.com
'''
import re
a=re.findall('电话[是\s:：(]*(\d+)[)\s-]*(\d*)',s)
print(a)
for i,j in a:
    print(i,j)
 