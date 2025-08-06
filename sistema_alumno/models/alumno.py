class Alumno:
    nombreApellido = None
    email = None
    Matricula = None

    def __init__(self,nombreApellido,email,Matricula):
        self.nombreApellido = nombreApellido
        self.email = email
        self.Matricula = Matricula

    def getInformacion(self):
        return f"Alumno: {self.nombreApellido},email: {self.email},Matricula: {self.Matricula}"
