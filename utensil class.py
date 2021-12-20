#name,type,size,price
#colour,made,

class utensils_details(object):
    def __init__(self,name,type,price,size):
       self.name=name
       self.type=type
       self.price=price
       self.size=size

    def utensils(self):
        print(f"{self.name}\n{self.type}\n{self.price}\n{self.size}")

class description(utensils_details):
    def __init__(self,name,type,price,size,colour,made):
        super().__init__(name,type,price,size)
        self.colour=colour
        self.made=made

    def output(self):
         print(f"{self.colour}\n{self.made}")

c1=description("cup","plastic","$100","small","pink","china")
c1.utensils()
c1.output()

