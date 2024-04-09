import math
print(" Programme qui calcule les solutions d~une équation du second degré")
a = float(input("veuillez entrer la valuer de a :"))
b = float(input("veuillez entrer la valuer de b :"))
c = float(input("veuillez entrer la valuer de c :"))
delta = b ** 2 - 4 * a *  c
if delta < 0 :
   print("n'est pas de solution")
elif delta == 0 :
   x = (-b)/(2*a)
   print("la solutions sont :", format(x , ".2f"))
else:
    x1 = ( -b - math.sqrt(delta))/(2*a)
    x2 = ( -b + math.sqrt(delta))/(2*a)
    print("la solutions sont :", format(x1 , ".2f"), "et",format(x2 , ".2f"))