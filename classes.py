class Names:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def output(self):
        # print("My name is",self.name,"I am ",self.age,"years old.")
        print(f"My name is {self.name}, I am {self.age} years old.")

grace=Names("Grace",20)
grace.output()

irene=Names("Irene",20)
irene.output()

john=Names("John Doe",32)
john.output()

#Create a class
# argumentes/parameter num1,num2
# adds them


class num:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        sum=self.num1+self.num2
        print(f"{self.num1}+{self.num2}={sum}")

p9 =num(45,78)
p9.add()

j7=num(45,670)
j7.add()

f3=num(4567,9086)
f3.add()


class subtraction:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def sub(self):
        sub=self.n1-self.n2
        print(f"{self.n1} - {self.n2} = {sub}")

d1=subtraction(3456,2314)
d1.sub()


#Create student class
#Parameters Id number,reg_number,name,course
#Display print the details
class student_details:
    def __init__(self,name,ID_Number,RegNO):
        self.name=name
        self.ID_Number=ID_Number
        self.RegNO=RegNO

    def Display(self):
        print(f"my Name is {self.name},this is my ID.NO:{self.ID_Number} and my RegNO:{self.RegNO}")

g1=student_details("Day",2345667,"TU01-SC211-1376/2016")
g1.Display()























