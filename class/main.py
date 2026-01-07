#create students class

class Student:
    university="VBIT"#class/static var
    def __init__(self,name,age):#instance method
        self.name=name#instance var
        self.age=age


    def getName(self):
        print(self.name)


    def add(obj,num1,num2):
        print(num1+num2)
# init is a special method which is going to called when ever an object is created


obj1=Student("mahender",25)# create a new object
obj1.getName()
obj1.add(10,20)
