class Point:
    def __init__(self,x,y):
        self.x= x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)

    def __mul__(self, other):
        x = self.x*other.x
        y = self.y*other.y
        return Point(x,y)

    def __pow__(self, other):
        x = self.x**other.x
        y = self.y**other.y
        return Point(x,y)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

p1 = Point(5,4)
p2 = Point(3,2)
sub=p1-p2
mul=p1*p2
pow=p1**p2
print(sub)
print(mul)
print(pow)
