print("Bienvenue dans le programme pour calculer le prix de ton billet de cinéma")
print ("Indique ton âge ")
age= int(input())
price=int(price)
price=14.10
price=float(price)
price=str(price)
print("Est ce que ton film est en IMAX ? Indique Oui ou Non")
imax= bool(input())
imax=int(imax)
print("Y'a-t-il un réduction sur ton billet ? Indique Oui ou Non")
red= bool(input())
red= int(red)
if (age<=17 and age>=65) :
    prix= price-4
if (imax==True) :
    prix=price+4.40
if (red==True) :
    price=price//2
print("Le prix du ticket est "+ price)
