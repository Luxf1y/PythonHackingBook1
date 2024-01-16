import math

x=5.3
y=-5.3
z=5
x1=math.ceil(x) #ceil(x): 返回大于或等于x的最小整数
x2=math.floor(x) #floor(x): 返回小于或等于x的最大整数
y1=math.fabs(y) #fabs(x): 返回x的绝对值。
z1=math.factorial(z) #factorial(x): 返回x的阶乘。#必须是整数
xy1=math.hypot(x,y)#hypot(x, y): 返回直角三角形的斜边长度，即以x和y为直角边的三角形的斜边长度。
xy2=math.pow(x,y)#pow(x, y): 返回x的y次幂。
x3=math.sqrt(x)#sqrt(x): 返回x的平方根。
x4=math.log(x) #log(x): 返回x的自然对数。
x5=math.log10(x) #log10(x): 返回x的以10为底的对数.
x6=math.trunc(x) #trunc(x): 返回x的截断值，即去除小数部分的整数。
x7=math.isnan(x)#isnan(x): 检查x是否为NaN（Not a Number）。
pi=math.degrees(math.pi/2)#degrees(x): 将x从弧度转换为角度。
pi2=math.radians(180)#radians(x): 将x从角度转换为弧度。

print("x1="+str(x1))
print("x2="+str(x2))
print("y1="+str(y1))
print("z1="+str(z1))
print("xy1="+str(xy1))
print("xy2="+str(xy2))
print("x3="+str(x3))
print("x4="+str(x4))
print("x5="+str(x5))
print("x6="+str(x6))
print("x7="+str(x7))
print("pi="+str(pi))
print("pi2="+str(pi2))
