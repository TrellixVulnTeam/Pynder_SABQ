# -*- coding: utf-8 -*-
from tkinter import *
from GlobalVariable import GlobalVariable
from fase1 import fase1

janela = Tk()
janela.title("Pynder")
janela.geometry("400x700")
xx=400
yy=700
fontGrande = ('',30)
fontePequena = ('',15)


def login():
    g = GlobalVariable("","")
    g.setNome(nome.get())
    fase1(g.getNome())

lb = Label(janela, text="Bem vindo", font=fontGrande).place(x=125, y=100)
lb = Label(janela, text="Nome:", font=fontePequena).place(x=80, y=300)
nome = Entry(janela, width=15, font=fontePequena)
nome.place(x=150, y=300)

bt = Button (janela, text="Entrar", font=fontePequena, command=login)
bt.place(x=180, y=500)

janela.mainloop()