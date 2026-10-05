print("Insère un premier nombre entier ")
nb1= int(input())
nb1= float(nb1)
print("Insère un deuxième nombre entier ")
nb2= int(input())
nb2= float(nb2)
prod= nb1*nb2
add= nb1+nb2
add= float(add)
if (prod <= 1000) :
    print("Le résultat de " + str(nb1) +"*"+ str(nb2)+ " est "+ str(prod))
else :
    print("La somme de "+str(nb1)+" et "+str(nb2)+ " est "+ str(add))
