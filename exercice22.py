#les fonction :
# la definitin des fonctions :
def signe( A , B):
    if A * B > 0 :
        print("les valeurs A et B ont meme signe")
    else:
        print("les valeurs A et B  ont deux signes diffirents ")
def maximum (A,B):
    if A > B :
        return A
    else:
        return B

def minimum( A , B):
    if A < B :
        return A
    else:
        return B
    
# l'appel des fonctions :

A = int(input("veuillez entrer la valeur de A :"))
B = int(input("veuillez entrer la valeur de B :"))
signe(A , B)
print("la valeur maximum est :",maximum(A,B))
c = minimum(A,B)
print("la valeur le minimum est :",c)
