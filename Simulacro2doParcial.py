# Simulacro 2do Parcial
import random
maximo = 20


def menu():
    print('1- Cantidad Productos Bazar')
    print('2- Modificar Precio Producto')
    print('3- Promedio Precio de Categoría')
    print('4- Producto menor stock Alimentos')
    print('5- Productos mas caros por categoría')
    print('9-Salir')
    return int(input('Ingrese la opción elegida: '))


def contar_productos_categoria(categorias, categoria):
    i = 0
    contador = 0
    while i < maximo:
        if categorias[i] == categoria:
            contador = contador + 1
        i = i + 1
    return contador


def buscar_producto(nombre_a_buscar, productos):
    i = 0
    while i < maximo:
        if productos[i] == nombre_a_buscar:
            return i
        i = i + 1
    return -1


def modificar_precio_producto(nombre_a_buscar, precio, productos, precios):
    i = buscar_producto(nombre_a_buscar, productos)
    if i == -1:
        print("Producto no encontrado")
    else:
        precios[i] = precio


def calcular_promedio_precios_categoria(categoria, categorias, precios):
    i = 0
    contador = 0
    acumulador = 0
    while i < maximo:
        if categorias[i] == categoria:
            contador = contador + 1
            acumulador = acumulador + precios[i]
        i = i + 1
    return acumulador/contador


def buscar_menor_stock_categoria(categoria, categorias, cantidades):
    i = 0
    es_primer_elemento= True
    menor= 0
    menor_i= 0
    while i < maximo:
        if categorias[i] == categoria:
            if es_primer_elemento:
                menor= cantidades[i]
                menor_i= i
                es_primer_elemento= False
            if cantidades[i] < menor:
                menor = cantidades[i]
                menor_i= i
    
        i = i + 1
    return menor_i


def buscar_producto_mas_caro_categoria(categoria, categorias, precios):
    i = 0
    es_primer_elemento= True
    mayor= 0
    mayor_i= 0
    while i < maximo:
        if categorias[i] == categoria:
            if es_primer_elemento:
                mayor= precios[i]
                mayor_i= i
                es_primer_elemento= False
            if precios[i] > mayor:
                mayor = precios[i]
                mayor_i= i
        i = i + 1
    return mayor_i


def texto_categorias(cat):
    if cat == 1:
        return "Limpieza"
    elif cat == 2:
        return "Alimentos"
    elif cat == 3:
        return "Bazar"
    else:
        return "Codigo Inválido"


def mostrar_productos_mas_caros(productos, categorias, precios):
    cat = 1
    while cat <= 3:
        i = buscar_producto_mas_caro_categoria(cat, categorias, precios)
        print("El producto más caro de la categoría " + texto_categorias(cat) + " es: ", productos[i])
        cat = cat + 1



def main():
    productos = [''] * maximo
    categorias = [0] * maximo
    precios = [0] * maximo
    cantidades = [0] * maximo

    i = 0
    while i < maximo:
        productos[i]= "producto" + str(i)
        categorias[i]= random.randint(1,3)
        precios[i]= random.randint(1,1000)
        cantidades[i]= random.randint(1,100)
        i = i + 1

    opcion = 0
    while opcion != 9:
        opcion = menu()
        if opcion == 1:
            cantidad = contar_productos_categoria(categorias, 3)
            print("Cantidad de productos de BAZAR: ", cantidad)
        elif opcion == 2:
            nombre_a_buscar = input("Ingrese nombre a buscar: ")
            precio = int(input("Ingrese precio: "))
            modificar_precio_producto(nombre_a_buscar, precio, productos, precios)
        elif opcion == 3:
            categoria= int(input("Ingrese categoría: "))
            promedio = calcular_promedio_precios_categoria(categoria, categorias, precios)
            print("Promedio de precios de la categoría seleccionada: ", promedio)
        elif opcion == 4:
            i = buscar_menor_stock_categoria(2, categorias, cantidades)
            print("Producto con menor stock categoría Alimentos: ")
            print("Producto: ", productos[i])
            print("Categoria: ", categorias[i])
            print("Precio: ", precios[i])
            print("Cantidad: ", cantidades[i])
        elif opcion == 5:
            mostrar_productos_mas_caros(productos, categorias, precios)
        elif opcion == 9:
            print("Hasta luego")
            
    print(productos)
    print(categorias)
    print(precios)
    print(cantidades)
    
    
main()    