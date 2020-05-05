# Simulacro 1er Parcial

# Ejercicio 1
# Solicitar al usuario 10 números.
# Luego informe cuál fue el mayor número ingresado.

#primeraVuelta = True
#menor = 0
mayor = 0
vueltas = 1
#acumulador = 0
while vueltas <= 10: 
    numero = 3
    #numero = int(input("Ingrese un nro: "))
    #acumulador = acumulador + numero

#    if primeraVuelta == True:
#        menor = numero
#        primeraVuelta = False

    if numero > mayor:
        mayor = numero
    
    vueltas = vueltas + 1
    
print("El nro mayor es: ", mayor)
#print("La suma total es: ", acumulador)


# Ejercicio 2
# Solicitar al usuario el ingreso de un número.
# Verificar que sea mayor a cero, si no lo es imprimir
# un mensaje de error. Si es mayor a cero, imprimir todos
# los números de 0 al número ingresado, que sean múltiplos de 4.

x = 0
nro = 2
#nro = int(input("Ingrese un nro mayor a cero: "))
if nro <= 0:
    print("Error")
else:
    while x <= nro:
        if x % 4 == 0:
            print(x)
        x = x + 1
        #x = x + 4

# Ejercicio 3
# Desarrolle un programa para una ferretería que pida al usuario
# el importe de las últimas 10 ventas y
# luego informe la cantidad de ventas para cada una
# de las siguientes categorías:
# - Ventas Chicas: menos de $1000
# - Ventas Medianas: entre $1000 y $5000
# - Ventas Grandes: más de $5000
    
vueltas = 0
ventasChicas = 0
sumaVentasChicas = 0
ventasMedianas = 0
ventasGrandes = 0
while vueltas > 10:
    
    venta = int(input("Ingrese el importe de la venta: "))
    
    if venta <= 1000:
        ventasChicas= ventasChicas + 1 #contador
        sumaVentasChicas = sumaVentasChicas + venta #acumulador
    else:
        if venta > 5000:
            ventasGrandes = ventasGrandes + 1
        else: # venta > 1000 and venta <= 5000
            # No es menor que 1000
            # No es mayor que 5000
            ventasMedianas = ventasMedianas + 1
    
    vueltas = vueltas + 1

print("Ventas Chicas: ", ventasChicas)
print("Suma ventas chicas: ", sumaVentasChicas)
print("Ventas Medianas: ", ventasMedianas)
print("Ventas Grandes: ", ventasGrandes)

# Ejercicio 4
# Solicitar al usuario el ingreso de números,
# continuar hasta que ingrese -1.
# En este momento imprimir a pantalla la cantidad
# de números ingresados y el resultado de la suma de los mismos.

nro = 0
cantidad = 0
suma = 0
while nro != -1:
    nro = int(input("Ingrese un nro: (-1 para salir)"))
    if nro != -1:
        cantidad = cantidad + 1
        suma = suma + nro

print("Cantidad: ", cantidad)
print("Suma: ", suma)

# Ejercicio 5
# Solicitar al usuario que ingrese tres números.
# Luego validar que el primer número ingresado
# sea menor que el segundo,
# y el segundo menor que el tercer número.
# En caso afirmativo imprimir por pantalla "Correcto" sino "Incorrecto".

nro1 = int(input("Ingrese nro 1"))
nro2 = int(input("Ingrese nro 2"))
nro3 = int(input("Ingrese nro 3"))

if nro1 < nro2:
    if nro2 < nro3:
        print("Correcto")
    else:
        print("Incorrecto")
else:
    print("Incorrecto")
    
if nro1 < nro2 and nro2 < nro3:
    print("Correcto")
else:
    print("Incorrecto")
