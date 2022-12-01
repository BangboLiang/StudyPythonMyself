'''
Python3 循环语句
本章节将为大家介绍 Python 循环语句的使用。
Python 中的循环语句有 for 和 while。
'''

'''
while 循环
Python 中 while 语句的一般形式：
'''
a = 0
while a < 100:
    if a == 98:
        print(a, end="")
    else:
        print(a, end=",")
    a += 2
'''
同样要照顾缩进，注意的是，Python中不存在do..while循环
'''

'''
用while循环计算1到100总和
'''
print()
print()
Sum = 0
Count = 1
while Count <= 100:
    Sum += Count
    Count += 1
print(Sum)

'''
简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
'''
# flag = 1
# while(flag) : print('yeah!')
# print('Bye!')


'''
for语句
Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

programlanguages = ["C", "C++", "Perl", "Python"]

for x in programlanguages:
    print(x)

'''
以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
'''
sites = ["Baidu", "Google", "FaceBook", "Taobao"]
for site in sites:
    if site == "FaceBook":
        print("脸书!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

'''
range()函数
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
'''

'''
for i in range(5):
    print(i)
...
0
1
2
3
4
'''

'''
可以使用range指定区间的值： range(5,9) : 5, 6, 7, 8
也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'): range(0, 10, 3) :0,3,6,9
for i in range(-10, -100, -30) : -10, -40, -70
'''

'''
可以结合range()和len()函数以遍历一个序列的索引,如下所示:

'''

companies = ['Google', 'Baidu', 'Alibaba', 'Tencent', 'Twitter']
for i in range (len(companies)):
    print(i, companies[i])

'''
pass 语句
Python pass是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，如下实例
'''
# while a < 2:
#     pass      这里不加pass会报错
# s = 90

