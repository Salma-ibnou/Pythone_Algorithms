print(" Programme qui calcule et affiche la moyenne et la mention des notes")
N1 = int(input("veuillez entrer la note 1 :"))
N2 = int(input("veuillez entrer la note 2 :"))
N3 = int(input("veuillez entrer la note 3 :"))
Moy = ( N1 + N2 + N3)/3
print("la moyenne de l'etudiant est :",format(Moy,".2f"))

if Moy>=16 :
    print("la moyenne de l'etudiant est :tres bien")
elif 14<=Moy<=16:
    print("la moyenne de l'etudiant est : bien")

elif 12<=Moy<=14:
    print("la moyenne de l'etudiant est : assez bien")

elif 10<=Moy<=12:
    print("la moyenne de l'etudiant est : passable")
else:
    print("la moyenne de l'etudiant est : insuffisant")