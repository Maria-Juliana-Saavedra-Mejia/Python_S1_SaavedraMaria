## Fibonacci Sequence

def fibonacci(n):
    v1=0
    v2=1
    v3=v1+v2 
    for i in range(2, n):
       v3=v1+v2 
       v1=v2
       v2=v3
       print(v3)

n=int(input("coloque la cantidad de terminos de la sucesion: "))

##Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816
