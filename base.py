nom=input("entrer votre nom:  ")
age=input("entrer votre age:  ")
try:
    age=int(age)
    nom=str(nom)  
except:
    print("vous devez entrer un nombre pour l'age")
    print("vous devez entrer un nom valide")   
else:
    print("vous etes "+ nom +" vous avez "+str(age)+ " ans")
    