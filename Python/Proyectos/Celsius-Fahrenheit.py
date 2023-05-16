#Programa que convierte grados Celsius a Fahrenheit y viceversa
#Autor: Jhon Garcia

#Funcion que convierte grados Celsius a Fahrenheit
def conversion(temperatura, unidad):
    if unidad == "C":
        return (temperatura * 1.8) + 32
    elif unidad == "F":
        return (temperatura - 32) / 1.8
    else:
        return "Unidad no reconocida"

#Funcion que pide la temperatura y la unidad
def pedir_datos():
    temperatura = float(input("Introduce la temperatura: "))
    unidad = input("Introduce la unidad (C o F): ")
    return temperatura, unidad

#Funcion que imprime el resultado
def imprimir_resultado(temperatura, unidad):
    print("La temperatura es: ", temperatura, unidad)

#Funcion principal
def main():
    temperatura, unidad = pedir_datos()
    temperatura = conversion(temperatura, unidad)
    imprimir_resultado(temperatura, unidad)

#Llamada a la funcion principal
main()


