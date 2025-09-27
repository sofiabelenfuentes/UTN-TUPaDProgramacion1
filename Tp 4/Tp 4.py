# -------------------------------------------------
# Ejercicio 1: Imprimir números del 0 al 100
# -------------------------------------------------
for i in range(101):
    print(i)

# -------------------------------------------------
# Ejercicio 2: Contar dígitos de un número
# -------------------------------------------------
numero = input("Ingrese un número entero: ")
print("Cantidad de dígitos:", len(numero.strip('-')))

# -------------------------------------------------
# Ejercicio 3: Sumar números entre dos valores excluidos
# -------------------------------------------------
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("La suma es:", suma)

# -------------------------------------------------
# Ejercicio 4: Sumar números hasta que se ingrese 0
# -------------------------------------------------
total = 0
while True:
    num = int(input("Ingrese un número entero (0 para finalizar): "))
    if num == 0:
        break
    total += num
print("La suma total es:", total)

# -------------------------------------------------
# Ejercicio 5: Adivinar número aleatorio entre 0 y 9
# -------------------------------------------------
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto, intentá de nuevo.")

# -------------------------------------------------
# Ejercicio 6: Números pares de 100 a 0 en orden decreciente
# -------------------------------------------------
for i in range(100, -1, -2):
    print(i)

# -------------------------------------------------
# Ejercicio 7: Sumar números desde 0 hasta N
# -------------------------------------------------
n = int(input("Ingrese un número entero positivo: "))

if n < 0:
    print("Número no válido. Debe ser positivo.")
else:
    suma = sum(range(n + 1))
    print("La suma desde 0 hasta", n, "es:", suma)
# -------------------------------------------------
# Ejercicio 8: Contar pares, impares, positivos y negativos
# -------------------------------------------------
CANTIDAD_NUMEROS = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD_NUMEROS):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("\n--- Resultados ---")
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
# -------------------------------------------------
# Ejercicio 9: Calcular media de 100 números
# -------------------------------------------------
CANTIDAD_NUMEROS = 100  

suma = 0

for i in range(CANTIDAD_NUMEROS):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / CANTIDAD_NUMEROS
print("\nLa media de los", CANTIDAD_NUMEROS, "números es:", media)
# -------------------------------------------------
# Ejercicio 10: Invertir los dígitos de un número
# -------------------------------------------------
numero = input("Ingrese un número: ")

if numero[0] == '-':
    invertido = '-' + numero[:0:-1]
else:
    invertido = numero[::-1]

print("Número invertido:", invertido)
