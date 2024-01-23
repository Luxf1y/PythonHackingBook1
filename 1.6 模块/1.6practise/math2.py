import math

class maths:
    def plus(x,y):
        count=0
        for i in range(0,y):
             print("请输入x：",i)
             x=input()
             count=count+int(x)
        return count
    def minus(x,y):
        count=0
        for i in range(0,y):
            print("请输入x:",i+1)
            x=input()
            count=count-int(x)
        return count
    def cheng(x,y):
        count=0
        for i in range(0,y):
            print("请输入x:",i+1)
            x=input()
            count=count*int(x)
        return count   
    def chu(x,y):
        count=0
        for i in range(0,y):
            print("请输入x:",i+1)
            x=input()
            count=count/int(x)
        return count 