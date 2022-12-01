'''
Python3 条件控制
Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
'''

var1 = 100
if var1:
    print('1 - if 表达式条件为 TRUE')
    print('var1 equals', var1)

var2 = 0
if var2:
    print('2 - if 表达式条件为 TRUE')
    print('var2 equals', var2)
print('Good Bye!')

'''
小程序：判断狗子的年龄
'''
age = int(input('请输入小狗的年龄:'))
print('--------------------------容我三思--------------------------')
if age <= 0:
    print('你在逗我吧？')
elif age == 1:
    print('相当于14岁的人')
elif age == 2:
    print('相当于22岁的人')
else:
    human = 22 + (age - 2) * 5
    print(f'相当于{human}岁的人')
input('按下enter键退出')

'''
if常用的操作运算符
< <= > >= == !=
'''

'''
if可以嵌套
'''
print()
print()
print('此小程序用来判断输入的数字是否能被3和2整除')
num = int(input('请输入想要检测的数字:'))
if num % 2 == 0:
    if num % 3 == 0:
        print('可以同时被2和3整除')
    else:
        print('只能被2整除')
else:
    if num % 3 == 0:
        print('只能被3整除')
    else:
        print('不能被2和3任意一个数字整除')
'''
match...case
Python 3.10 增加了 match...case 的条件判断，不需要再使用一连串的 if-else 来判断了。
类似于C\C++的switch...case
'''