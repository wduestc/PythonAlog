# coding:utf-8
###############################
# 函数: 求解平方根
# 算法设计: 牛顿迭代法
# 相关数学知识:1.切线方程 2.求导
# 参考的链接:http://blog.csdn.net/young_gy/article/details/45766433
###############################

#求解平方根
def sqrt(x):
    y = 1.0
    while abs(y * y - x) > 1e-6:
        y = (y + x/y) / 2
        #print y
    return y
#求解立方根
def trip(x):
    y = 3.0
    while abs(y * y * y - x) > 1e-10:
        y = (y - y*(1-x/(y*y*y))/3)
    return y


print sqrt(4)
print trip(27)
