from abc import *

class Myclass(ABC):
    @abstractmethod
    def putdata(self,text):
        pass

    @abstractmethod
    def disconnect(self):
        pass

#Sub-Class:1
class IBM (Myclass):
    def putdata(self,text):
        print(text)

    def disconnect(self):
        print("Disconnecting from IBM printer...")

#Sub-Class:2
class Epson(Myclass):
    def putdata(self,text):
        print(text)
    def disconnect(self):
        print("Disconnecting from Epson printer...")


#Define Printer
class Printer:

    str = input("Enter the printer name:")

    #Convert the string into the class name
    classname = globals() [str]

    #Create an object
    x= classname()

    #Call methodsx
    x.putdata("Sending to printer")
    x.disconnect()
