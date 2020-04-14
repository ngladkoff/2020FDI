"""
Clase 2
Prof: Nicolas
Materia: FDI
"""

"""
valor1 = int(input("Ingrese valor 1: "))
valor2 = int(input("Ingrese valor 2: "))
resultado = valor1 + valor2
print("Resultado:", resultado)
"""

"""
descuento = 0
importeVenta = 2000
if importeVenta >= 1000:
    descuento = importeVenta * 0.10
elif importeVenta >= 500:
    descuento = importeVenta * 0.05
print("Importe a pagar:", importeVenta - descuento)
"""
"""
suma, numero= 0,1
while numero <= 10:
    suma= suma + numero
    numero = numero + 1
print("La suma es: ", suma)
"""

## Repetir 10
vuelta = 1
while vuelta <= 10:
    #print(contar)
    print("Hola")
    
    vuelta = vuelta + 1

print("Menu:")
opcion = 0
while opcion != 9:
    print("1 - Hacer a")
    print("2 - Hacer b")
    print("9 - Salir")
    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        print("Hacer A")
    elif opcion == 2:
        print("Hacer B")

