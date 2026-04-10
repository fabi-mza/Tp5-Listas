# Ejercicio 1
# Crear una lista con las notas de 10 estudiantes
# Se muestra la lista completa
notas = [9, 6, 7, 3, 10, 8, 8, 9, 7, 7]
print("La lista de notas: ")
for nota in notas:
    print(nota, end=" ")
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"El promedio del curso es: {promedio}") #Se muestra el promedio del curso

# Indica nota más alta y la más baja
nota_alta = notas[0]
nota_baja = notas[0]

for nota in notas:
    if nota > nota_alta:
        nota_alta = nota
    if nota < nota_baja:
        nota_baja = nota
print(f"La nota más alta es: {nota_alta}.")
print(f"La nota más baja es: {nota_baja}.")


# Ejercicio 2
# Pedir al usuario que cargue 5 productos en una lista
productos = []
print("Ingresar 5 productos: ")
for i in range(5):
    item = input(f"Producto: {i+1}")
    productos.append(item)
lista_ordenada = sorted(productos)
print("Lista de productos ordenada alfabeticamente: ")
for p in lista_ordenada:
    print(f"- {p}.")
eliminar = input("¿Qué producto desea eliminar de la lista?: ")
if eliminar in productos:
    productos.remove(eliminar)
    print(f"El producto {eliminar} ha sido eliminado del listado.")
else:
    print(f"El producto {eliminar} no se encontraba en el listado.")
print(f"Lista de productos actualizada: ")
for p in productos:
    print(f"- {p}.")


# Ejercicio 3
# Generar una lista con 15 números enteros al azar entre 1 y 100

import random
num_azar = []
for i in range(15):
    num_azar.append(random.randint(1, 100))

# Listas par e impar
par = []
impar = []
for num in num_azar:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

# Se muestra los números de cada listado        
print(f"Lista original: {num_azar}")
print(f"Cantidad de números pares: {len(par)}")
print(f"El listado de números pares: {par}")
print(f"Cantidad de números impares: {len(impar)}")
print(f"El listado de números impares: {impar}")


# Ejercicio 4
# Dada una lista con valores repetidos:

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Lista sin números repetidos
sin_repetidos = []
for num in datos:
    if num not in sin_repetidos:
        sin_repetidos.append(num)

# Se muestra el resultado
print(f"Listado original: {datos}")
print(f"Listado sin números repetidos: {sin_repetidos}")


# Ejercicio 5
# Crear una lista con los nombres de 8 estudiantes presentes en clase

estudiantes = ["Ana", "Juan", "Pedro", "Pablo", "Sofia", "Marta", "Mia", "Hugo"]
print(f"Listado de estudiantes: {estudiantes}")

# Elección del usuario
accion = input("¿Desea agregar (A) o eliminar (E) algún alumno?: ").upper()
if accion == "A":
    nuevo = input("Agrega el nombre del estudiante: ").capitalize()
    estudiantes.append(nuevo)
    print(f"Se ha agregado a: {nuevo}")
elif accion == "E":
    eliminar = input("Escriba el nombre a eliminar del listado: ").capitalize()
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"Se ha eliminado a: {eliminar}")
    else:
        print("El nombre no se encuentra en la lista.")
else:
    print("Opción no válida.")

# Se muestran listas actualizadas
print(f"Lista final actualizada ({len(estudiantes)} alumnos): ")
print(estudiantes)


# Ejercicio 6
# Dada un listado con 7 números, rotar todos los elementos una posición hacia la derecha

numeros = [1, 2, 3, 4, 5, 6, 7]
num_rotados = [numeros[-1]] + numeros[:-1]

# Muestra resultados
print(f"Listado original: {numeros}")
print(f"Lista con números rotados: {num_rotados}")


# Ejercicio 7
# Crea una matriz de 7x2 con las temperaturas mínimas y máximas de una semana

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [
    [10, 30],
    [15, 25],
    [17, 28],
    [12, 24],
    [14, 20],
    [11, 19],
    [16, 29]
]
suma_min = 0
suma_max = 0
max_ampl = 0
dia_max_ampl = ""

for i in range(len(temperaturas)):
    temp_min = temperaturas[i][0]
    temp_max = temperaturas[i][1]
    suma_min += temp_min
    suma_max += temp_max
    ampl = temp_max - temp_min
    if ampl > max_ampl:
        max_ampl = ampl
        dia_max_ampl = dias[i]
        
prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)

# Se muestran resultados
print(f"Promedio de temperaturas mínimas: {prom_min:.1f} °C")
print(f"Promedio de temperaturas máximas: {prom_max:.1f} °C")
print(f"El día que se registró mayor amplitud térmica es: {dia_max_ampl} con {max_ampl} °C")


