##Ejericio 7 Pro- Filtro Python
##Numeros Amigos

def suma_divisores_propios(n):
    suma=0
    for i in range(1,n):
        if n%i == 0:
            suma += i #suma=suma+i
    return suma

def numeros_amigos(a,b):
    return suma_divisores_propios(a) == b and suma_divisores_propios(b) == a

num1=int(input("Ingresa el primer número:"))
num2=int(input("Ingresa el segundo número:"))

if(numeros_amigos(num1,num2)):
    print("Los numeros se aman! :loveatfirstsight:")
else:
    print("Los numeros se odian")