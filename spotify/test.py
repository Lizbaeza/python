from tkinter import Tk,Button
from reproductor import Reproductor

listas = ["musicas/vida_mia.mp3"]
musica = Reproductor(listas[0])

def reproducirMusica():
    musica.reproducir()

winamp = Tk()
winamp.title("WINAMP")
winamp.geometry("300x100")

bPlay = Button(text="▶", command=reproducirMusica)
bPlay.place(x=50,y=50)

winamp.mainloop()