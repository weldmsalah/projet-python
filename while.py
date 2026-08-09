mot_de_passe=""
while  not mot_de_passe == "super":
    mot_de_passe=input("Entrez le mot de passe svp: ")
    if not mot_de_passe == "super":
        print("Mot de passe incorrect ")
        print("try again")
print ("Mot de passe correct")   