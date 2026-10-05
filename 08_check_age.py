print("Quel âge as tu ?")
age=(input())
age= float(age)
if(age < 12) :
    print("Tu es un enfant")
if(age >= 12 and age < 17) :
    print("Tu es un ado")
else :
    print("Tu es adulte")