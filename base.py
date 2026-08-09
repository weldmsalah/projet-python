nom=input("entrer votre nom:  ")
age=input("entrer votre age:  ")
try:
    age=int(age)
except:
    print("vous devez entrer un nombre pour l'age")   


else:
    print("vous etes "+ nom +" vous avez "+str(age)+ " ans")