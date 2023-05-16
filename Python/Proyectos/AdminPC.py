class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def __str__(self):
        return f'Dispositivo de entrada: {self._idDispositivoEntrada}, Tipo de entrada: {self._tipoEntrada}, Marca: {self._marca}'

class Raton(DispositivoEntrada):
    contadorRatones = 0
    def __init__(self, tipoEntrada, marca):
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'ID: {self._idRaton}, Tipo de entrada: {self._tipoEntrada}, Marca: {self._marca}'

class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        super().__init__(tipoEntrada, marca)
    
    def __str__(self):
        return f'ID: {self._idTeclado}, Tipo de entrada: {self._tipoEntrada}, Marca: {self._marca}'

class Monitor:
    contadorMonitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'ID: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño} Pulgadas'

class Computadora:
    contadorComputadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadora += 1
        self._idComputadora = Computadora.contadorComputadora
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        Nombre: {self._nombre}, ID PC: {self._idComputadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

class Orden:
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadorasStr = ''
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__()
        return f'''
            Orden: {self._idOrden}
        Computadoras: {computadorasStr}
        '''
    
teclado1 = Teclado('USB', 'HP')
teclado2 = Teclado('Bluetooth', 'Dell')
raton1 = Raton('USB', 'HP')
raton2 = Raton('Bluetooth', 'Dell')
monitor1 = Monitor('HP', 27)
monitor2 = Monitor('Dell', 24)
computador1 = Computadora('HP', monitor1, teclado1, raton1)
computador2 = Computadora('Dell', monitor2, teclado2, raton2)

computadoras1 = [computador1, computador2]
orden1 = Orden(computadoras1)
print(orden1)
computadora3 = Computadora('Lenovo', monitor1, teclado2, raton1)
orden1.agregarComputadora(computadora3)
print(orden1)