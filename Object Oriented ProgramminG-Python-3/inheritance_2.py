#INHERITANCE
class a:
    def m(self):
        print ('a1')

class b(a):
    def m(self):
        print('b1')

class c(a):
     def m(self):
         print('c1')

class d(b,c):
    def m(self):
        print('d1')
        b.m(self)
        c.m(self)
        a.m(self)
obj1=d()
obj1.m()