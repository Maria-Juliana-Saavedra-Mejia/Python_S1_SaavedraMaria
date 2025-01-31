##Nùmero entero serie
CantidadTerminos=int(input("Ingresa el ultimo numero de la sucesion: "))
if CantidadTerminos <= 0: 
    print ("0")

sum=0
for i in range (1, CantidadTerminos):
    if (i%2==0):
         sum=sum-(1/i)
    else:
        sum=sum +(1/i)

print ("La cantidad de terminos es: ", CantidadTerminos)
print ("La sumatoria da: ", sum)
   
## Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816