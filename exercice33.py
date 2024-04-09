print("Structure conditionnelle à choix multiple : if ... elif ... else ...")
nbr = int(input("veuillez entrer les nombres de photocopies :"))
if nbr<10:
    f = nbr * 0.30
elif nbr<30 :
    f = 10 * 0.30 + (nbr -10)*0.25
else:
    f = 10 * 0.30 +20*0.25 + (nbr -30)*0.2
print("le montant de facture a payer est :",f , "DH")
 
      