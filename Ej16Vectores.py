# Ejercicio 16
import random

maximo = 10
codigos = [0] * maximo
nombres = [''] * maximo
tipos_siembra = [0] * maximo
tipos_riego = [0] * maximo
tipos_verdura = [0] * maximo
tipos_vertura_texto = ['', 'Bulbo','Raiz','Tallo y Hoja','Fruto']

def ingresar_numero(mensaje, mensaje_error, valor_minimo, valor_maximo):
    while True:
        v = int(input(mensaje))
        if v < valor_minimo or v > valor_maximo:
            print(mensaje_error)
        else:
            return v

def cantidad_raiz_almacigo(tipos_siembra, tipos_verdura, maximo):
    cantidad = 0
    idx = 0
    while idx < maximo:
        if tipos_siembra[idx] == 2 and tipos_verdura[idx] == 2:
            cantidad = cantidad + 1
        
        idx = idx + 1
    return cantidad
    
def tipos_verdura_riego_frecuente(tipos_verdura, tipos_riego, maximo):
    tipos= ['O'] * 4
    
    idx = 0
    while idx < maximo:
        if tipos_riego[idx] == 3:
            tipos[tipos_verdura[idx] - 1] = 'X'
                
        idx = idx + 1
    
    idx2 = 0
    while idx2 < 4:
        if tipos[idx2] == 'X':
            print("Tipo Riego: ", tipos_vertura_texto[idx2 + 1])
        idx2 = idx2 + 1
    
def listar_plantas_fruto_poca_frecuencia(nombres, tipos_verdura, tipos_riego, maximo):
    
    i= 0
    while i < maximo:
        if tipos_verdura[i] == 4 and tipos_riego[i] == 1:
            print(nombres[i])
        
        i = i + 1

    
    
i = 0
while i < maximo:
    # codigos[i] = ingresar_numero("Ingrese código de Planta: ", "Debe ingresar un código entre 100 y 999", 100, 999)
    # nombres[i] = input("Ingrese nombre de la Planta: ")
    # tipos_siembra[i] = ingresar_numero("Ingrese tipo de siembra: [1-Directo | 2-Almácigo]", "Debe ingresar un tipo válido", 1,2)
    # tipos_riego[i] = ingresar_numero("Ingrese tipo de riego: [1-Poco Frecuente | 2-Frecuente | 3-Muy Frecuente]", "Debe ingresar un tipo válido", 1,3)
    # tipos_verdura[i] = ingresar_numero("Ingrese tipo de verdura: [1-bulbo | 2-raiz | 3-tallo y hoja | 4-fruto]", "Debe ingresar un tipo válido", 1,4)
    codigos[i] = random.randint(100, 999)
    nombres[i] = "Planta" + str(i) 
    tipos_siembra[i] = random.randint(1,2)
    tipos_riego[i] = random.randint(1,3)
    tipos_verdura[i] = random.randint(1,4)

    i = i + 1
    

print("Cantidad Raiz Almácigo: ", cantidad_raiz_almacigo(tipos_siembra, tipos_verdura, maximo))
tipos_verdura_riego_frecuente(tipos_verdura, tipos_riego, maximo)
listar_plantas_fruto_poca_frecuencia(nombres, tipos_verdura, tipos_riego, maximo)
    
    
