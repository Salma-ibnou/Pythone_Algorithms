print(" Programme qui retourne le type d'un caractère : alphabet, nombre ... ")
car = input("veuillez entrer un caractere :")
if "a" <= car <= "z" or "A" <= car <= "Z":
    print(car, "est une lettre de l'alphabet.")
elif "0" <= car <= "9":
    print(car, "est un chiffre.")
else:
    print(car, "est un caractère spécial.")