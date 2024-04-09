print("programme de table multiplication")
a = int(input("saisir la valeur de a :"))
while a<1 or a>10 :
   a = int(input("saisir la valeur de a :"))
i=0
# methode 1:
#while i in range(11) :
     #m=i*a
    # print(i,"x",a,"=",m)
     #i=i+1
# methode 2:
while i <= 10 :
   m=i*a
   print(i,"x",a,"=",m)
   i=i+1