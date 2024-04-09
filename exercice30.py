import math
print("Programme qui calcule la résistance en série et en parallèle")
R1 = float(input("veuillez entrer la valuer de R1:"))
R2 = float(input("veuillez entrer la valuer de R2: "))
R3 = float(input("veuillez entrer la valuer de R3: "))


Rser = R1+R2+R3
Rpar = (R1*R2*R3) / (R1*R2+R2*R3+R2*R3)

print("la valeur de la resistance en serie est :", format(Rser,".2f"))
print("la valeur de la resistance en Parallele est :", format(Rpar,".2f"))