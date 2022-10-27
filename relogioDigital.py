from tkinter import *
import tkinter
from datetime import datetime as dt


fundo = "#3d3d3d"
cor = "#fafcff"

janela=Tk()
janela.title("Relógio do Juca")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=fundo)

def relogio():
    tempo = dt.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia=tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1=Label(janela, text="", font=("Serif 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2=Label(janela, text="", font=("Serif 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=SE, padx=5)


relogio()
janela.mainloop()