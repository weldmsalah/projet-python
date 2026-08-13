import random
x=random.randint(1,10)
print("  le rendu du random  x  : "+ str(x ))
ton_age=str(input("donne une valeur entre 1 et 10: "))
if ton_age==str(x):
    print("bravo vous avez trouvez la bonne reponse")    
else:
    print("(else)ce n est pas la bonne reponse ") 
    m=4
    while not ton_age==str(x) and m > 0 :
                ton_age=str(input("W , donne une nouvelle valeur "))
                m-=1
                try:
                    int(ton_age)==x
                
                    if int(ton_age) >x:
                          print("sup")
                    elif int(ton_age)<x:
                          print("inf")         
                except:
                    print("une valeurnumrique  ?  ")
print("fin du Prog")        