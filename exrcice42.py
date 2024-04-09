print("Programme qui vérifie si une année est bissextile ou non")
annee = int(input("veuillez entrer la valuer d'annee :"))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("L'année", annee ,"est bissextile.")
else:
    print("L'année", annee , "n'est pas bissextile.")