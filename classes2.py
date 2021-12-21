class Reptile(object):
    def __init__(self,name="Dolphin",age="40 years",type="orca"):
        self.name=name
        self.age=age
        self.type=type

    def Reptile_Details(self):
        print(f"{self.name}\n{self.age}\n{self.type}")

class fish(Reptile):
    def __init__(self,name="Dolphin",age="40 years",type="orca",weight="500kgs",colour="greyish",length="4.0m"):
        super().__init__(name,age,type)
        self.weight=weight
        self.colour=colour
        self.length=length

    def Details(self):
        print(f"{self.weight}\n{self.colour}\n{self.length}")

w1=fish()
w1.Reptile_Details()
w1.Details()

