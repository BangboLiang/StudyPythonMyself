'''
Python3 字符串
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
创建字符串很简单，只要为变量分配一个值即可。
'''
str1 = 'Hello, world!'
str2 = 'William'

'''
Python 字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
'''
print("我叫 %s 今年 %d 岁!" % ('小明', 10))

'''
python字符串格式化符号:
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
'''

'''
f-string
f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来
它会将变量或表达式计算后的值替换进去，实例如下：
'''

name = 'Runoob'
print(f'Hello {name}')
print(f'{1+2}')
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

'''
Unicode 字符串
在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。
使用的语法是在字符串前面加上前缀 u。
在Python3中，所有的字符串都是Unicode字符串。
'''

'''
Python 的字符串内建函数
详见 https://www.runoob.com/python3/python3-string.html
''' 