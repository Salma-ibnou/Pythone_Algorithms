s = 0
for i in range(8):
   print("entrer nombre N",i+1," : ", end=" ")
   n = int(input())
   if n < 0:
      break
   else:
    s = s+n
print("la somme est :",s)  