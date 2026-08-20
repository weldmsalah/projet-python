class fruit:
    def __init__(self,saison,prix,couleur,taille,):
        self.saison=saison
        self.prix=prix
        self.couleur=couleur
        self.taille=taille
    def Augmentation(self,valeur):
        augmenter=self.taille+valeur
        reduction=(self.prix)*valeur/3
        return augmenter     
pomme=fruit("juillet",2,"rouge",0.30) 
.+

banane=fruit("mars",1.5,"jaune",20) 
#print("les meilleur pommes sont en ",pomme.saison) 
#print(banane.couleur,"est la couleur des banane")
print("valeur  des pommes ",pomme.Augmentation(0.5)) 
   
   
       