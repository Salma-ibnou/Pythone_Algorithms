print(" Structure conditionnelle alternative : if ...: ... else : ...")
sex = input("veuillez entrer le sex de l'habitant (H/F) :")
age = int(input("veuillez entrer de l'habitant l'age :"))

#---------------------METHODE1-----------------#
#if sex == "H" and age >= 20:
##       print("l'habitant  est imposable")
##elif sex == "F" and 18 <=age<=35:
##        print("l'habitant  est imposable")
##else:
##      print("l'habitant  est non imposable")

#---------------------METHODE2-----------------#
#if (sex == "H" and age >= 20) or (sex == "F" and 18 <=age<=35):
  #  print("l'habitant  est imposable")
#else :
   # print("l'habitant  est non imposable")

#---------------------METHODE33-----------------#
R1 =  sex == "H" and age >= 20
R2 =  sex == "F" and 18 <=age<=35
if R1 == True :
    print("l'habitant  est imposable")
elif R2 == True :
    print("l'habitant  est imposable")
else:
    print("l'habitant  est non imposable")
    