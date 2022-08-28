from doctest import master
from tkinter import *
import os

def to_switch_off():
    return os.system("shutdown /s /t l")

def restart():
    return os.system("shutdown /r /t l")

def exit():
    return os.system("shutdown -l")

master = Tk()
master.geometry("300x300")
master.title('Devlog Shotdown')

master.configure(bg='#3489eb')

Button(master, text="DESLIGAR", command=to_switch_off).place(x=20, y=20)
Button(master, text="RENICIAR", command=restart).place(x=19, y=50)
Button(master, text="Sair", command=exit).place(x=32 , y=80)

mainloop()