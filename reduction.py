# système qui demande l'âge en fonction de l'âge donné une réduction est donné

age = int(input("Entrez votre âge pour recevoir votre réduction ! "))
if age <= 10:
    print("Vous avez 50% de réduction pour les - de 10 ans")
# si vous entrez un nombre qui est moins de 10 vous aurez 50% de réduction
if 10 < age < 18 :
    print("Vous avez 30% de réduction pour les 10/18 ans")
# si vous entrez un nombre entre 10 et 18 vous aurez 30% de réduction
if age >= 60:
    print("Vous avez 20% de réduction pour les + de 60 ans")
# si vous entrez un nombre qui est supérieur à 60 vous avez 20% de réduction
