# 1er Parcial

# Solicitar al usuario un número. Informar por pantalla si el número ingresado es par.
# Continuar solicitando el ingreso de números e informando por pantalla hasta que
# el usuario ingrese -1.

# x % 2 == 0
# while mientras no sea -1 la eleccion del usuario
"""
numero = 0
while numero != -1:
    numero = int(input("Ingrese un número: "))
    if numero != -1:    
        if numero % 2 == 0:
            # El número es par
            print("El número es par")
        else:
            print("El número es impar")
"""
# Solicitar al usuario un número. Informar por pantalla si el número ingresado es
# múltiplo de 3. Continuar solicitando el ingreso de números e informando por pantalla
# hasta que el usuario ingrese -1.
"""
numero = 0
while numero != -1:
    numero = int(input("Ingrese un número: "))
    if numero != -1:    
        if numero % 3 == 0:
            print("El número es múltiplo de 3")
        else:
            print("El número no es múltiplo de 3")
"""
# Solicitar al usuario un número. Informar por pantalla si el número ingresado es negativo.
# Continuar solicitando el ingreso de números e informando por pantalla hasta que el
# usuario ingrese 0.
"""
numero = -1
while numero != 0:
    numero = int(input("Ingrese un número: "))
    if numero != 0:    
        if numero < 0:
            print("El número es negativo")
        else:
            print("El número no es negativo")
"""

"""
Solicite al usuario la temperatura. En base a la temperatura ingresada indicar por pantalla
si es un día “caluroso”, “templado” o “frío” en base a los siguientes criterios:
-   Caluroso: más de 25 grados
-   Templado: entre 15 y 25 grados
-   Frío: menos de 15 grados
"""
"""
temperatura = 0
temperatura = int(input("Ingrese temperatura: "))
if temperatura < 15:
    print("Frio")
else:
    if temperatura > 25:
        print("Caluroso")
    else:
        print("Templado")
"""

"""
Solicitar al usuario una hora (solo hora, sin minutos, en formato 24hs).
En base a la hora ingresada informar por pantalla si es de mañana, tarde o noche
según el siguiente criterio:
-   Mañana: hora menor a 13
-   Tarde: hora entre las 13 y las 20
-   Noche: hora mayor a 20
"""
"""
hora = int(input("Ingrese hora:"))
if hora < 13:
    print("Mañana")
else:
    if hora >= 13 and hora <= 20:
        print("Tarde")
    else:
        print("Noche")
"""

"""
Solicitar al usuario que ingrese su estado
(1- Hambriento, 2- Cansado, 3- Aburrido).
En base a la opción ingresada proponerle al usuario que hacer según el siguiente criterio:
-   Hambriento: Decirle que coma
-   Cansado: pedirle que duerma
-   Aburrido: proponerle jugar
"""
"""
hambriento = 1
cansado = 2
aburrido = 3

estado= int(input("Ingresar estado [1-Hambriento/2-Cansado/3-Aburrido]:"))
if estado == hambriento:
    print("Comer")
elif estado == cansado:
    print("Dormir")
elif estado == aburrido:
    print("Jugar")
else:
    print("La opcion no es válida")
"""

"""
Solicitar al usuario dos números, el primero que representa el mes y el segundo el año.
Verificar si es una fecha válida, teniendo en cuenta que los meses tienen que estar
entre 1 y 12, y el año entre 1900 y 2100.
Indicar por pantalla si el par ingresado es válido o inválido, sin importar si es el mes
o el año el incorrecto.
"""
"""
mes = int(input("Ingrese el mes:"))
anio = int(input("Ingrese el año:"))
"""
"""
if mes >= 1:
    if mes <= 12:
        if anio >= 1900:
            if anio <= 2100:
                print("Fecha válida")
            else:
                print("Fecha inválida")
        else:
            print("Fecha inválida")
    else:
        print("Fecha inválida")
else:
    print("Fecha inválida")
"""
"""
if mes >= 1 and mes <= 12:
    if anio >= 1900 and anio <= 2100:
        print("Fecha válida")
    else:
        print("Fecha inválida")
else:
    print("Fecha inválida")
"""
"""
if mes >= 1 and mes <= 12 and anio >= 1900 and anio <=2100:
    print("Fecha válida")
else:
    print("Fecha inválida")
"""

"""
Solicitar al usuario dos números, el primero representa la hora y el segundo los minutos.
Verificar si es una hora válida, teniendo en cuenta que las horas tienen que estar
entre 0 y 23 y los minutos entre 0 y 59. Indicar por pantalla si el par ingresado
es válido o inválido, sin importar si es la hora o son los minutos los incorrectos.
"""
"""
hora= int(input("Ingrese hora:"))
minutos= int(input("Ingrese minutos:"))
if hora >=0 and hora <=23 and minutos >= 0 and minutos <= 59:
    print("Hora válida")
else:
    print("Hora inválida")
"""

"""
Solicitar al usuario dos números, el primero representa la edad y el segundo la antigüedad
en la empresa de un empleado. Verificar que los datos sean válidos sabiendo que la edad
de los empleados tiene que estar entre 18 y 65 años, y la antigüedad entre 0 y 10 años.
"""
"""
edad= int(input("Ingrese Edad: "))
antiguedad= int(input("Ingrese antigüedad))
if edad >= 18 and edad <= 65 and antiguedad >= 0 and antiguedad <= 10:
    print("Datos válidos")
else:
    print("Datos inválidos")
"""

