print("donne moi un nombre de secondes")
sec= float(input())
sec= int(sec)
sec= str(sec)
h= h % sec//3600
h= str(h)
h= float(h)
minu= sec % 3600//60
minu= float(minu)
minsec= sec % 3600//60
minu= str(min)
minsec= str(minsec)
minu= float(minu)
print(h+"heure " minu +"min "+ minsec +"sec")
