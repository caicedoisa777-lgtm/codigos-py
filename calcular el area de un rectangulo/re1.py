#funcion con parametros
def area_rectangulo(base, altura):
    area = base * altura
    return area
#programa principal
base = float(input("Ingrese la base del rectángulo:"))
altura = float(input("Ingrese la altura del rectángulo:"))
#llamada a la funcion
area_total = area_rectangulo(base, altura)
#salida 
print("el área del rectangulo es:", area_total)