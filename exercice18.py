print("programme de nombre compis entre 10 et 20")
n = int(input("saisie un nombre :"))
while n<10 or n>20 :
    if n<10 :
        print("plus petit")
    
    elif n>20 :
        print("plus grand") 
    n = int(input("saisie un nombre :"))
while n>=10 or n<=20 :
    print("bravo! le nombre compis entre 10 et 20")
    break
