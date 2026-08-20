

class Comedian:
    def __init__(self,role,force,vie):
        self.role=role       
        self.force=force
        self.vie=vie
     
        

    def Excution(self):
        print(f'  le role principale :{self.role} \n  la reserve de force de frappe ( {self.force} )  \n nombre de coeur restant {self.vie}  ')

    def Recherche_caractere(self):
        if int(self.vie) >  0 :
            print(f"continue le jeux,vous avez encore {self.vie} vie ")
        else:
            print("vous n 'avez plus de vie")
        
tom=Comedian("bob l eponge",77,1)
gan=Comedian("rascale",23,"9") 

print("*"*77)
tom.Recherche_caractere()
print("*"*77)
tom.Excution()
