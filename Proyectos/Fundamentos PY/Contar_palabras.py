#Programa que cuente el número de palabras y caracteres de un texto
#Autor: Jhon Garcia

#Funcion que pide un texto
def pedir_texto():
    texto = input("Introduce un texto: ")
    return texto

#Funcion que cuenta el numero de palabras y caracteres
def contar_palabras(texto):
    palabras = texto.split()
    caracteres = len(texto)
    return palabras, caracteres

#Funcion que imprime el resultado
def imprimir_resultado(palabras, caracteres):
    print("El numero de palabras es: ", len(palabras))
    print("El numero de caracteres es: ", caracteres)

#Funcion principal
def main():
    texto = pedir_texto()
    palabras, caracteres = contar_palabras(texto)
    imprimir_resultado(palabras, caracteres)    

#Llamada a la funcion principal
main()