## Programa de comparacion de numeros
print ("Los nùmeros que satisfacen la siguiente expresiòn P^3 + Q^4 -2 * P^2 < 680 son: ")
for p in range (0, 200):
    for q in range (0,200):
        expresionMatematica= p**3 + q**4 -2 * p**2
        if (expresionMatematica<680):
            print ("P: ", p)
            print ("Q: ", q)
            print ("Resultado= ", expresionMatematica)
## Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816