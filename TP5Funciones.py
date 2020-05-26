# TP 5 - Funciones

# Ejercicio 4
"""
def es_par_opcion2(p):
    return p % 2 == 0
"""

"""
def es_par(p):
    if p % 2 == 0:
        return True
    else:
        return False
    
    
variable= int(input("Ingrese Nro: "))

esNroPar = es_par(variable)
if esNroPar == True:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")
"""

"""
if es_par(variable):
    print("Es par")
else:
    print("Es impar")
"""    
    
# Ejercicio 5

"""
def devolver_mayor(valor1, valor2):
    
    if valor1 >= valor2:
        return valor1
    else:
        return valor2
    

v1 = int(input("Ingrese valor 1: "))
v2 = int(input("Ingrese valor 2: "))
mayor = devolver_mayor(v1,v2)
print("El número mayor es:", mayor)
"""

# print(mayor(int(input("Primer numero:")), int(input("Segundo numero:"))))

# Ejercicio 6

"""
def es_multiplo(valor1, valor2):
    if valor1 % valor2 == 0:
        return True
    else:
        return False
    
# print("40 es múltiplo de 8?: ",es_multiplo(40,8))
# print("50 es múltiplo de 3?: ",es_multiplo(50,3))

v1= int(input("Ingrese v1: "))
v2= int(input("Ingrese v2: "))
print("El 1ro es múltiplo del 2do?", es_multiplo(v1,v2))
"""

# Ejercicio 7

def factorial2(nro):
    calculo = 1
    vuelta = 1
    while vuelta <= nro:
        calculo = calculo * vuelta
        vuelta = vuelta + 1
    
    return calculo


def factorial(nro):
    calculo = nro

    while nro != 1:
        nro = nro - 1
        calculo = calculo * nro
    return calculo

print("El factorial de 4 es: ", factorial(4))
print("El factorial de 6 es: ", factorial(6))
    

# Ejercicio 9

def signo(n):
    resultado = 0
    
    if n < 0:
        resultado = -1
    elif n > 0:
        resultado = 1
    else:
        resultado = 0

    return resultado

def signo2(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
    
nro = int(input("ingrese nro: "))
resultado = signo2(nro)
print(resultado)

# Ejercicio 10

def comparar(a,b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0
    
nro = int(input("Ingrese un nro: "))
nro2 = int(input("Ingrese otro nro: "))
resultado = comparar(nro,nro2)
print(resultado)


    

