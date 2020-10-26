import math
num1= int(input ("numero por favor "))
num2= int(input ("numero por favor "))

top=num2+1

for x in range(num1, top):
    verificador=0
    num=(x)
    raiz= int(math.sqrt(num)+1)
    for i in range (2,raiz):
         divisor= num%i
         if divisor==0:
             verificador+=1
         
    if verificador==0:
        print ("El numero " + format(num) + " es primo y tiene " + format(verificador) +" divisores")

    else:
        print ("El numero " + format(num) + " no es primo")
