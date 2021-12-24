class person(object):
    def __init__(self,Name,password):
        self.Name=Name
        self.password=password

    def personal_Details(self):
        print(f"Welcome {self.Name}\nPlease enter your password:{self.password}")

    def person_ToDo(self,ToDo):
        print(f"{self.Name} will do the following:\n\t{ToDo}")

class Student(person):
    def __init__(self,Name,password):
        super().__init__(Name,password)

    def personADMNO(self,ADMNO):
        print(f"{self.Name}'s ADMNO is {ADMNO}")

    def Institution(self,Institution):
        print(f"{self.Name} is a student at {Institution}")

    def Course(self,Course):
        print(f"{self.Name} is a {Course}")

Q1=Student("Gaciuki","4065grace")
Q1.personal_Details()
Q1.person_ToDo("Arrays\n\tListing\n\tClasses")
Q1.personADMNO(7806)
Q1.Institution("Taita Taveta Uni")
Q1.Course("Software Eng")