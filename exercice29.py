
import math
print(" Programme qui calcule la distance entre deux points A et B du plan")
xA = float(input("Entrez la coordonnée x du point A : "))
yA = float(input("Entrez la coordonnée y du point A : "))
xB = float(input("Entrez la coordonnée x du point B : "))
yB = float(input("Entrez la coordonnée y du point B : "))
AB = (xB- xA)**2 + (yB - yA)**2
AB= math.sqrt(AB)
print("La distance entre les points A et B est :",format(AB,".2f"))