## Mayor y menor 
grande=0
pequeño=0
for i in range (1,11):
    N=int(input("Ingresa numero: "))
    if i==1:
        grande=N
        pequeño=N
    elif N> grande:
        grande=N
    elif N<pequeño:
        pequeño=N

             
print ("El mayor es: ", grande)
print ("El menor es: ", pequeño)

## Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816