print("programme d'afficher l'etat d'eau ")
T=int(input("veuillez entrer la valeur de la temperateur de l'eau :"))
if T<100 and T>0 :
    print("l'etat de l'eau est liquide")
else:
    if T>= 100:
        print("l'etat de l'eau est vapeur")
    else :
        print("l'etat de l'eau est glace")
