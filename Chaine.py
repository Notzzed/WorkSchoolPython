chaine1 = input("rentrez la première chaine de caractères")
chaine2 = input("rentrez la deuxième chaine de caractères")

if (len(chaine1)>len(chaine2)):
    print("la chaine la plus longue est", chaine1,"et contient",len(chaine1), "caractères")
else:
    print("la chaine la plus longue est", chaine2,"et contient",len(chaine2), "caractères")
