## Ejercicio empresa 
mayorSueldo = -1
menorSueldo = float('inf')
TotalBruto = 0
TotalEp = 0
TotalPension = 0
TotalNeto = 0
n=int(input("Ingrese el numero de empleados: "))
for i in range (1,n+1):
    nom=str(input("Digite su nombre: "))
    horas=int(input("Digite las horas trabajadas: "))
    bruto= horas * 20000
    eps= bruto * 0.04
    pension= bruto * 0.04
    neto= bruto- eps-pension 

    TotalBruto= TotalBruto + bruto
    TotalEp= TotalEp + eps
    TotalPension= TotalPension + pension
    TotalNeto= TotalNeto + neto

    if neto> mayorSueldo:
         mayorSueldo= neto
         nombreMayor= nom
    if neto < menorSueldo:
         menorSueldo= neto
         nombreMenor= nom

    print ("Empleado: ", nom)
    print ("Salario Bruto: ", bruto)
    print ("EPS ", eps)
    print ("Pension: ", pension)
    print ("Salario Neto: ", neto)

promedioBruto= TotalBruto/n
promedioNeto= TotalBruto/n
print ("Totales: ")
print ("Total Salarios Brutos: ", TotalBruto)
print ("Total EPS: ", TotalEp)
print ("Total Pension: ", TotalPension)
print ("Total Salarios Netos: ", TotalNeto)
print ("Empleado que mas gana: ", nombreMayor)
print ("Empleado que mas gana salario: ", mayorSueldo)
print ("Empleado que menos gana: ", nombreMayor)
print ("Empleado que mas gana salario: ", menorSueldo)
print ("Promedio Salario Bruto: ", promedioBruto)
print ("Promedio salarioa Neto: ", promedioNeto)

##Desarrollado por : Maria Juliana Saavedra Mejia / T.I. 1097100816