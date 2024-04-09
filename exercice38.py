print(" Programme qui calcule le prix TTC d^un produit")
PHT = float(input("veuillez entrer le prix hors taxe de produit : "))
Cat = input("veuillez entrer la categorie de produit : ")
if  Cat == "A" :
    print("le prix TTC de produits est : " , PHT+PHT*0.07)
elif   Cat == "B":
    print("le prix TTC de produits est : " , PHT+PHT*0.02)

elif   Cat == "C":
    print("le prix TTC de produits est : " , PHT+PHT*0.25)
else:
    print("la categorie n'existe pas ")
