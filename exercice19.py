print("programme de calcule la somme des entiers jusqu'a ce nombre")
n  =int(input("saisie nombre:"))
while n<=1 :
    n=int(input("saisie nombre:"))
s = 0
i = 1
while i <= n :
    s = s+i
    i = i+1
print("la somme des entiers jusqu'a nombre :" ,n, "est: ", s)