# Vectores

# Como crear un vector
max = 3
edades = [-1] * max # opción vacío
# edades = [30,40,20,35,32] # opción con valores
nombres = [''] * max
# nombres = ['Mateo', 'Nicolas', 'Alberto', 'Juan', 'Alejandro']

# Guardar datos en el vector
edades[2] = 24

indice = 0
while indice < max:
    nombres[indice] = input("Ingrese nombre: ")    
    edades[indice] = int(input("Ingrese edad: "))
    indice = indice + 1

# Obtener un dato del vector
indice = 0
while indice < max:
    aImprimir= nombres[indice] + ":" + str(edades[indice])
    #print(nombres[indice], edades[indice])
    print(aImprimir, end=' | ')
    indice = indice + 1

