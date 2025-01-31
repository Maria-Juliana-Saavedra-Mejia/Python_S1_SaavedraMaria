res=0
mult=0
div=0
sum=0
print ("Bienvenido a la calculadora de Maria Julianan Saavedra")
n1=int(input("Escriba el primer numero: "))
n2=int(input("Escriba el segundo numero: "))
print ("suma (1)")
print ("Resta(2)")
print ("Multiplicacion (3)")
print ("Division (4)")
Code=int(input("Digite el codigo para la operacion que quiere realizar: "))

if Code == 1:
    sum = n1 + n2 
    print("la suma entre ", n1, " y ", n2, " es : ", sum)

if Code == 2:
    res = n1 - n2 
    print("la suma entre ", n1, " y ", n2, " es : ", res)

if Code == 3:
    mult = n1 * n2 
    print("la suma entre ", n1, " y ", n2, " es : ", mult)

if Code == 4:
    div = n1/ n2 
    print("la suma entre ", n1, " y ", n2, " es : ", div)

if Code > 4:
    print("Codigo incorrecto")

