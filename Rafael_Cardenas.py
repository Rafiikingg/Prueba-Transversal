import random
import csv
import math 
import statistics

trabajadores = (['Juan Pérez'],['María García'],['Carlos López'],['Ana Martínez'],['Pedro Rodríguez'],['Laura Hernández'],['Miguel Sánchez'],['Isabel Gómez'],['Francisco Díaz'],['Elena Fernández'])

def asignar_sueldos (trabajadores):
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        trabajador.append(sueldo)
    print()
    print("Los sueldos han sido asignados")

def clasificar_sueldo (trabajadores):
    for trabajador in trabajadores:
        sueldo = trabajador[1]
    try:
        print("--SUELDOS MENORES A 800.000--")
        print("Nombre empleado \t Sueldo")
        for trabajador in trabajadores:
            if trabajador[1] < 800000:
                print(trabajador)
        print("--SUELDOS ENTRE 800.000 Y 2.000.000--")
        print("Nombre empleado \t Sueldo")
        for trabajador in trabajadores:
            if trabajador[1] < 800000 and trabajador[1] <= 2000000:
                print(trabajador)
                
        print("--SUELDOS MAYORES A 2.000.000--")
        print("Nombre empleado \t Sueldo")
        for trabajador in trabajadores:
            if trabajador[1] < 2000000:
                print(trabajador)
        print(f"\nTOTAL SUELDO: ")  
    except IndexError:
        print("No existen sueldos registrados")
        
    

def estadisticas (trabajadores):
    for trabajador in trabajadores:
        try:
            sueldo = trabajador[1]
            sueldo_alto = max(trabajador[1])
            sueldo_menor = min(trabajador[1])
            promedio_sueldo = sum(trabajador[1]) / len[trabajadores]
            sueldototal = sum (trabajador[1]) 
            mediagenerica = sueldototal ** (1/len(trabajadores))

            print("ESTADISTICAS DE SUELDO")
            print(f"Sueldo mas alto: {sueldo_alto}")
            print(f"Sueldo mas bajo: {sueldo_menor}")
            print(f"Promedio sueldo: {promedio_sueldo}")
            print(f"Media generica: {mediagenerica}")
        except Exception:
            print("No hay sueldos registrados")

def reporte_de_sueldos (trabajadores):
    
    for trabajador in trabajadores:
        trabajador = trabajadores[1]
        sueldobruto = trabajador[1]
        descuentosalud = round(sueldobruto * 0.07)
        descuentoafp= round(sueldobruto * 0.12)
        sueldoliquido = (sueldobruto - descuentoafp) - descuentosalud
        with open ("reporte_de_sueldos.csv", 'w', newline='',encoding='utf-8') as archivo:
            archivo.write("|Nombre empleado| \t |Sueldo Bruto| \t |Decuento Salud| \t |Sueldo Liquido|")
            for trabajador in trabajadores:
                archivo.write(f"\n{trabajador}, {sueldobruto}, {descuentosalud}, {descuentoafp}, {sueldoliquido}")
def salir():
    print("Finalizando programa...")
    print("Desarrollado por Rafael Cárdenas")
    print("Rut 22.061.709-2")
    
while True:

    print("""
    -----------MENÚ------------
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadisticas
    4. Reporte de sueldos
    5. Salir del programa """)
    print()
    try:
        opc = int(input("Elija una opción: "))
        if opc == 1:
            asignar_sueldos(trabajadores)
        if opc == 2:
            clasificar_sueldo(trabajadores)
        if opc == 3:
            estadisticas(trabajadores)
        if opc == 4:
            reporte_de_sueldos(trabajadores)
        if opc == 5:
            salir()
            break
    except ValueError:
        print()
        print("Debes ingresar una de las opciones")
        
        continue

