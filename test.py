cours=["pommes","bananes","lait","fromage","oeufs"]
suplementaires=input("ajouter un element à la liste: ")

if len(cours)<2:
  cours.insert(len(cours),suplementaires)
  print(len(cours))
  print(cours)
else:
    print("la liste est pleine")
      





# print("bismi lah")
# list=[35,0,25,55,1]

# list.sort()#mettre list en ordre croissant
# print(list)

# list.remove(55)#supprimer 55 de la list
# print(list)

# list.append(100)#ajouter 100 à la list
# print(list)

# list.insert(0, 53)#ajouter 50 à la position 
# print(list)