print("Programme calculatrice")
A = float(input("veuillez entrer la valuer de A "))
B = float(input("veuillez entrer la valuer de B "))
Opera = input("veuillez entrer l'operateur")
if Opera == "+" :
    s = A + B
    print("la somme est :", s)
elif Opera == "-":
    m = A - B
    print("moins est :", m)
elif Opera == "*":
    mu = A - B
    print(" multiplier est :", mu)
elif Opera == "/":
   
    if B != 0:
         div = A / B
         print("moins est :",div)
    else : 
        print(" la division par 0 est impossible ")

