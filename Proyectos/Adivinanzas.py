#Programa que adivina un numero
#Autor: Jhon Garcia

import random

#Funcion que pide un numero
def pedir_numero():
    numero = int(input("Introduce un numero: "))
    return numero

#Funcion que adivina el numero
def adivinar_numero(numero):
    intentos = 0
    adivinado = False
    numero_aleatorio = random.randint(0, 100)
    while not adivinado:
        intentos += 1
        if numero_aleatorio == numero:
            adivinado = True
    return intentos


#Funcion que imprime el resultado
def imprimir_resultado(intentos):
    print("El numero es: ", intentos)

#Funcion principal
def main():
    numero = pedir_numero()
    intentos = adivinar_numero(numero)
    imprimir_resultado(intentos)

#Llamada a la funcion principal
main()