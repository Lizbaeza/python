import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from controllers.alumno_controller import AlumnoController
from models.alumno import Alumno

class TestAlumno:
    def __init__(self):
        self.ac = AlumnoController()

    def amin(self):
        while True:
            print("-----------MENU-----------")
            print("1. cargar alumno")
            print("2. ver alumno")
            print("3. Actualizar alumno")
            print("4. Borrar Todo")
            print("5. Ver Todo")
            print("0. salir")
            resp = input("opcion: ")
            if resp == "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                matricula = input("Matricula: ")
                self.ac.save(Alumno(nombre,email,matricula))
            elif resp == "5":
                for alu in self.ac.getAll():
                    print(alu.getInformacion())
            elif resp == "0":
                print("BYE")
                break 


if __name__ == "__main__":
    vista = TestAlumno()
    vista.amin()


    