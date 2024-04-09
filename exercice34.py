print("Structure conditionnelle à choix multiple : if ... elif ... else ...")
age = int(input("veuillez entrer Age :"))
if 6<=age<=7 :
    print("la categorie d'enfant est Poussin")
elif 8<=age<=10:
    print("la categorie d'enfant est Pupille")
elif 10<=age<=11:
    print("la categorie d'enfant est Minime")
else:
    print("la categorie d'enfant est cadet")
