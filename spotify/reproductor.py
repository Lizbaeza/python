from pygame import mixer

class Reproductor:
    def __init__(self,archivo):
        mixer.init()
        mixer.music.load(archivo)

    def reproducir(self):
        mixer.music.play()

    def pausar(self):
        pass

    def parar(self):
        pass
