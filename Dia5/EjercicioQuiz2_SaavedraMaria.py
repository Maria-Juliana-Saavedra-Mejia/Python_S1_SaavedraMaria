import json
def abrirJSON():
    dicFinal={}
    with open,{'./inmuebles.json','r'}as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
def guardarJSON(dic):
    with open, {'./inmuebles.json','w'}as outFile:
        json.dump(dic, outFile)

inmuebles={}
print("Bienvenido al sistema de compra de inmuebles")
print("(1) digite si es admin")
print("(2) digite si es cliente")
op1=int(input("Digite el codigo según le corresponda:  "))
booleano=True
while booleano==True:  
    inmuebles=abrirJSON
    if op1==1:
        print("(1) si quiere crear un nuevo inmueble")
        print("(2) si quiere ver los inmuebles")
        print("(3) si quiere realizar un cambio en algún inmueble")
        print("(4) si quiere eliminar un inmueble")
        print("(5) si quiere salir del programa")
        admin=int(input("Digite el codigo de lo que quiere realizar:  "))   
        if  admin==1:
            año=int(input("Digite el año de su inmueble"))
            metro=int(input("Digite los metros de su inmueble"))
            habitaciones=int(input("Digite la cantidad e habitaciones de su inmueble"))
            garaje=int(input("¿Tiene Garaje"))
            print("1. si")
            print("2. no")
            g=int(input("Digite la opcion: "))
            if g==1:
                garaje=True
            if g==2:
                garaje=False 
            else:
                print=("codigo incorrecto")
            zona=input("digite la zona en que esta ubicado (A) O (B)")
            
        if admin==2:
            for i in range(len(inmuebles["listainmuebles"])):
                print(inmuebles["listainmuebles"][i])

        if admin==3:
            print()

        if admin==4:
            print()

        if admin==5:
            break

    if op1==2:
        for i in range(len(inmuebles["listainmuebles"])):
            print(inmuebles["listainmuebles"][i])
        dinero=int(input("Digite el precio que dispone para la compra: "))
