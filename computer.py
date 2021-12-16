class computer(object):
    def __init__(self,Name,RAM,Storage,SSD,Processor,Price):
        self.Name=Name
        self.RAM=RAM
        self.Storage=Storage
        self.SSD=SSD
        self.Processor=Processor
        self.Price=Price

    def Laptop(self):
        print(f"Name:{self.Name}\nRAM:{self.RAM}\nStorage:{self.Storage}\nSSD:{self.SSD}\nProcessor:{self.Processor}\nPrice:{self.Price}")
class Allocation(computer):
    def __init__(self,user,department,employeeNO,Name,RAM,Storage,SSD,Processor,Price):
        super().__init__(Name,RAM,Storage,SSD,Processor,Price)
        self.user=user
        self.department=department
        self.employeeNO=employeeNO
    def Display(self):
        print(f"Allocated to:{self.user}\nDepartment:{self.department}\nemployeeNO:{self.employeeNO}")

M1=Allocation("Mise","IT","234Y56T","Toshiba","16gb","1TB","2TB","3.2Ghtz","$1076")
M1.Display()
M1.Laptop()