"""
Solicitar al usuario 20 números. Al finalizar indicar por pantalla la suma de los números
ingresados que son múltiplos de 5.
"""
"""
vuelta = 0
suma = 0
while vuelta < 20:
    numero= int(input("Ingrese un número: "))

    if numero % 5 == 0:
        suma = suma + numero
    
    vuelta = vuelta + 1

print("Suma: ", suma)
"""

"""
Solicitar al usuario 20 números. Al finalizar informar por pantalla la cantidad de números
ingresados que son múltiplos de 6.
"""
"""
vuelta = 0
cantidad = 0
while vuelta < 20:
    numero= int(input("Ingrese un número: "))

    if numero % 6 == 0:
        cantidad = cantidad + 1
    
    vuelta = vuelta + 1

print("Cantidad: ", cantidad)
"""

"""
Solicitar al usuario 20 números. Al finalizar informar por pantalla el promedio de los números
ingresados que son pares.
"""
"""
vuelta = 0
cantidad = 0
suma = 0
while vuelta < 20:
    numero= int(input("Ingrese un número: "))

    if numero % 2 == 0:
        suma = suma + numero
        cantidad = cantidad + 1
    
    vuelta = vuelta + 1

print("Promedio: ", suma/cantidad)
"""

"""
Le solicitan desarrolle una aplicación para una empresa de logística. El sistema primero
deberá solicitar al usuario la cantidad de paquetes a enviar. Luego solicitar para cada
paquete el peso, volumen (cm3) y distancia expresada en kilómetros hasta el destino.

En base a los datos ingresados del paquete, se deberá calcular el importe a cobrar,
que se calculará de la siguiente manera: 
importe = 200 + peso * 10 + volumen * 2 + importe por kilómetros
y el importe por kilómetros es:
-   Menos de 60km: $100
-   Entre 60 km y 500 km: $300
-   Más de 500km: $500

Una vez calculado el importe, informar por pantalla al usuario y solicitar los datos
del próximo paquete.

Al finalizar la carga de todos los paquetes informar por pantalla
la suma de todos los importes calculados.
"""
"""
# Entradas
CantidadPaquetes
Por cada paquete:
-Peso
-Volumen
-Distancia

# Salidas
ImportePaquete
ImporteTotal
"""
"""
importeTotal = 0
importePaquete= 0

cantidadPaquetes = int(input("Ingrese Cantidad de paquetes"))

vuelta = 0
while vuelta < cantidadPaquetes:
    peso = int(input("Ingrese Peso: "))
    volumen = int(input("Ingrese Volumen: "))
    distancia= int(input("Ingrese Distancia: "))

    # Calculo
    
    importeKilometros= 0

    if distancia < 60:
        importeKilometros= 100
    else:
        if distancia > 500:
            importeKilometros= 500
        else:
            importeKilometros= 300
    
    importePaquete = 200 + peso * 10 + volumen * 2 + importeKilometros
    print("Importe paquete: ", importePaquete)
    importeTotal = importeTotal + importePaquete
    vuelta = vuelta + 1
    
print("Importe total: ", importeTotal)
"""

"""
importe = 100 + importe por peso o volumen + kilómetros * 70
y el importe por peso o volumen es:
-   Importe peso = peso * 10
-   Importe volumen = volumen * 2
-   De ambos importes tomar el mayor de los dos.
"""
"""
importeTotal = 0
importePaquete= 0

cantidadPaquetes = int(input("Ingrese Cantidad de paquetes"))

vuelta = 0
while vuelta < cantidadPaquetes:
    peso = int(input("Ingrese Peso: "))
    volumen = int(input("Ingrese Volumen: "))
    distancia= int(input("Ingrese Distancia: "))

    # Calculo
    
    importePesoVolumen= 0

    if peso * 10 > volumen * 2:
        importePesoVolumen= peso * 10
    else:
        importePesoVolumen= volumen * 2
    
    importePaquete = 100 + importePesoVolumen + distancia * 70

    print("Importe paquete: ", importePaquete)
    importeTotal = importeTotal + importePaquete
    vuelta = vuelta + 1
    
print("Importe total: ", importeTotal)
"""

"""
importe = Importe por kilómetros + peso * 10 + volumen * 2
y el importe por kilómetros es:
-   Menos de 100km: $300
-   Entre 100 km y 500 km: $500
-   Más de 500km: $1000
"""
importeTotal = 0
importePaquete= 0

cantidadPaquetes = int(input("Ingrese Cantidad de paquetes"))

vuelta = 0
while vuelta < cantidadPaquetes:
    peso = int(input("Ingrese Peso: "))
    volumen = int(input("Ingrese Volumen: "))
    distancia= int(input("Ingrese Distancia: "))

    # Calculo
    importeKilometros = 0

    if distancia < 100:
        importeKilometros= 300
    elif distancia > 500:
        importeKilometros= 1000
    else
        importeKilometros= 500

    importePaquete = importeKilometros + peso * 10 + volumen * 2

    print("Importe paquete: ", importePaquete)
    importeTotal = importeTotal + importePaquete
    vuelta = vuelta + 1
    
print("Importe total: ", importeTotal)
