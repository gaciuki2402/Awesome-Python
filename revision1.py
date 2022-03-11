class Vehicle_details():
    def __init__(self,Name,Colour,Brand,No_Plate):
        self.Name=Name
        self.Colour=Colour
        self.Brand=Brand
        self.No_Plate=No_Plate
    def Details_Output(self):
        print(f"Name:{self.Name}\nNo_Plate:{self.No_Plate}\nBrand:{self.Brand}\nColour:{self.Colour}")

class Dealer_Details(Vehicle_details):
    def __init__(self,Name,Colour,Brand,No_Plate,Location,Owner,Date_of_Manufacture):
        super().__init__(Name,Colour,Brand,No_Plate)
        self.Location=Location
        self.Owner=Owner
        self.Date_of_Manufacture=Date_of_Manufacture

    def Output(self):
        print(f"Location:{self.Location}\nOwner:{self.Owner}\nDate:{self.Date_of_Manufacture}")

d1=Dealer_Details("Lamborghini","Grey","Tesla","wkei483","Nairobi_Kenya","GaciukiGrace","22/02/2021")
d1.Details_Output()
d1.Output()
print("x"*67)

class Beverages():
    def __init__(self,Name,Price):
        self.Name=Name
        self.Price=Price

    def Output(self):
        print(f"{self.Name} has a price of {self.Price} per cup.")
    def Coffee(self,name,quality):
        print(f"{name} is of {quality} quality compared to other types of coffee.")
    def Juice(self,quantity):
        print(f"The price of juice is {self.Price} per {quantity} . It's content are only fruits.")

class Customers(Beverages):
    def __init__(self,Name,Price,delivery_fee,location):
        super().__init__(Name,Price)
        self.delivery_fee=delivery_fee
        self.location=location
    def customer(self,person):
        print(f"My name is {person} and i would like you to deliver for me {self.Name}. Am located at {self.location}.")
    def dealer(self,discount):
        print(f"Our delivery fee is {self.delivery_fee} but we offer discount of {discount} only to electronics goods.")

c1=Customers("Tea","50ksh",500,"Nakuru")
c1.Output()
c1.Coffee("Arabica coffee","High")
c1.Juice("litre")
c1.customer("Kinyanjui")
c1.dealer(200)
print("x"*67)

class Babies():
    def __init__(self,Name,Weight_in_kgs,age_in_months):
        self.Name=Name
        self.Weight_in_kgs=Weight_in_kgs
        self.age_in_months=age_in_months
    def Baby(self):
        print(f"My name is {self.Name} and i have {self.Weight_in_kgs} kilograms.I am {self.age_in_months} months old.")

class Baby_Details(Babies):
    def __init__(self,Name,Weight_in_kgs,age_in_months,parent_name,hospital_born):
        super().__init__(Name,Weight_in_kgs,age_in_months)
        self.parent_name=parent_name
        self.hospital_born=hospital_born
    def B_a_b_y(self,DOB):
        print(f"{self.Name} was born on {DOB}.Her mother's name is {self.parent_name}.she's {self.age_in_months} months old.")

    def kid(self,location):
        print(f"{self.Name} was born at {self.hospital_born} which is located at {location}")


b1=Baby_Details("Salma",0.6,6,"Joyce","St Basil")
b1.Baby()
b1.B_a_b_y("24th Feb 2020")
b1.kid("Warsaw_Poland")





