# Segundo parcial
# Tema 2
import random

MAX = 10

opcion = 0

generos = [0] * MAX
artistas = [""] * MAX
titulos = [""] * MAX
duraciones = [0] * MAX

i = 0
while  i < MAX:
    generos[i] = random.randint(1,4)
    artistas[i] = "Artista" + str(random.randint(1,3))
    titulos[i] = "Titulo" + str(i)
    duraciones[i] = random.randint(100, 300)
    i = i + 1
    
def menu():
    print("1- Canciones por Artista")
    print("2- Duración  y cantidad de canciones por Genero")
    print("3- Canción de mayor duración")
    print("4- Promedio duración canciones por genero")
    print("5- Buscar canción por Título")
    print("9- Salir")
    op = int(input("Ingrese opción: "))
    return op


def mostrar_canciones_por_artista(artistas,titulos):
    artista = input("Nombre del artista: ")
    
    i = 0
    while i < MAX:
        if artistas[i] == artista:
            print(titulos[i])
                    
        i = i +1


def mostrar_cantidad_duracion_por_genero(generos, duraciones):
    genero = int(input("Ingrese genero: "))
    genero = 0
    cantidad_canciones= 0
    duracion_acc= 0
    i = 0
    while i < MAX:
        if generos[i] == genero:
            cantidad_canciones= cantidad_canciones + 1
            duracion_acc= duracion_acc + duraciones[i]
        i = i + 1
    
    if cantidad_canciones == 0:
        print("No se encontraron canciones para el género seleccionado")
    else:
        print("Cantidad: ", cantidad_canciones)
        print("Duracion Acc.: ", duracion_acc)
    

def mostrar_cancion_mayor_duracion(titulos, duraciones):
    i_mayor= 0
    i = 0
    while i < MAX:
        if duraciones[i] > duraciones[i_mayor]:
            i_mayor = i
        
        i = i + 1
    
    print(titulos[i_mayor])
    
    
def mostrar_promedio_canciones_generos(generos, duraciones):
    
    duracion_rock= 0
    cantidad_rock= 0
    duracion_pop= 0
    cantidad_pop= 0
    duracion_latina= 0
    cantidad_latina= 0
    duracion_cumbia= 0
    cantidad_cumbia= 0
    
    i = 0
    while i < MAX:
        if generos[i] == 1:
            duracion_rock = duracion_rock + duraciones[i]
            cantidad_rock = cantidad_rock + 1
        if generos[i] == 2:
            duracion_pop = duracion_pop + duraciones[i]
            cantidad_pop = cantidad_pop + 1
        if generos[i] == 3:
            duracion_latina = duracion_latina + duraciones[i]
            cantidad_latina = cantidad_latina + 1
        if generos[i] == 4:
            duracion_cumbia = duracion_cumbia + duraciones[i]
            cantidad_cumbia = cantidad_cumbia + 1
               
        i = i + 1

    print("Rock cantidad: ", cantidad_rock)
    print("Rock duracion acc.: ", duracion_rock)
    print("Pop cantidad: ", cantidad_pop)
    print("Pop duracion acc.: ", duracion_pop)
    print("Latina cantidad: ", cantidad_latina)
    print("Latina duracion acc.: ", duracion_latina)
    print("Cumbia cantidad: ", cantidad_cumbia)
    print("Cumbia duracion acc.: ", duracion_cumbia)


def convertir_genero_texto(genero):
    if genero == 1:
        return "Rock"
    elif genero == 2:
        return "Pop"
    elif genero == 3:
        return "Latina"
    elif genero == 4:
        return "Cumbia"
    else:
        return "Genero no existente"
    


def mostrar_cancion(generos,artistas,titulos):
    titulo = input("Titulo de la canción: ")
    encontrado = False
    
    i = 0
    while i < MAX:
        if titulos[i] == titulo:
            print("Titulo: ", titulos[i])
            nombre_genero= convertir_genero_texto(generos[i])
            print("Genero: ", nombre_genero)
            print("Artista: ", artistas[i])
            encontrado = True
        i = i + 1
    if encontrado == False:
        print("Titulo no encontrado")


while opcion != 9:
    opcion = menu()
    if opcion == 1:
        a= mostrar_canciones_por_artista(artistas,titulos)
    elif opcion == 2:
        mostrar_cantidad_duracion_por_genero(generos, duraciones)
    elif opcion == 3:
        mostrar_cancion_mayor_duracion(titulos, duraciones)
    elif opcion == 4:
        mostrar_promedio_canciones_generos(generos, duraciones)
    elif opcion == 5:
        mostrar_cancion(generos,artistas,titulos)
    elif opcion == 9:
        print ("Chau!")
    else:
        print("Opción Incorrecta")









