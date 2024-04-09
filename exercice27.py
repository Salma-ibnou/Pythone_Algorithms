print("Programme qui échange le contenu des deux variables")
A = int(input("veuillez entrer la valeur de A :"))
B = int(input("veuillez entrer la valeur de B :"))
#methode 1
#C = A
#A = B
#B = C

#methode 2
A,B = B,A
print("la nouvelle valeur de A est :",A)
print("la nouvelle valeur de B est :",B)