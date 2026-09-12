#calculadora de total de compra
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

# Ejemplo de uso
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

resultado = calcular_total(precio, cantidad)
print("El total de la compra es: $", resultado)
