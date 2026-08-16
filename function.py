#aprtir d une liste sortir le nom et l age pour chaque personne
list=[["mohamed",25,"ingenieur"],#linge 0
      ["said",33,"technicien"],#ligne 1
      ["karim",21,"ouvrier"],# ligne 2
      ["malik",44,"supervisor"]]#ligne 3
ligne=int(input("ligne  "))
nom=int(input("nom sur la liste (N°) "))
age=int(input("donner votre age (N°) "))

print(f'bonjour Monsieur {list[ligne][nom]} votre age est :{list[ligne][age]} ans')
print(f'bonjour Monsieur {list[ligne][0]} votre age est :{list[ligne][1]} ans')
