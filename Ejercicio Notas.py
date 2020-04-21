# Ejercicio Notas

nota1 = 0

while nota1 != -1:
    # Entradas
    nota1 = int(input("Ingrese Nota 1:"))
    if nota1 != -1:    
        nota2 = int(input("Ingrese Nota 2:"))

        # Proceso
        estado = ""

        if nota1 >= 7:
            if nota2 >=7:
                estado= "Promociona"
            else:
                if nota2 >= 4:
                    estado= "Aprobado"
                else:
                    estado= "Recupera 2do"
        else:
            if nota1 >= 4:
                if nota2 >= 4:
                    estado= "Aprobado"
                else:
                    estado= "Recupera 2do"
            else:
                if nota2 >= 4:
                    estado= "Recupera 1ro"
                else:
                    estado= "Recursa"


        """
        if nota1 >= 7 and nota2 >= 7:
            estado= "Promociona"
        elif nota1 >= 4 and nota2 >= 4:
            estado= "Aprobado"
        elif nota1 < 4 and nota2 >= 4:
            estado= "Recupera 1er Parcial"
        elif nota2 < 4 and nota1 >= 4:
            estado= "Recupera 2do Parcial"
        else
            # nota1 < 4 & nota2 < 4
            estado = "Recursa"
        """

        """
        elif nota1 < 4 and nota2 < 4:
            estado= "Recursa"
        """ 

        # Salida
        print("Estado:",estado)

print("Chau")