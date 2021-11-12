devise = input("indiquer la devise :")
montant = int(input("indiquer le montant :"))

if devise == 'euro':
    montant_dollar = montant*1.14
    print("le montant en dollar vaut", montant_dollar)
elif devise == 'dollar':
    montant_euro = montant/1.14
    print("le montant en euro vaut", montant_euro)
