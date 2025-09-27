# ---------------------------
# Ejercicio 1: Mayor de edad
# ---------------------------
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
# ---------------------------
# Ejercicio 2: Nota aprobada
# ---------------------------
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# ---------------------------
# Ejercicio 3: Número par
# ---------------------------
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
# -------------------------------------
# Ejercicio 4: Clasificación por edad
# -------------------------------------
edad = int(input("Ingrese su edad nuevamente: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
# -------------------------------
# Ejercicio 5: Verificación de contraseña
# -------------------------------
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# -------------------------------------------------
# Ejercicio 6: Sesgo en distribución de números aleatorios
# -------------------------------------------------
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar los resultados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Evaluar tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución sin sesgo claro")
# -------------------------------------------------
# Ejercicio 7: Añadir signo de exclamación si termina en vocal
# -------------------------------------------------
texto = input("Ingrese una palabra o frase: ")

# Verificamos la última letra (ignorando espacios)
ultima_letra = texto.strip()[-1].lower()

if ultima_letra in 'aeiou':
    texto += "!"
    print("Resultado:", texto)
else:
    print("Resultado:", texto)
# -------------------------------------------------
# Ejercicio 8: Transformar nombre según opción
# -------------------------------------------------
nombre = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con primera letra mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida.")
# -------------------------------------------------
# Ejercicio 9: Clasificación de un terremoto
# -------------------------------------------------
magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
# -------------------------------------------------
# Ejercicio 10: Determinar estación según fecha y hemisferio
# -------------------------------------------------

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes actual (1-12): "))
dia = int(input("Ingrese el día del mes actual (1-31): "))

# Convertimos fecha en un número tipo MMDD para comparar más fácilmente
fecha = mes * 100 + dia

# Definir estación según rango de fechas y hemisferio
if 321 <= fecha <= 620:
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif 621 <= fecha <= 920:
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif 921 <= fecha <= 1220:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    # Esto cubre desde 21/12 a 20/03 (incluye fechas desde 1221 a 1231 y de 101 a 320)
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

# Determinar estación final según hemisferio
if hemisferio == "N":
    print("Estás en el hemisferio norte. La estación es:", estacion_norte)
elif hemisferio == "S":
    print("Estás en el hemisferio sur. La estación es:", estacion_sur)
else:
    print("Hemisferio no válido. Ingrese N o S.")
