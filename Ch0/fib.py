# coding:utf-8


def fib1(n):
    if n < 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f1+f2
    return f2

print fib1(3)
print fib2(3)