"""
# Tema 1


def mostrar_canciones_x_genero(titulos,generos,artistas):
    print("Mostrar Canciones por Género")
    genero = int(input("Seleccione un género: "))
    i = 0
    while i < MAX:
        if generos[i] == genero:
            print(artistas[i], titulos[i])
        
        i = i + 1
    
def mostrar_duracion_promedio_canciones_artista(artistas, duraciones):
    print("Mostrar Duración Promedio Canciones de Artista")
    artista = input("Ingrese nombre de Artista: ")
    i = 0
    duracion_acumulada = 0
    cantidad_canciones = 0
    while i < MAX:
        if artistas[i] == artista:
            cantidad_canciones = cantidad_canciones + 1
            duracion_acumulada = duracion_acumulada + duraciones[i]
        i = i + 1
   
    if cantidad_canciones == 0:
        print("Artista no encontrado")
    else:
        print("Promedio duración: ", duracion_acumulada//cantidad_canciones)


def mostrar_titulo_cancion_menor_duracion_opcion2(titulos, duraciones, generos, artistas):
    i_menor_duracion = 0
    i = 0
    while i < MAX:
        if duraciones[i] < duraciones[i_menor_duracion]:    
            i_menor_duracion = i
        i = i + 1

    print("Titulo menor duración: ", titulos[i_menor_duracion])
    print("Genero menor duración: ", generos[i_menor_duracion])
    print("Duracion: ", duraciones[i_menor_duracion])
    print("Artista: ", artistas[i_menor_duracion])


def mostrar_titulo_cancion_menor_duracion(titulos, duraciones):
    menor_duracion = duraciones[0]
    titulo_menor_duracion = titulos[0]
    i = 0
    while i < MAX:
        if duraciones[i] < menor_duracion:    
            menor_duracion = duraciones[i]
            titulo_menor_duracion = titulos[i]
        i = i + 1

    print("Titulo menor duración: ", titulo_menor_duracion)


def mostrar_cantidad_canciones_generos(titulos,generos,artistas, duraciones):
    cantidad = [0] * 5
    duracion_acc = [0] * 5
    i = 0
    genero = 0
    
    while i < MAX:
        genero = 1
        while genero < 5:
            if generos[i] == genero:
                cantidad[genero] = cantidad[genero] + 1
                duracion_acc[genero] = duracion_acc[genero] + duraciones[i]
            genero = genero + 1
        
        i = i + 1

    print("Rock: ", cantidad[1])
    print("Pop: ", cantidad[2])
    print("Latina: ", cantidad[3])
    print("Cumbia: ", cantidad[4])


def mostrar_cantidad_canciones_generos_opcion2(titulos,generos,artistas):
    cantidad_rock = 0
    cantidad_pop = 0
    cantidad_latina = 0
    cantidad_cumbia = 0
    
    i = 0
    
    while i < MAX:
        if generos[i] == 1:
            cantidad_rock = cantidad_rock + 1

        if generos[i] == 2:
            cantidad_pop = cantidad_pop + 1

        if generos[i] == 3:
            cantidad_latina = cantidad_latina + 1

        if generos[i] == 4:
            cantidad_cumbia = cantidad_cumbia + 1

        i = i + 1

    print("Rock: ", cantidad_rock)
    print("Pop: ", cantidad_pop)
    print("Latina: ", cantidad_latina)
    print("Cumbia: ", cantidad_cumbia)


def buscar_cancion(a_buscar, titulos):
    i = 0
    while i < MAX:
        if titulos[i] == a_buscar:
            return i
        i = i + 1
    return -1

def mostrar_datos_cancion(titulos,generos,artistas,duraciones):
    titulo = input("Ingrese el título de la canción: ")
    i = buscar_cancion(titulo, titulos)
    if i == -1:
        print("Canción no encontrada")
    else:
        print(titulos[i], generos[i], artistas[i], duraciones[i])
        
    
while opcion != 9:
    opcion = menu()
    if opcion == 1:
        mostrar_canciones_x_genero(titulos,generos,artistas)
    elif opcion == 2:
        mostrar_duracion_promedio_canciones_artista(artistas, duraciones)
    elif opcion == 3:
        mostrar_titulo_cancion_menor_duracion(titulos, duraciones)
    elif opcion == 4:
        mostrar_cantidad_canciones_generos(titulos,generos,artistas)
    elif opcion == 5:
        mostrar_datos_cancion(titulos,generos,artistas,duraciones)
    elif opcion == 9:
        print ("Chau!")
    else:
        print("Opción Incorrecta")

"""