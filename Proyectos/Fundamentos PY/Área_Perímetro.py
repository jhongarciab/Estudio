#Programa que calcule el área y perímetro de una figura geométrica
#Autor: Jhon Garcia

#Funcion que pide el tipo de figura
def pedir_figura():
    figura = input("Introduce el tipo de figura (cuadrado, rectángulo o triángulo): ")
    return figura

#Funcion que pide los datos de la figura
def pedir_datos(figura):
    if figura == "cuadrado":
        lado = float(input("Introduce el lado: "))
        return lado
    elif figura == "rectángulo":
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        return base, altura
    elif figura == "triángulo":
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        lado1 = float(input("Introduce el primer lado: "))
        lado2 = float(input("Introduce el segundo lado: "))
        return base, altura, lado1, lado2
    else:
        return "Figura no reconocida"
    
#Funcion que calcula el área y el perímetro
def calcular_area_perimetro(figura, datos):
    if figura == "cuadrado":
        lado = datos
        area = lado * lado
        perimetro = lado * 4
        return area, perimetro
    elif figura == "rectángulo":
        base, altura = datos
        area = base * altura
        perimetro = (base * 2) + (altura * 2)
        return area, perimetro
    elif figura == "triángulo":
        base, altura, lado1, lado2 = datos
        area = (base * altura) / 2
        perimetro = base + lado1 + lado2
        return area, perimetro
    else:
        return "Figura no reconocida"
    
#Funcion que imprime el resultado
def imprimir_resultado(area, perimetro):
    print("El área es: ", area)
    print("El perímetro es: ", perimetro)

#Funcion principal
def main():
    figura = pedir_figura()
    datos = pedir_datos(figura)
    area, perimetro = calcular_area_perimetro(figura, datos)
    imprimir_resultado(area, perimetro)

#Llamada a la funcion principal
main()