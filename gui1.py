from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")

def abrirChorme():
    os.system("start chrome")


def abrirRobloxPlayer():
    os.system("start Roblox Player")


ventana = Tk()
ventana.title("Menu principal")
ventana.config(bg="red")
ventana.geometry("520x480")
ventana.resizable(0,0)

botonCalc = Button(text="calculadora", command=abrirCalculadora)
botonCalc.place(x=50, y=50)

botonChorme = Button(text="Chorme", command=abrirChorme)
botonChorme.place(x=50, y=100)

botonRoblox= Button(text="Roblox", command=abrirRobloxPlayer)
botonRoblox.place(x=50, y=150)

ventana.mainloop()