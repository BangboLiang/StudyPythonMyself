'''
Python3 字典
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
格式如下所示：
d = {key1 : value1, key2 : value2, key3 : value3 }
注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。
键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
'''
# 一个简单的字典实例：
sample = {'name':'lbb', 'likes': 'magic cube', 'url':'BangboLiang.github.io'}

'''
创建空字典
使用大括号 { } 创建空字典：
'''
emptyDict = {}
print(emptyDict)
print("Length:", len(emptyDict))
print(type(emptyDict))

'''
访问字典里的值
把相应的键放入到方括号中，如下实例:
'''
print(f"sample[name]:{sample['name']}")
print()

'''
修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
'''
tinydict = {'Name': 'William', 'Age': 22, 'Class': 'CS2201'}

tinydict['Age'] = 23
tinydict['School'] = 'HNU'

print (f"tinydict['Age']: {tinydict['Age']}")
print (f"tinydict['School']: {tinydict['School']}")

'''
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显式删除一个字典用del命令，如下实例：
'''
del tinydict['School']
print(tinydict)
tinydict.clear()
print(tinydict)
del tinydict

'''
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
'''
# 1.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
tinydict2 = {'Name': 'William', 'Age': 23, 'Name': 'Liang'}

print("tinydict2['Name']: ", tinydict2['Name'])

# 2.键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
# tinydict3 = {['Name']: 'William', 'Age': 23}
# print ("tinydict3['Name']: ", tinydict3['Name'])
# Traceback (most recent call last):
#   File "dictionary.py", line 62, in <module>
#     tinydict3 = {['Name']: 'William', 'Age': 23}
# TypeError: unhashable type: 'list'

'''
字典内置函数&方法
Python字典包含了以下内置函数：
len(dict)               计算字典元素个数，即键的总数。
str(dict)               输出字典，可以打印的字符串表示。
type(variable)          返回输入的变量类型，如果变量是字典就返回字典类型。

Python字典包含了以下内置方法：
dict.clear()                            删除字典内所有元素
dict.copy()                             返回一个字典的浅复制
dict.fromkeys()                         创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
dict.get(key, default=None)             返回指定键的值，如果键不在字典中返回 default 设置的默认值
key in dict                             如果键在字典dict里返回true，否则返回false
dict.items()                            以列表返回一个视图对象
dict.keys()                             返回一个视图对象
dict.setdefault(key, default=None)      和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict.update(dict2)                      把字典dict2的键/值对更新到dict里
dict.values()                           返回一个视图对象
pop(key[,default])                      删除字典 key（键）所对应的值，返回被删除的值。
popitem()                               返回并删除字典中的最后一对键和值。
'''
