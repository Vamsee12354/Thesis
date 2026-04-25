class homework:
    def __init__(self, maths, chem, phy):
        self.maths = maths
        self.chem = chem
        self.phy = phy

    def checkhomework(self):
        if self.maths and self.chem and self.phy:
            print("All homework is completed!")
        else:
            print(f"Maths: {self.maths}, Chem: {self.chem}, Phy: {self.phy}")
            print("Some homework is not done!")


# Ask the user for input (like cin>> in C++)
maths_done = input("Did you complete Maths homework? (yes/no): ").strip().lower() == "yes"
chem_done  = input("Did you complete Chem homework? (yes/no): ").strip().lower() == "yes"
phy_done   = input("Did you complete Phy homework? (yes/no): ").strip().lower() == "yes"

avashkar = homework(maths_done, chem_done, phy_done)
avashkar.checkhomework()