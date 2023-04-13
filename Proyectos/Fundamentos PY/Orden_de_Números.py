#Programa que ordena una lista de numeros
#Autor: Jhon Garcia

#Funcion que pide una lista de numeros
def pedir_lista():
    lista = []
    numero = (input("Introduce un numero y escriba salir para finalizar lista: "))
    while numero != "salir":
        lista.append(numero)
        numero = (input("Introduce otro numero: "))
    return lista

#Funcion que ordena la lista
def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

#Funcion que imprime el resultado
def imprimir_resultado(lista):
    print("La lista de menor a mayor es: ", lista)

#Funcion principal
def main():
    lista = pedir_lista()
    lista = ordenar_lista(lista)
    imprimir_resultado(lista)

#Llamada a la funcion principal
main()