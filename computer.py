#create computer Class
#display name,Ram,storage,ssd,processor
class computer(object):
    def __init__(self,Name,RAM,Storage,SSD,Processor):
        self.Name=Name
        self.RAM=RAM
        self.Storage=Storage
        self.SSD=SSD
        self.Processor=Processor

    def Laptop(self):
        print(f"Name:{self.Name}\nRAM:{self.RAM}\nStorage:{self.Storage}\nSSD:{self.SSD}\nProcessor:{self.Processor}")

f2=computer("Toshiba","16gb","1TB","2TB","3.2Ghtz")
f2.Laptop()