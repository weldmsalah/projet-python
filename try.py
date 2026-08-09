ton_age=0
while ton_age==0:
    an=input("une valeure d age ")
    try:
        ton_age=int(an)+1
        print(ton_age)
    except:
        print("une valeurnumrique  ?  ")
print("fin")        