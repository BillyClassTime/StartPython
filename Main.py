import os
#from Varios import principal
import Ejercicio1DNI
import Ejercicio2Salarios
while True:
    os.system("cls") #Limpia la pantalla en la consola
    print("Bienvenidos")
    print("Menu principal")
    print("1-Calcular DNI")
    print("2-Calcular Salario Neto Español")
    print("8-Año bisiesto")
    print("10-Ordenar una cadena")
    print("20-Determinar números capicuas")
    print("0 -Salir")
    opcion = input("Seleccione una opción:")
    if opcion == "1":
        Ejercicio1DNI.principal()
    elif opcion == "2":
        Ejercicio2Salarios.principal()
    elif opcion == "0":
        print("Un placer atenderle. Bye")
        break
    continuar=input("Presione enter para continuar...")