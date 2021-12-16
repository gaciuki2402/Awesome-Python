class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def DogName(self):
        print(f"i am {self.name},and i am {self.age} years old.")

    def FoodType(self,food):
        print(f"{self.name} eats {food}")
# if __name__=="__main__":
#     d1=Dog("Scooby",3)
#     d1.DogName()
#     d1.FoodType("Fish")

class JackRusselTerrier(Dog):
    def __init__(self,name,age):
        super().__init__(name,age) #Inherit the instance of dog class

    def DogColour(self,colour):
        print(f"{self.name} is {colour} in colour.")

    def Sound(self,sound):
        print(f"{self.name} {sound}'s")
        
if __name__=="__main__":
    j1 = JackRusselTerrier("Jack",4)
    j1.DogName()
    j1.FoodType("Meat")
    j1.DogColour("Brown")
    j1.Sound("Wuuf")