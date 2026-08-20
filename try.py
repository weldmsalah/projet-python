import random
x=random.randint(1,10)
M=0
c=0

while not int(x)==int(M) and c<14:
    M=int(input("un chiffre [1,10] "))
    print(x)
    c+=1
    if int(x)>int(M):
        print("il faut plus") 
    elif int(x)<int(M):
        print("il faut moins") 
    else:
        print(f'bravo le N°secret est {x} et vous avez donner {M} ')       