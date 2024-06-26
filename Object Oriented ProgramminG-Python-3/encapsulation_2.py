#ENCAPSULATION

class Student:
    def __init__(self,name, roll_no, age):
        #private member
        self.name = name
        #private members to restrict access
        #avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    #Getter methods
    def get_roll_no(self):
        return self.__roll_no

    #setter method to modify data member
    #condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10,15)

#before Modify
jessa.show()
#changing roll number using setter
jessa.set_roll_no(120)

jessa.set_roll_no(25)
jessa.show()
