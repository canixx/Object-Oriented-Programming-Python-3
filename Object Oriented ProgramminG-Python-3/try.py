class First():
    def sum1(self, a, b):
        c= a+b
        return c
class Second():
    def sub1(self, x, y):
        z=x-y
        return z
class Third(First,Second):
    pass
obj1=Third()
print(obj1.sum1(20,25))
print(obj1.sub1(50,25))