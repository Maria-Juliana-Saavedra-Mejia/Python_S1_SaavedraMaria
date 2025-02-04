nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]
apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

booleano=True
while (booleano==True):
    print("Digite 1 si quiere cambiar el nombre de algun estudiante")
    print("Digite 2 si quiere cambiar el apellido de algun estudiante")
    print("Digite 3 para acabar con el programa")
    n1=int(input("Digite el codigo de lo que quiere modificar"))
    if n1==1:
        for i in range (len(nombres)):
            print("Nombre #: ", i , " : ", nombres[i], apellidos[i])
        NumeroEst=int(input("Digite el numero del estudiante que quiere editar"))
        cambioEst=input("Digite el nombre nuevo del estudante:")
        nombres[NumeroEst]=[cambioEst]
        for i in range (len(nombres)):
             print("Nombre #: ", i , " : ", nombres[i], apellidos[i])
    if n1==2:
        for i in range (len(apellidos)):
             print("Apellidos #: ", i , " : ", nombres[i], apellidos[i])
        NumeroEst=int(input("Digite el numero del estudiante que quiere editar"))
        cambioEst=input("Digite el apellido nuevo del estudante:")
        apellidos[NumeroEst]=[cambioEst]
        for i in range (len(apellidos)):
             print("Apellidos #: ", i , " : ", nombres[i], apellidos[i])
    if n1==3:
        booleano=False
        break
    if n1>3:
        print ("Codgo incorrecto")    

    


        
        
