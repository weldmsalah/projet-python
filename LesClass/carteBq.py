apport=int(input("la valeure de votre versement est : "))
prendre=int(input("la valeure de votre retrait est : "))
class GetionCptB:
    def __init__(self,nCompte,nomClien,soldeCompte):
        self.nCompte=nCompte
        self.nomClien=nomClien
        self.soldeCompte=soldeCompte
    def versement(self,apport):
        self.soldeCompte+=apport
    def retrait(self,prendre):
        if (self.soldeCompte)>prendre:
            self.soldeCompte-=prendre
        else:
            print("retrait impossible \n votre solde est insufisant!")       
    def affichageinfo(self):    
        print(f'clien Monsieur :{self.nomClien} \n Numero de Compte : {self.nCompte} \n votre solde a ce jour : {self.soldeCompte} euros ')

imane=GetionCptB(2306,"MOHAMED SALAH",700) 
imane.versement(apport)
imane.retrait(prendre)
imane.affichageinfo()

