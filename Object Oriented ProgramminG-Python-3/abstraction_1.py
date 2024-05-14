from abc import*
class Myclass(ABC):
    @abstractmethod
    def connect (self):
        pass
    @abstractmethod
    def disconnect (self):
        pass


#Sub-Class:1

class Oracle(Myclass):
    def connect(self):
        print("*Connecting to oracle database...")

    def disconnect(self):
        print("Disconnecting from oracle database...")


#Sub-Class:2

class Sybase(Myclass):
    def connect(self):
        print("Connecting to sybase database...")

    def disconnect(self):
        print("Disconnecting from sybase database...")


#Define Database

class Database:

    str = input("Enter the database name: ")

    #Convert the string into the class name
    classname = globals() [str]

    #create an object
    x = classname()

    #call methods
    x.connect()
    x.disconnect()
