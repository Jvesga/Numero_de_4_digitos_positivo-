"""programa que lee un numero y determina si es de 4 digitos y si es positivo"""

print("-----------------------------------------------------------")
print("----Programa para saber si es # de 4 digitos y positivo----")
print("-----------------------------------------------------------")

# input
X=int(input(" digite un valor para X: "))


# prossesing
if X >= 1000 and X <= 9999 :
    msj = "4 digitos"   
else:
    msj = "menos de 4 digitos"
if X > 0:
    msj2 = " positivo"
else:
    msj2 = " negativo"

# output 
print("El numero tiene " + str(msj),"y es" + str(msj2))
