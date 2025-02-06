import json
from os import system

def abrirJSON():
    dicFinal={}
    with open("./libros.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./libros.json",'w') as outFile:
        json.dump(dic,outFile)

## Menu inicio para clientes o administradores 

print ("Bienvenido al programa de la Biblioteca Campuslands")
print ("Si es administrador digite   (1)")
print ("Si es cliente digite         (2)")
op=int(input("Digite su elecciòn: "))
system("clear")
##Clave administradores 
if op==1:
    codigo=int(input("Digite su codigo "))
    if codigo==101 or codigo==102 or codigo==506 or codigo==641 :
        ##Menu administradores
        print("Para agregar un libro                  (1)")
        print("Para ver el catalog de libros          (2)")
        print("Para eliminar un libro                 (3)")
        print("Para editar la informacion de un libro (4)")
        print("Para salir del programa                (5)")
        admin=int(input("Digte su eleccion "))
        system("clear")
        while admin!=5:
            ## Menu para saber la categoria del libro
            if admin==1:
                print("Fantasia         (1)")
                print("Terror           (2)")
                print("Accion y aventura(3)")
                print("Fantasia         (4)")
                tipodeLibro=int(input("Elija la categoria del libro: "))
                if tipodeLibro==1: ## si es de fantasia 
                    libroNuevo={}
                    nl=str(input ("Digite el nombre del libro nuevo "))
                    libroNuevo["Libro"]=nl
                    ano=str(input("Digite el año en que el libro fue lanzado "))
                    libroNuevo["Año"]=ano
                    au=str(input ("Digite el autor del libro "))
                    libroNuevo["Autor"]=au
                    dis=int(input("Digite la disponibilidad del libro (1-disponible)(2- no disponible) "))
                    if dis==1:
                        libroNuevo["Disponibilidad"]=True
                    else:
                        libroNuevo["Disponibilidad"]=False

                    ["Fantasia"].append(libroNuevo)
                    guardarJSON(libroNuevo)
                    system("clear")
                if tipodeLibro==2: ## si es de terror 
                    libroNuevo={}
                    nl=str(input ("Digite el nombre del libro nuevo "))
                    libroNuevo["Libro"]=nl
                    ano=str(input("Digite el año en que el libro fue lanzado "))
                    libroNuevo["Año"]=ano
                    au=str(input ("Digite el autor del libro "))
                    libroNuevo["Autor"]=au
                    dis=int(input("Digite la disponibilidad del libro (1-disponible)(2- no disponible) "))
                    if dis==1:
                        libroNuevo["Disponibilidad"]=True
                    else:
                        libroNuevo["Disponibilidad"]=False

                    ["Terror"].append(libroNuevo)
                    guardarJSON(libroNuevo)
                    system("clear")

                if tipodeLibro==4: ## si es de Ciencia Ficcion
                    libroNuevo={}
                    nl=str(input ("Digite el nombre del libro nuevo "))
                    libroNuevo["Libro"]=nl
                    ano=str(input("Digite el año en que el libro fue lanzado "))
                    libroNuevo["Año"]=ano
                    au=str(input ("Digite el autor del libro "))
                    libroNuevo["Autor"]=au
                    dis=int(input("Digite la disponibilidad del libro (1-disponible)(2- no disponible) "))
                    if dis==1:
                        libroNuevo["Disponibilidad"]=True
                    else:
                        libroNuevo["Disponibilidad"]=False

                    ["Ciencia Ficcion"].append(libroNuevo)
                    guardarJSON(libroNuevo)
                    system("clear")
                if tipodeLibro==3: ## si es de Accion y Aventura
                    libroNuevo={}
                    nl=str(input ("Digite el nombre del libro nuevo "))
                    libroNuevo["Libro"]=nl
                    ano=str(input("Digite el año en que el libro fue lanzado "))
                    libroNuevo["Año"]=ano
                    au=str(input ("Digite el autor del libro "))
                    libroNuevo["Autor"]=au
                    dis=int(input("Digite la disponibilidad del libro (1-disponible)(2- no disponible) "))
                    if dis==1:
                     libroNuevo["Disponibilidad"]=True
                    else:
                        libroNuevo["Disponibilidad"]=False

                    ["Accion y Aventura"].append(libroNuevo)
                    guardarJSON(libroNuevo)
                    system("clear")
    else:
        print("Codigo incorrecto")
        exit()




## Menu para clientes 

