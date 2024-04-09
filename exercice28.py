print(" Programme qui convertit la durée en heures, minutes et secondes ")
T =  int(input("veuillez entrer la duree en seconde :"))
H = T // 3600
M = (T % 3600) // 60
S = (T % 3600) % 60
print(H,"H:",M,"M:",S,"S")