




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
