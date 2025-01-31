## Temperature Conversion

def celcius_farengeith(temp):
    farengeith= (temp*9/5) +32
    return farengeith

def Farengeith_celcius(temp2):
    celcius= (temp2 - 32) * 5/9 
    return celcius

print (" (1)")
print ("Celcius (2)")
n=int(input("coloque el codigo de que temperatura quiere encontrar: "))

if n==1: 
    temp=int(input("Digite el valor de su temperatura: "))
    print (celcius_farengeith(temp), " °F")


if n==2: 
    temp2=int(input("Digite el valor de su temperatura: "))
    print (Farengeith_celcius(temp2), " °C")

if n>2:
    print("Codigo incorrecto")


##Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816
