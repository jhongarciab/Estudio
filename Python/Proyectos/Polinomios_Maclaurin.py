import sympy as sp

def polinomio():
    funcionprimera = input("Ingrese la función: ")
    x = sp.Symbol('x')
    try:
        funcion = sp.sympify(funcionprimera)
    except sp.SympifyError:
        print(f'La función {funcionprimera} no es válida.')
        return

    n = int(input("Ingrese las iteraciones deseadas: "))
    polinomio_MC = funcion.series(x, 0, n).removeO()

    print(f"El polinomio de Maclaurin de la función {funcionprimera} es: ")
    print(polinomio_MC)

polinomio()