# Ejercicio 8
# Crear una matriz con las notas de 5 estudiantes en 3 materias

notas = [
    [7, 8, 9],
    [10, 7, 8],
    [9, 6, 7],
    [5, 8, 7],
    [9, 10, 8]
]
cant_alumno = len(notas)
cant_materias = len(notas[0])
print("Promedio por cada estudiante: ")
for i in range(cant_alumno):
    suma_notas = sum(notas[i])
    promedio = suma_notas / cant_materias
    print(f"Estudiante {i+1}: {promedio:.2f}")
print("Promedio por materia: ")
nombres_materias = ["Matemáticas", "Lengua", "Inglés"]
for j in range(cant_materias):
    suma_materias = 0
    for i in range(cant_alumno):
        suma_materias += notas[i][j]
    prom_materias = suma_materias / cant_alumno
    print(f"{nombres_materias[j]}: {prom_materias:.2f}")


# Ejercicio 9
# Representar un tablero de Ta-te-ti como una lista 3x3

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
def mostrar_tablero():
    for fila in tablero:
        print(" | ".join(fila))
jugadas = 0
while jugadas < 9:
    mostrar_tablero()
    if jugadas % 2 == 0:
        turno = "X"
    else:
        turno = "O"
    fila = int(input("Ingrese fila (0, 1, 2): "))
    columna = int(input("Ingrese columna (0, 1, 2): "))
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("¡ERROR! Debes elegir número entre 0 y 2.")
        continue
    if tablero[fila][columna] == "-":
        tablero [fila][columna] = turno
        jugadas += 1
    else:
        print("¡Casillero ocupado! Intenta de nuevo.")
        
mostrar_tablero()
print("Fin del juego.")


# Ejercicio 10
# Una tienda registra las ventas de 4 productos durante 7 dias, en una matriz de 4x7

ventas = [
    [5, 20, 10, 15, 7, 25, 30],
    [35, 15, 5, 8, 20, 10, 10],
    [10, 30, 15, 20, 5, 8, 35],
    [15, 9, 35, 10, 25, 15, 10]
]
totales_productos = []
print("Total vendido por producto.")

for i in range(len(ventas)):
    total_prod = sum(ventas[i])
    totales_productos.append(total_prod)
    print(f"Producto {i+1}: {total_prod} unidades.")
    
ventas_por_dia = []
for dia in range(7):
    total_dia = 0
    for producto in range(4):
        total_dia += ventas[producto][dia]
    ventas_por_dia.append(total_dia)
    
dia_maximo = ventas_por_dia.index(max(ventas_por_dia)) + 1
print(f"El día con mayores ventas: {dia_maximo}, con un total: {max(ventas_por_dia)}.")
producto_maximo = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido: {producto_maximo}, con un total: {max(totales_productos)}")


# Ejercicio 11
# Crear una lista con los nombres de 10 estudiantes

estudiantes = ["Ana", "Pedro", "Lucia", "Juan", "Marta", "Diego", "Elena", "Ramiro", "Sonia", "Marcos"]

busqueda = input("Ingrese el nombre del estudiante a buscar: ")

# Comparar sin errores de mayúsculas
if busqueda.capitalize() in estudiantes:
    posicion = estudiantes.index(busqueda.capitalize())
    print(f"El nombre '{busqueda}' se encuentra en la posición {posicion}.")
else:
    print(f"El nombre '{busqueda}' no se encuentra en la lista.")


# Ejercicio 12
# Pedir al ususario que ingrese 8 números enteros y almacenarlos en una lista
numeros = []
for i in range(8):
    num = int(input(f"Ingrese el número entero {i+1}: "))
    numeros.append(num)

print("--- Resultados ---")
print(f"Lista original: {numeros}")

# Investigando sorted(): devuelve una NUEVA lista sin modificar la original
print(f"Ordenada de menor a mayor: {sorted(numeros)}")

# Investigando reverse=True: invierte el orden del resultado
print(f"Ordenada de mayor a menor: {sorted(numeros, reverse=True)}")


# Ejercicio 13
# Dada la siguiente lista de puntajes de un videojuego

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Puntajes extremos
print(f"Puntaje más alto: {max(puntajes)}")
print(f"Puntaje más bajo: {min(puntajes)}")

# Ranking (Mayor a menor)
ranking = sorted(puntajes, reverse=True)
print(f"Ranking: {ranking}")

# Posición del puntaje 990
# Sumamos 1 porque la indexación empieza en 0 (la posición 0 es el 1° lugar)
posicion_990 = ranking.index(990) + 1
print(f"El puntaje 990 se encuentra en la posición {posicion_990} del ranking.")
