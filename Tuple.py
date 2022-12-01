'''
Python3 元组
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''

tup1 = ('google', 'william', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   # 不需要括号也可以
print(type(tup3))
print(type(tup1) == type(tup2) and type(tup2)== type(tup3))
emptup = ()                 # 创建空元组

# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
tupi = (50)     # int
tupt = (50,)    # tuple
print(type(tupi), type(tupt))

# 元组与字符串类似，下标索引从 0 开始，可以进行截取，组合等。

'''
访问元组
元组可以使用下标索引来访问元组中的值，如下实例:
'''
print('tup1[0]:', tup1[0])
print('tup2[1:5]:', tup2[1:5])

'''
修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
'''
tupa = (12, 34.56)
tupb = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

tupc = tupa +tupb
print(tupc)

'''
删除元组
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
'''
tup2del = ('google', 'william', 1997, 2000)
print (tup2del)
del tup2del
# print ("删除后的元组 tup : ")
# print (tup2del)
# 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
# Traceback (most recent call last):
#   File "Tuple.py", line 49, in <module>
#     print (tup2del)
# NameError: name 'tup2del' is not defined


'''
元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
Python 表达式	                    结果	                                        描述
len((1, 2, 3))	                      3	                                    计算元素个数
(1, 2, 3) + (4, 5, 6)	        (1, 2, 3, 4, 5, 6)	                            连接
('Hi!',) * 4	            ('Hi!', 'Hi!', 'Hi!', 'Hi!')	                    复制
3 in (1, 2, 3)	                    True	                                元素是否存在
for x in (1, 2, 3): 
    print (x, end=" ")	            1 2 3	                                    迭代
'''

'''
元组内置函数
Python元组包含了以下内置函数
len(tuple)          计算元组元素个数。
max(tuple)          返回元组中元素最大值。	
min(tuple)          返回元组中元素最小值。
tuple(iterable)     将可迭代系列转换为元组。	
'''
