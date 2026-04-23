import os
os.system("cls")

IVA = 0.19
PRESUPUESTO_MAXIMO = 50000000

nombre_proyecto = input("Ingrese el nombre del proyecto: \n")

try:
    cantidad_metros = int(input("Ingresa la cantidad de metros cuadrados a construir: \n"))
    while cantidad_metros <= 0:
        cantidad_metros = int(input("La cantidad de metros debe ser mayor a 0\nIngrese la cantidad de metros:\n"))
    costo_metros = int(input("Ingresa el costo por metro cuadrado: \n"))
    while costo_metros <= 0:
        costo_metros = int(input("El costo por metro debe ser mayor a 0\nIngrese el costo por metro:\n"))
    cantidad_trabajadores = int(input("Ingrese la cantidad de trabajadores:\n"))
    while cantidad_trabajadores <= 0:
        cantidad_trabajadores = int(input("La catindad de trabajadores debe ser mayor a 0\nIngrese la cantidad de trabajadores:\n"))
    sueldo_trabajadores = int(input("Ingrese el pago por cada trabajador:\n"))
    while sueldo_trabajadores <= 0:
        sueldo_trabajadores = int(input("El pago por trabajador debe ser mayor a 0\nIngrese el pago por trabajador:\n"))
except:
    print("El pepe")

costo_materiales = cantidad_metros * costo_metros
costo_obra = cantidad_trabajadores * sueldo_trabajadores

costo_neto = costo_materiales + costo_obra

valor_iva = costo_neto * IVA
costo_total = costo_neto + valor_iva

presupuesto_ajustado = PRESUPUESTO_MAXIMO * 1.1

if costo_total <= PRESUPUESTO_MAXIMO:
    estado = "Dentro del presupuesto"
elif costo_total > PRESUPUESTO_MAXIMO and costo_total <= presupuesto_ajustado:
    estado = "Presupuesto ajustado"
else:
    estado = "Fuera del presupuesto"

os.system("cls")
print(f"-------Resúmen del proyecto--------")
print(f"Nombre: {nombre_proyecto}")
print(f"Costo total: {round(costo_total, 2)}")
print(f"Estado del proyecto: {estado}")
print(f"Fin")
