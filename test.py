class homework:
    def __init__(self, maths,chem,phy):
            self.maths=maths
            self.chem=chem
            self.phy=phy
    def checkhomework(self):
        if(self.maths==True & self.chem==True & self.phy==True ): 
            print(f"The person {self} has completed Maths = {self.maths} in his homework")


avashkar=homework(True,True,True)


avashkar.checkhomework()