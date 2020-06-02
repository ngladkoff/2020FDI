# TP6
"""
# Ej1
cantidad = 0
max = 5
numeros = [-1] * max
indice = 0
nro = 0
while nro != -1 and indice < max:
    nro = int(input("Ingrese un nro: "))
    if nro != -1:
        numeros[indice] = nro
        indice = indice + 1
cantidad = indice
indice = 0
while indice < cantidad:
    print(numeros[indice])
    indice = indice + 1
print("Cantidad: ", cantidad)

#Ej 2
vueltas = 0
suma = 0
while vueltas < cantidad:
    suma= suma + numeros[vueltas]    
    vueltas = vueltas + 1
    
print("Suma: ", suma)
print("Promedio: ", suma/cantidad)
"""
"""
# Devolver mayor
def devolver_mayor(v, tamanio):
    
    i = 1
    mayor = v[0]
    
    while i < tamanio:
        
        if v[i] > mayor:
            mayor = v[i]

        i = i + 1
    
    return mayor

def devolver_menor(v, tamanio):
    
    i = 1
    menor = v[0]
    
    while i < tamanio:
        
        if v[i] < menor:
            menor = v[i]

        i = i + 1
    
    return menor


vector1 = [40,3,25,50,25,3,40]
vector2 = [4,3,2,4,9,9,1,30,4,3]

m1= devolver_mayor(vector1, 7)
m2= devolver_menor(vector2, 10)
print("M1", m1)
print("M2", m2)
"""

# Ejercicio 12
max = 10
producto = ["Leche", "Atun", "Mermelada", "","","","","","",""]
cantidad = [5,3,7,0,0,0,0,0,0,0]
opMenu = 0
i = 3

def menu():
    print("Opciones:")
    print("1-Alta Producto")
    print("2-Búsqueda")
    print("3-Modificar Stock")
    print("9-Salir")
    op = int(input("Ingrese opción: "))
    return op

def alta_producto(p,c,i):
    p[i] = input("Ingrese nombre producto: ")
    c[i] = int(input("Ingrese cantidad stock: "))
    
def busqueda_producto(buscar,p,c,tamanio):
    idx= 0
    encontrado = False
    while idx < tamanio:
        if p[idx] == buscar:
            print(p[idx], c[idx])
            encontrado = True
        idx = idx + 1
        
    if encontrado == False:
        print("No encontrado")
    
while opMenu != 9:
    opMenu= menu()
    if opMenu == 1:
        #Alta
        alta_producto(producto, cantidad, i)
        i = i + 1
    elif opMenu == 2:
        #Busqueda
        buscar= input("Ingrese prod a buscar: ")
        busqueda_producto(buscar, producto, cantidad, max)
    elif opMenu == 3:
        #Modificar
        pass
    elif opMenu == 9:
        #Salir
        print("Hasta luego")
    else:
        print("Opción inválida")
    
    
    
    