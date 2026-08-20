"""intervention input pour modifier target( augmentation de salaire totale )
"""
print("*********"*6)
target=int(input("saisissez votre augmentation de salaire ici :"))
print("*********")
class employee:
    def __init__(self,name,age,gender,salary):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary

    def totalsalary(self,target):       # nouvelle METHODE
        totalsalary=self.salary+target
        print("salaire actuelle est ",totalsalary) # important ici la vergule ,

    def printall(self):     
        print(f'Monsieur {self.name} est ageé de {self.age} et de genre {self.gender} son salaire apres augmentation est {self.salary} $')

                            # cree un objet obigatoirement en dehors de la class 
em1=employee("said",23,"mal",1500)    #on a donner les parametre 
em2=employee("ahmed",33,"mal",100)
print("*"*25)
print(em1.printall())
print(em2.totalsalary(target))

