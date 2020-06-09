# Ejercicio 13 - Vectores
import random
maximo = 20
nombres = [''] * maximo
notas = [-1] * maximo

def menu():
    print("Menu:")
    print("1-Buscar Alumno")
    print("2-Modificar su nota")
    print("3-Realizar la media de notas")
    print("4-Realizar la media de notas menores a 5")
    print("5-Mostrar el alumno con mejor nota")
    print("6-Mostrar alumno con peor nota")
    print("9-Salir")
    return int(input("Ingrese opción: "))

def buscar_en_vector(a_buscar, vector, maximo):
    i = 0
    while i < maximo:
        if a_buscar == vector[i]:
            return i
        i = i + 1
    return -1

def buscar_alumno(nombres, notas, maximo):
    a_buscar= input("Ingrese el nombre a buscar: ")
    idx = buscar_en_vector(a_buscar, nombres, maximo)
    if idx == -1:
        print("No encontrado")
    else:
        print(nombres[idx], ' : ' , notas[idx])

def buscar_todos(nombres,notas,maximo):
    a_buscar= input("Ingrese el nombre a buscar: ")
    i = 0
    encontrado = False
    while i < maximo:
        if a_buscar == vector[i]:
            print(nombres[i], ':', notas[i])
            encontrado = True
        i = i + 1
    
    if encontrado == False:
        print("No encontrado")

def buscar_todos(nombres,notas,maximo):
    i = 0
    encontrado = False
    while i < maximo:
        if notas[i] >= 4:
            print(nombres[i], ':', notas[i])
            encontrado = True
        i = i + 1
    
    if encontrado == False:
        print("No encontrado")

def modificar_nota(nombres,notas,maximo):
    a_buscar= input("Ingrese el nombre del alumno a modificar: ")
    idx = buscar_en_vector(a_buscar, nombres, maximo)
    if idx == -1:
        print("No encontrado")
    else:
        print("Nota actual: ", notas[idx])
        nueva_nota= int(input("Ingrese nueva nota: "))
        notas[idx] = nueva_nota
    
def calcular_media_notas(notas, maximo):
    suma= 0
    i = 0
    cantidad = 0
    while i < maximo:
        if notas[i] != -1:
            suma = suma + notas[i]
            cantidad = cantidad + 1
        i = i + 1
    return suma // cantidad
    
def calcular_media_notas_menores5(notas, maximo):
    suma= 0
    cantidad = 0
    i = 0
    while i < maximo:
        if notas[i] < 5 and notas[i] != -1:
            suma = suma + notas[i]
            cantidad = cantidad + 1
        i = i + 1
        
    if cantidad == 0:
        return 0
    
    return suma // cantidad

def buscar_mejor_nota(notas,maximo):
    mayor = notas[0]
    i = 0
    while i < maximo:
        if notas[i] > mayor:
            mayor = notas[i]
        i = i + 1
    return mayor    

def buscar_peor_nota(notas,maximo):
    menor = notas[0]
    i = 0
    while i < maximo:
        if notas[i] < menor and notas[i] != -1:
            menor = notas[i]
        i = i + 1
    return menor    

def imprimir_alumnos_con_nota(nota,nombres,notas,maximo):            
    i = 0
    while i < maximo:
        if nota == notas[i]:
            print(nombres[i])
        i = i + 1



"""
i = 0
while i < maximo:
    nombres[i] = input("Ingrese nombre: ")
    notas[i] = int(input("Ingrese nota: "))
    i = i + 1    
"""

"""
nombres = ['Nicolas','Alejadro','Alberto','','','','','','','',]
notas = [10,9,8,5,2,1,9,6,4,3]
"""
i = 0
while i < maximo:
    nombres[i] = "Alumno" + str(i)
    notas[i] = random.randint(1,10)
    i = i + 1    


op = 0
while op != 9:
    op= menu()
    if op == 1:
        buscar_alumno(nombres,notas,maximo)
    elif op == 2:
        # buscar_todos(nombres, notas, maximo)
        modificar_nota(nombres,notas,maximo)
    elif op == 3:
        media = calcular_media_notas(notas,maximo)
        print("Media notas: ", media)
    elif op == 4:
        media = calcular_media_notas_menores5(notas,maximo)
        print("Media notas menores 5:", media)
    elif op == 5:
        mejor_nota = buscar_mejor_nota(notas,maximo)
        print("Mejor nota: ", mejor_nota)
        imprimir_alumnos_con_nota(mejor_nota,nombres,notas,maximo)
    elif op == 6:
        peor_nota = buscar_peor_nota(notas,maximo)
        print("Peor nota: ", peor_nota)
        imprimir_alumnos_con_nota(peor_nota,nombres,notas,maximo)
    elif op == 9:
        print("Hasta luego")

