class Animal(object):
    def __init__(self,Type,Age):
        self.Type=Type
        self.Age=Age

    def Pony(self):
        print(f"My name is Kristabell and i am an {self.Type} breed type of pony.\nI am {self.Age}years old")

    def FoodType(self,Food):
        print(f"{self.Type}'s best foods are:\n\t{Food}")

    def AmountOfFeed(self,Amount):
        print(f"{self.Type} eats {Amount} of hay or any other feed")

class AmericanQuarterHorse(Animal):
    def __init__(self,Type,Age):
        super().__init__(Type,Age)

    def Shelter(self,Shelter):
        print(f"{self.Type} lives in:\n\t{Shelter}.")

    def LifeSpan(self,LifeSpan):
        print(f"{self.Type} lives to upto {LifeSpan}.")

    def Ridden(self,Ridden):
        print(f"{self.Type} can be ridden in {Ridden}.")

P1=AmericanQuarterHorse("American Quarter Horse",19)
P1.Pony()
P1.FoodType("Oats\n\tBarley\n\tRye")
P1.AmountOfFeed("1-1.5 pounds")
P1.Shelter("Bleak Areys\n\tMoors\n\tHarsh")
P1.LifeSpan("25-30 years")
P1.Ridden("western or English")
