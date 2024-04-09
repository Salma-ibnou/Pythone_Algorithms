print("Structure conditionnelle à choix multiple : if ... elif ... else ...")
N = int(input("veuillez entrer la valuer de nombre :"))
if N == 6:
    print("le personnage va a droite ")
elif N == 4:
    print("le personnage va a gauche ")
elif N == 8:
    print("le personnage va en haut ")
elif N == 2:
    print("le personnage va en bas")
else:
    print(" erreur de saisie , le personnage ne bouge pas ")