# 打印一个斐波那契数列
a, b = 0, 1
while b < 100:
    if b == 89:
        print(b, end="")
    else:
        print(b, end=",")
    a, b = b, a+b
