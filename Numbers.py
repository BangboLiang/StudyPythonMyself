'''
Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
'''

number = 0xa0F #0x表示十六进制
print(number)

number = 0o37 # 0o表示八进制
print(number)

number = 0b1100 # 0b表示二进制
print(number)

'''
数字类型转换
int(x) 将x转换为一个整数。
float(x) 将x转换到一个浮点数。
complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
'''
x = 1
y = 45
j = complex(x,y)
print(type(j))
print(j)

'''
常用的数学函数
abs(x)
ceil(x)
floor(x)
cmp(x,y)            如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
exp(x)
log(x)              如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)
max(x1, x2,...)     返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)     返回给定参数的最小值，参数可以为序列。
modf(x)	            返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	        x**y 运算后的值。
round(x n)	        返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
sqrt(x)	            返回数字x的平方根。
'''

'''
随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
Python包含以下常用随机数函数：
choice(seq)	                        从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange (start, stop, step)	    从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	                        随机生成下一个实数，它在[0,1)范围内。
seed(x)	                            改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	                    将序列的所有元素随机排序
uniform(x, y)	                    随机生成下一个实数，它在[x,y]范围内。
'''


'''
三角函数
Python包括以下三角函数：
acos(x)	    返回x的反余弦弧度值。
asin(x)	    返回x的反正弦弧度值。
atan(x)	    返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	    返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	    返回的x弧度的正弦值。
tan(x)	    返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''

'''
数学常量
pi	        数学常量 pi（圆周率，一般以π来表示）
e	        数学常量 e，e即自然常数（自然常数）。
'''