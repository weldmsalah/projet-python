loto= [25,14,10,33]
m=globals=1


match loto:
    case  [250,140,100,330]:                 #filter loto 
        print("premiere case match ok")
        print(str(loto)+" complet")
        print("exucution du reste du prog")
        m+=1
        print(m)
    case [25,14,n1,n2]:
        print("deusieme propo")
        m+=5
        print(m)
    case _:
        print("dans tout les cas")
        loto[0]=5
        print(f'varible globale {m}')  
        print(loto)   #a poursuivre append/remov/..         