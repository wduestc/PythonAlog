# coding:gb18030
def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x/y) / 2
        #print y
    return y


print sqrt(1)
