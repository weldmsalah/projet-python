
compte=[2,4,6,8]                        
plus=input("ajouter un element à la liste:  ")          # input
compte.append(int(plus))                                # liste.append(element)
print("ajoute le dernier element "+str(compte))                          
if len(compte)<8:                                       # len(liste)                            
  compte.insert(len(compte),int(plus)+1)                # liste.insert(position,element)       
  print("a l'indice placer element+1"+str(compte))     
  compte.sort() 
  print (compte)
  compte.reverse()                                        #liste.sort() metre en ordre croissant 
  print(compte) 
  compte.remove(int(plus)) 
  print(compte)                                
   
else:
    

    print("la liste est pleine intervention depuit GH")
    print ("intervention depuit le local")
        









# list.remove(55)#supprimer 55 de la list
# print(list)

# list.append(100)#ajouter 100 à la list
# print(list)

# list.insert(0, 53)#ajouter 50 à la position 
# print(list)
