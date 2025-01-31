print("Hola Mundo!")
## TIPOS DE DATOS
## 1. STRING
cadenaTexto= "textico"
print (type(cadenaTexto))
## 2. NUMERO ENTERO
numeroEntero=2
print (type( numeroEntero))
## 3. NUMERO FLOTANTE - FLOAT 
numeroFlotante=1.1
print (type(numeroFlotante))
## 4. NUMERO DOBLE - DOUBLE 
numeroDoble=1.09378756538596574657846586846465875694876
print (type (numeroDoble))
## 5. BOOLEANO - TRUE/FALSE 
Booleanito= True
print (type (Booleanito))

## ENTRADAS POR PARTE DEL USUARIO
x=input ("Ingresa un nùmero") ## TODO IMPUT ES TEXTO/STRING
print(type (x))

## CONVERSION E TIPOS DE DATO - CASTEO 
## SINTÀXIS - TIPO DATO(DATO_A_CONVERTIR)
x=int(input("Ingresa un numero"))
print(type (x))

## EJERCICIO - SUMAR DOS NUMERS DADODS POR UUARIO 
N1=int(input("Ingresa primer numero"))
N2=int(input("Ingresa segundo numero"))
rta= N1 + N2
print("El resutado final es", rta)

## CICLOS FOR AND WHILE
##CICLO FOR NORMAL
for i in range (5): ## i sera iterador hasta el 5
    print (i)

print ("###############")
## CICLO CON PASOS 

for i in range (0,5,2): ## i sera el iterador e ira desde 0 hasta 5 con paso 2 en 2 
    print(i)


print ("###############")
## CICLO WHILE

Booleanito1= True
while (Booleanito1 == True):
   print (Booleanito1)
   Booleanito1= False    

   
##4 tipos de funciones
##Funcion sin parametros y sin retorno
def funcion1():
    print("Soy una funcion increible!!!!!!!")


funcion1()

##Funcion sin parametros pero con retorno
def funcion2():
    return 5
print("Su número es:",funcion2())

##Funcion con parámetros pero sin retorno
def funcion3 (nombre,apellido):
    print("Su nombre es:",nombre," ",apellido)
funcion3("Edgar","Acevedo")

##Función con parámetros y retorno
def funcion4(a,b):
    c= a**b
    return c

funcionA= int(input("Ingrese el numero base:"))
funcionB=int(input("Ingrese la elevación deseada:"))
print("El resultado de su elevación es de:",funcion4(funcionA,funcionB))
##Desarrollado por : Pedro Gomez / C.C:1.666.555.444

