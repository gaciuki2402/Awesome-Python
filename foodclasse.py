class food(object):
    def __init__(self,starch,sugars,cellulose):
        self.starch=starch
        self.sugars=sugars
        self.cellulose=cellulose

    def foodtypes(self):
         print(f"starch:{self.starch}\nsugars:{self.sugars}\ncellulose:{self.cellulose}")

class Daily_Requirement(food):
    def __init__(self,starch,sugars,cellulose,children,adolescents,men,women):
        super().__init__(starch,sugars,cellulose)
        self.children=children
        self.adolescents=adolescents
        self.men=men
        self.women=women

    def Requirement_of_different_groups(self):
        print(f"children:{self.children}\nadolescent:{self.adolescents}\nmen:{self.men}\nwomen:{self.women}")

s3=Daily_Requirement("cereals and tubers","white sugar and glucose","indegistible","50grams","300grams","400-700grams","300-500grams")
s3.foodtypes()
s3.Requirement_of_different_groups()

























