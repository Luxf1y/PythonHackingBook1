class animal():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def run(self):
        print("%d 的 %d 在 run" % (self.name,self.color))
    def eat(self)
        print("%d 的 %d 在 eat" % (self.name,self.color))

class tiger(animal):
    def __init__(self,name,color,xingge):
        animal.__init__(self,name,color)
        self.xingge=xingge
    def run(self):   
        print('%s的'% self.xingge)
        animal.run(self)
    def eat(self):   
        print('%s的'% self.xingge)
        animal.eat(self)

a=tiger('tiger','white','hungry')
