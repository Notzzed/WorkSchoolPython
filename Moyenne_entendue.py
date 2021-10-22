NombreValeurs=int(input("Vous souhaitez faire la moyenne de combien de valeurs ? "))
Somme=0.0
for i in range(NombreValeurs):
    print("Valeur n°",i+1," :")
    Valeur=float(input())
    Somme=Somme+Valeur
Moyenne=Somme/NombreValeurs
MoyenneArrondie=round(Moyenne,2)
print("La moyenne est : ",MoyenneArrondie)
