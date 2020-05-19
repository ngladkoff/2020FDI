import random
# Funciones

def menu():
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Potencia")
    print("5-Salir")
    op= int(input("Ingrese opción: "))
    return op
    
def sumar(par1,par2):
    return par1 + par2

def restar(nro1,nro2):
    return nro1 - nro2

def multiplicar(nro1, nro2):
    i= 0
    calculo= 0
    while i < nro2:
        calculo= sumar(calculo, nro1)
        i= i + 1 
    return calculo

def calculadora(op, nro1, nro2):
    if op == 1:
        return sumar(nro1,nro2)
    elif op == 2:
        return restar(nro1, nro2)
    elif op == 3:
        return multiplicar(nro1,nro2)
    
menuSeleccionado= menu()
"""
if menuSeleccionado == 1:
    #Sumar
    primerValor= int(input("Ing 1er valor: "))
    resultado = sumar(primerValor, primerValor * 3)
    print ("Resultado: ", resultado)

elif menuSeleccionado == 2:
    #Restar
    a= 0
elif menuSeleccionado == 3:
    #Multiplicar
    a= 10
    b= 3
    resultado = multiplicar(a,b)
    print ("Resultado: ", resultado)    
"""
n1= int(input("Ingrese nro1: "))
n2= int(input("Ingrese nro2: "))
print("Resultado: ", calculadora(menuSeleccionado, n1, n2))
