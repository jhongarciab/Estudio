class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, mail=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._mail = mail

    def __str__(self):
        return f"""
        ID: {self._id_persona}
        Nombre: {self._nombre}
        Apellido: {self._apellido}
        Mail: {self._mail}
        """
    
    @property
    def id_persona(self):
        return self._id_persona
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def mail(self):
        return self._mail
    
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @mail.setter
    def mail(self, mail):
        self._mail = mail