from controllers.alumno_controller import AlumnoController
from view.test_alumno import ejecutar_vista

def main():
    controlador = AlumnoController()
    ejecutar_vista(controlador)

if __name__ == "__main__":
    main()