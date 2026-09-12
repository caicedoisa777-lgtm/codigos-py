# 1. Crear matriz de 3 filas x 4 columnas inicializada en 0
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 2. Pedir fila y columna al usuario (ajustamos a índice empezando en 0)
fila = int(input("Ingrese el número de fila (1-3): ")) - 1
columna = int(input("Ingrese el número de columna (1-4): ")) - 1

# Validar que los datos estén dentro del rango permitido
if 0 <= fila < 3 and 0 <= columna < 4:
    # 3. Marcar asiento como reservado → valor 1
    asientos[fila][columna] = 1
    print("\nAsiento reservado correctamente.\n")
else:
    print("\n Fila o columna no válidas.\n")

# 4. Mostrar la matriz en formato tabla con bucles anidados
print("Estado de los asientos (0=Libre | 1=Reservado):")
for fila_actual in asientos:
    for valor in fila_actual:
        print(f"| {valor} ", end="")  # Mostrar cada valor alineado
    print("|") 