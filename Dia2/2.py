## Interes Calculator 

def interes_simple (c,r,t):
    inte= c*(r/100)*t
    return inte 

def interes_compuesto (c,r,p):
    com=c*(1 + ((r/100)/p))-c
    return com


c=float(input("Ingrese el capital: "))
r=float(input("Ingrese la tasa de interes en porcentaje: "))
t=float(input("Ingrese el tiempo (en años): "))
p=int(input("Digite el numero de periodos para el capital compuesto: "))
print ("Su interes simple es de: $ ", interes_simple (c,r,t))
print ("Su interes compuesto es de: $ ", interes_compuesto (c,r,p))

##Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816