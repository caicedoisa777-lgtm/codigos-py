# Definimos las dimensiones de la matriz
FILAS = 5
COLUMNAS = 5

# Inicializamos una lista vacía para almacenar la matriz
matriz = []

print("=== Ingreso de valores para matriz 5x5 ===")
print(f"Debes ingresar {FILAS * COLUMNAS} valores en total.\n")

# Bucle anidado para recorrer filas y columnas
for i in range(FILAS):
    fila_actual = []  # Lista para guardar los valores de la fila i
    for j in range(COLUMNAS):
        # Solicitamos el valor al usuario con su posición
        valor = input(f"Ingrese valor en posición [{i+1}][{j+1}]: ")
        fila_actual.append(valor)  # Agregamos el valor a la fila
    matriz.append(fila_actual)  # Agregamos la fila completa a la matriz

# Mostramos la matriz organizada
print("\n" + "=" * 30)
print(" Matriz 5x5 ingresada:")
print("=" * 30)

for fila in matriz:
    # Formateamos para que se vea ordenada
    print(" | ".join(f"{v:^6}" for v in fila))
    print("-" * 35)