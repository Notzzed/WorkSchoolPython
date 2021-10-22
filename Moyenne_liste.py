
liste=[]
n=0.0

while n!= "fin":
    n=input("rentrez des valeurs ou taper fin")
    if n!= "fin":
     n = float(n)
     liste.append(n)

moyenne=sum(liste)/len(liste)
print(liste)
print(moyenne)
