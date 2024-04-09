print("programme le citoyen peut voter ou ne peut pas voter")
age = int(input("veuillez vous entrer votre age :"))
msg ="vous pouvez voter " if age >= 18 else "vous ne pouvez pas voter"
print(msg)
