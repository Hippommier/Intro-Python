print("En quelle année est tu né(e) ?")
date=int(input())
date= float(date)
age= 2026-date
if(age < 12) :
    print("Tu es un enfant")
if(age >= 12 and age < 17) :
    print("Tu es un ado")
else :
    print("Tu es adulte")
print("à la fin de l'année 2026 tu auras "+ str(age))