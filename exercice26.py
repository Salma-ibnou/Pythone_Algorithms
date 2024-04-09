import math
print("Programme qui calcule et affiche le volume d'une sphère")
r= float(input("veuillez entrer la valeur de rayon :"))
volume =(4 * math.pi * ( r**3 ) ) / 3
print("le volume est:" ,format (volume,".2f"))