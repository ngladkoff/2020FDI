# Ejercicio Piedra-Papel-Tijera
import random

puntoRondaJugador = 0
puntoRondaMaquina = 0

while puntoRondaJugador < 3 and puntoRondaMaquina < 3:

    puntosJugador= 0
    puntosMaquina= 0

    while puntosJugador<2 and puntosMaquina<2:

        ## Eleccion de Jugadores
        print("Seleccione 1-Piedra / 2-Papel / 3-Tijera")
        eleccionJugador = int(input("Opción: "))
        eleccionMaquina = random.randint(1,3)

        ## Definir un Ganador
        if eleccionJugador == 1:
            if eleccionMaquina == 1:
                print("Empate")
            else:
                if eleccionMaquina == 2:
                    print("Gana la maquina")
                    puntosMaquina = puntosMaquina + 1
                else:
                    print("Gano!!!")
                    puntosJugador = puntosJugador + 1
        else:
            if eleccionJugador == 2:
                if eleccionMaquina == 1:
                    print("Gano!!!")
                    puntosJugador = puntosJugador + 1
                else:
                    if eleccionMaquina == 2:
                        print("Empate")
                    else:
                        print("Gana la maquina")
                        puntosMaquina = puntosMaquina + 1
            else:
                if eleccionMaquina == 1:
                    print("Gana la maquina")
                    puntosMaquina = puntosMaquina + 1
                else:
                    if eleccionMaquina == 2:
                        print("Gano!!!")
                        puntosJugador = puntosJugador + 1
                    else:
                        print("Empate")
                        
        # FIN ELECCION GANADOR
    #FIN DEL WHILE JUEGOS
    if puntosJugador > puntosMaquina:
        print("Ganó la ronda el jugador")
        puntoRondaJugador = puntoRondaJugador + 1
    else:
        print("Ganó la ronda la maquina")
        puntoRondaMaquina = puntoRondaMaquina + 1
    
#FIN DEL WHILE RONDAS

if puntoRondaJugador > puntoRondaMaquina:
    print("Ganó la partida el jugador")
else:
    print("Ganó la partida la maquina")
    
    
            
        
