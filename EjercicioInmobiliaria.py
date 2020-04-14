# Ejercicio Inmobiliaria

salario = 8000
cVentas = int(input("Ingrese cantidad de ventas: "))
iTotal = int(input("Ingrese el importe total de ventas: "))
#comision= 500 * cVentas
iPagar = salario + 500 * cVentas + iTotal * 0.02
print("Total a pagar:", iPagar)
