## Number Classification

def par_impar(n):
    if n%2==0:
        print (n," Es un numero par")
    else:
        print (n," Es un numero impar")


def primo_compuesto(n):
    divisores=0
    for i in range (2,n):
        if n%i==0:
          divisores+=i  

    if divisores==0:
        print (n," Es un numero primo")
    else:
        print (n," Es un numero compuesto")
  

def cuadrado_perfecto(n):
    r= int (n**0.5)
    if r*r == n:
        print (n," Es un cuadrado perfecto")
    else:
        print (n," No es un cuadrado perfecto")



n=int(input ("Ingres el numero: "))
print (par_impar(n))
print (primo_compuesto(n))
print (cuadrado_perfecto(n))

##Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816