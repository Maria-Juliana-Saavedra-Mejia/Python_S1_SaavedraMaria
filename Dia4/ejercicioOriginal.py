##  Ejercicio Modulos
bo=True
while bo==True:
    from inicio import*
    print (inicio())
    opc=int(input(":"))
    from modulop import *
    if opc==1:
        print(agregarEstudiante())
    elif opc==2:
        print(verLista())
    elif opc==3:
        print (editarEstudiante())
    elif opc==4:
        print(eliminarEstudiante())
    elif opc==5:
        break
    else:
        print (caracterDesconocido())
  ##Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816
