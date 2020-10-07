import math
num= int(input ("numero por favor "))
raiz= int(math.sqrt(num))
verificador=0
for i in range (2,raiz):
     divisor= num%i
     if divisor==0:
         verificador+=1
     
if verificador==0:
    print ("El numero " + format(num) + " es primo")

else:
    print ("El numero " + format(num) + " no es primo")
