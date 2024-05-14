class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print('Person Name: %s'%(self.name))
        print('Person age:%s'%(self.age))

class Employee(Person):
    def __init__(self,name,age,company,salary):
        self.company = company
        self.salary = salary
        super(Employee,self).__init__(name,age)

    def __repr__(self):
        return str(self.name + self.age + self.company + self.salary)

    def showme(self):
        Person.show(self)
        print('Company Name:%s'%(self.company))
        print('Employe Salary per Annum:%s'%(self.salary))
        print('\n')

empdict = {'guido':['45','PYTHON','500000'],'van':['25','JYTHON','200000'],'rossum':['35','ABC','400000']}
for key,value in empdict.items():
    print(key,value)


emp = Employee(key,value[0],value[1],value[2])
emp.showme()
print(emp.__repr__())
