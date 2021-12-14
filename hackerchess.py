# Funcion strip() ... elimina espacios delanteros y traseros de una cadena
import random
import os

def movimiento_ofensivo(r1, r2, jugador):
    # Busca una torre que se pueda avanzar.
    # Intentaremos avanzar el máximo posible -> Es un movimiento de ataque.

    columna_movimiento = 0
    jugada_encontrada = False
    while not jugada_encontrada and columna_movimiento < n:
        jugada_encontrada = (r2[columna_movimiento] -
                             r1[columna_movimiento]) > 1

        if jugada_encontrada:
            # Calcular nueva posición teniendo en cuenta el jugador que mueve pieza
            # Se trata de dejar la torre adyacente a la torre del contrario.
            if jugador == 1:
                r1[columna_movimiento] = r2[columna_movimiento] - 1
            else:
                r2[columna_movimiento] = r1[columna_movimiento] + 1

        else:
            # La torre no se puede mover hacia adelante así que vamos a intentar con otra pieza ...
            columna_movimiento = columna_movimiento + 1

    return jugada_encontrada, columna_movimiento

def movimiento_defensivo(r1, r2, jugador):
     # Busca una torre que se pueda mover hacia atras ya que no podemos avanzar

    columna_movimiento = 0
    jugada_encontrada = False
    while not jugada_encontrada and columna_movimiento < n:
        # Calcular nueva posición teniendo en cuenta el jugador que mueve pieza
        # Retrocedemos una casilla.
        if jugador == 1:
            jugada_encontrada = r1[columna_movimiento] > 0

            if jugada_encontrada:
                r1[columna_movimiento] = r1[columna_movimiento] - 1
        else:
            jugada_encontrada = r2[columna_movimiento] < (n-1)

            if jugada_encontrada:
                r2[columna_movimiento] = r2[columna_movimiento] + 1

        if not jugada_encontrada:
            # La torre no puede retrocer un paso
            columna_movimiento = columna_movimiento + 1

    return jugada_encontrada, columna_movimiento

def jugar(r1, r2, jugador):
    # Calcula el movimiento optimo que debe realizar un jugador.
    # Intenta buscar un movimiento de ataque que acorrale al contrario
    # y sino opta por uno defensivo, es decir retrocederemos posiciones.

    jugada_encontrada, columna_movimiento = movimiento_ofensivo(
        r1, r2, jugador)

    if not jugada_encontrada:
        jugada_encontrada, columna_movimiento = movimiento_defensivo(
            r1, r2, jugador)

    return jugada_encontrada, columna_movimiento

def pon_blancas(dim, r1):

def pon_negras(dim, r1, r2):

def verticalRooks(r1, r2):
    # Esta función es la que "juega" la partida y empieza el jugador 2 segun enunciado.

    fin_partida = False
    while not fin_partida:
        # Juega el jugador 2
        jugada_encontrada, columna_movimiento = jugar(r1, r2, 2)
        if not jugada_encontrada:
            resultado = "Gana el jugador " + "1"
            fin_partida = True      # ---> Partida finalizada

        # Juega el jugador 1
        jugada_encontrada, columna_movimiento = jugar(r1, r2, 1)
        if not jugada_encontrada:
            resultado = "GANA el jugador " + "2"
            fin_partida = True      # ---> Partida finalizada

    return resultado


#####
# Inicio programa
#####
# Abre un fichero para guardar los resultados
fptr = open("resultados.txt", 'w')

# "t" contiene el número de partidas a jugar
t = int(input('Leer número de partidas ').strip())

# "n" contiene el tamaño del tablero
n = int(input('Leer tamaño tablero ').strip())

# Este bucle realiza un iteración por partida
for num_partida in range(t):
    # "r1" contiene la posición (fila) de las torres del jugador 1
    r1 = []
    pon_blancas(n, r1)

    # "r2" contiene la posición (fila) de las torres del jugador 2
    r2 = []
    pon_negras(n, r1, r2)

    # Mostrar posición INICIAL de las torres
    print()
    print("* PARTIDA " + str(num_partida) + " *")
    print("  Inicial: Torres jugador 1", r1)
    print("  Inicial: Torres jugador 2", r2)

    # Jugar una partida -> Ambos jugadores son automáticos
    result = verticalRooks(r1, r2)

    # Mostrar posición FINAL de las torres
    print("  Final:   Torres jugador 1", r1)
    print("  Final:   Torres jugador 2", r2)
    print("  " +result)

    # Guardar los resultados de la partida en el archivo
    fptr.write("PARTIDA " + str(num_partida) + "\n")
    fptr.write("Final: Torres jugador 1" + str(r1) + "\n")
    fptr.write("Final: Torres jugador 2" + str(r2) + "\n")
    fptr.write(result + "\n\n")

# Cerrar el archivo antes de que el programa termine
fptr.close()
