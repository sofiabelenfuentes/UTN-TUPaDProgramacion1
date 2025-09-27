import random

def actividad_1():def actividad_7():
    # Temperaturas mínimas y máximas de 7 días (7x2)
    # Formato: [ [min, max], ... ]
    temperaturas = [
        [15, 25],
        [17, 28],
        [16, 26],
        [14, 24],
        [18, 30],
        [16, 27],
        [15, 29]
    ]

    suma_min = 0
    suma_max = 0
    amplitudes = []

    for i, (t_min, t_max) in enumerate(temperaturas):
        suma_min += t_min
        suma_max += t_max
        amplitudes.append(t_max - t_min)

    promedio_min = suma_min / len(temperaturas)
    promedio_max = suma_max / len(temperaturas)
    dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1

    print(f"\nPromedio temperaturas mínimas: {promedio_min:.2f}")
    print(f"Promedio temperaturas máximas: {promedio_max:.2f}")
    print(f"Mayor amplitud térmica se registró en el día: {dia_mayor_amplitud}")

def actividad_8():
    # Notas 5 estudiantes en 3 materias (5x3)
    notas = [
        [8, 7, 9],
        [6, 7, 5],
        [9, 9, 8],
        [7, 6, 7],
        [8, 8, 9]
    ]

    print("\nPromedio de cada estudiante:")
    for i, estudiante in enumerate(notas, start=1):
        promedio = sum(estudiante) / len(estudiante)
        print(f"Estudiante {i}: {promedio:.2f}")

    print("\nPromedio de cada materia:")
    for j in range(len(notas[0])):
        suma = sum(notas[i][j] for i in range(len(notas)))
        promedio = suma / len(notas)
        print(f"Materia {j+1}: {promedio:.2f}")

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def actividad_9():
    tablero = [["-" for _ in range(3)] for _ in range(3)]

    jugadores = ["X", "O"]
    turno = 0

    def jugada_valida(fila, col):
        return 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == "-"

    print("\nTablero inicial:")
    mostrar_tablero(tablero)

    while True:
        jugador = jugadores[turno % 2]
        print(f"Turno del jugador {jugador}")
        try:
            fila = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
        except ValueError:
            print("Ingrese valores numéricos válidos.")
            continue

        if not jugada_valida(fila, col):
            print("Movimiento inválido, intente nuevamente.")
            continue

        tablero[fila][col] = jugador
        mostrar_tablero(tablero)

        turno += 1
        # Opcional: podríamos agregar condición de ganador o empate para finalizar

        if turno == 9:
            print("Juego terminado. Tablero lleno.")
            break

def actividad_10():
    # Ventas de 4 productos durante 7 días (4x7)
    ventas = [
        [5, 3, 6, 7, 5, 2, 4],  # producto 1
        [3, 7, 2, 5, 6, 3, 8],  # producto 2
        [4, 4, 5, 6, 5, 7, 5],  # producto 3
        [6, 5, 7, 8, 6, 7, 6]   # producto 4
    ]

    print("\nTotal vendido por producto:")
    totales_productos = []
    for i, producto in enumerate(ventas, start=1):
        total = sum(producto)
        totales_productos.append(total)
        print(f"Producto {i}: {total}")

    totales_dias = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(7)]
    dia_mayor_venta = totales_dias.index(max(totales_dias)) + 1
    print(f"\nDía con mayores ventas totales: Día {dia_mayor_venta}")

    producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
    print(f"Producto más vendido en la semana: Producto {producto_mas_vendido}")

def main():
    while True:
        print("\nSeleccione una actividad para ejecutar:")
        print("7. Temperaturas mínimas y máximas")
        print("8. Notas de estudiantes en materias")
        print("9. Juego Ta-Te-Ti")
        print("10. Ventas de productos")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "7":
            actividad_7()
        elif opcion == "8":
            actividad_8()
        elif opcion == "9":
            actividad_9()
        elif opcion == "10":
            actividad_10()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

    notas = [7, 8.5, 6, 9, 10, 5, 7.5, 8, 6.5, 9.2]
    print("\nNotas de los estudiantes:")
    for nota in notas:
        print(nota)

    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")

    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")

def actividad_2():
    productos = []
    for i in range(5):
        producto = input(f"Ingrese el producto {i+1}: ")
        productos.append(producto)

    productos_ordenados = sorted(productos)
    print("\nProductos ordenados:")
    for p in productos_ordenados:
        print(p)

    producto_eliminar = input("Ingrese el producto que desea eliminar: ")
    if producto_eliminar in productos:
        productos.remove(producto_eliminar)
        print("Lista actualizada:")
        for p in productos:
            print(p)
    else:
        print("Producto no encontrado en la lista.")

def actividad_3():
    numeros = [random.randint(1, 100) for _ in range(15)]

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print("\nNúmeros generados:", numeros)
    print(f"Números pares ({len(pares)}): {pares}")
    print(f"Números impares ({len(impares)}): {impares}")

def actividad_4():
    lista_repetidos = [1, 2, 3, 2, 4, 5, 3, 6, 4, 7]
    lista_sin_repetidos = []
    for elemento in lista_repetidos:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)

    print("\nLista original:", lista_repetidos)
    print("Lista sin elementos repetidos:", lista_sin_repetidos)

def actividad_5():
    estudiantes = ["Ana", "Juan", "Luis", "Marta", "Sofia", "Carlos", "Elena", "Pedro"]
    print("\nEstudiantes actuales:")
    for e in estudiantes:
        print(e)

    accion = input("¿Desea agregar (a) o eliminar (e) un estudiante? (a/e): ").lower()

    if accion == "a":
        nuevo = input("Ingrese el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo)
    elif accion == "e":
        eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        if eliminar in estudiantes:
            estudiantes.remove(eliminar)
        else:
            print("Estudiante no encontrado.")
    else:
        print("Acción no válida.")

    print("Lista actualizada de estudiantes:")
    for e in estudiantes:
        print(e)

def actividad_6():
    numeros = [1, 2, 3, 4, 5, 6, 7]
    print("\nLista original:", numeros)

    ultimo = numeros[-1]
    for i in range(len(numeros) - 1, 0, -1):
        numeros[i] = numeros[i - 1]
    numeros[0] = ultimo

    print("Lista rotada a la derecha:")
    print(numeros)

def main():
    while True:
        print("\nSeleccione una actividad para ejecutar:")
        print("1. Notas de estudiantes")
        print("2. Lista de productos")
        print("3. Números aleatorios pares e impares")
        print("4. Lista sin elementos repetidos")
        print("5. Agregar o eliminar estudiante")
        print("6. Rotar lista a la derecha")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            actividad_1()
        elif opcion == "2":
            actividad_2()
        elif opcion == "3":
            actividad_3()
        elif opcion == "4":
            actividad_4()
        elif opcion == "5":
            actividad_5()
        elif opcion == "6":
            actividad_6()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
