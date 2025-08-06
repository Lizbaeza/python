#CRUD Create,Read,Update,Delete
class AlumnoController:
    alumnos = None
    def __init__(self):
        self.alumnos = []

    def save(self,alumno):
       self.alumnos.append(alumno)

    def getAll(self):
        return self.alumnos

    def getAlumno(self,indice):
        #validar indice 
        return self.alumnos[indice]

    def update(self,alumno,indice):
        self.alumnos[indice] = alumno
    
    def delete(self,indice):
        alumno = self.alumnos[indice]
        self.alumnos.remove(alumno)