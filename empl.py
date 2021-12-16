#Employee Details= age,name,phone
#Employee Salary -->Basic salary,Tax,commission,salary

class EmpDetails(object):
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone

    def OutputEmpDetails(self):
        # print("Name: {}\nAge: {}\nPhone: {}".format(self.name,self.age,self.phone))#F string
        print(f"Name: {self.name}\nAge:{self.age}\nPhone: {self.phone}")
yuuhh=EmpDetails("Grace",20,"0712345678")
yuuhh.OutputEmpDetails()


