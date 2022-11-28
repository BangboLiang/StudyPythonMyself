# 缩进

if True:
    print('缩进后的print')
else:
    print('你应该看不见我')

# 换行符
one = 1
two = 2
three = 3

total_num = one + \
            two + \
            three
print('total_num='+str(total_num))

# 注意：在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \


'''
数字(Number)类型
python中数字有四种类型：整数、布尔型、浮点数和复数。

int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

'''
字符串(String)
Python 中单引号 ' 和双引号 " 使用完全相同。
使用三引号(\''' or """)可以指定一个多行字符串。
转义符 \
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''

word = 'WORD'
sentence = 'This is just a sentence'
phrase = """This is a phrase,
It includes several lines."""
print(word)
print(sentence)
print(phrase)

# 字符串切片 [start:end:step]

Z2N = '0123456789'

print(Z2N[0:1])
print(Z2N[0:])
print(Z2N[0::2])
print(Z2N[::-1]) # 倒序

# 这里的 r 指 raw，即 raw string，会自动将反斜杠转义，转义字符直接输入，例如'\n'不会换行：
print(r"\n")

'''
用户输入: input()函数
'''

# a = input('Please input an integer:')

# print('You entered ' + str(a))

'''
Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割，以下是一个简单的实例：
'''

a = 12345; b=12233; print(a+b)


'''
print 输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
'''

print('This is a sentence without end line.', end="")
print('Yeah')


'''
mport 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
'''