import random

class Parent:
    def __init__(self, role):
        self.role = role
        self.blood_type = input(f"Enter the {self.role}'s blood type : ").upper()

class Offspring(Parent):
    def __init__(self):
        self.father = Parent('father')
        self.mother = Parent('mother')

    def determine_blood_type(self):
        alleles = list(self.father.blood_type + self.mother.blood_type)
        
        offspring_allele = "".join(random.sample(alleles, 2))
        
        print(f"Offspring's allele  : {offspring_allele}")
        
        blood_type_dict = {
            "AA" : "A",
            "AO" : "A",
            "AB" : "AB",
            "BB" : "B",
            "BO" : "B",
            "OO" : "O",
            "OA" : "A",
            "BA" : "AB",
            "OB" : "B",
            "AO" : "A"
        }
        
        for allele, blood_type in blood_type_dict.items():
            if offspring_allele == allele:
                print(f"Offspring's Blood Type   : {blood_type}")

offspring = Offspring()
offspring.determine_blood_type()
