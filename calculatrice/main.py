import customtkinter
from tkinter import *
from tkinter import messagebox


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

#Je créé la zone de ma calculatrice
tk = customtkinter.CTk()
tk.geometry("350x490")

def button_click(nombre):
    texte.insert (END, nombre)

def clear():
    texte.delete(0, END)

def enlever():
    texte.delete(len(texte.get())-1)

def calculEgal():
    try:
        equation = texte.get()
        new_equation = equation.replace('X','*')
        result = eval(new_equation)
        clear()
        texte.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror('Erreur, division par 0 !')
    except :
        messagebox.showerror('Erreur')

#creation de la zone de texte 
texte = customtkinter.CTkEntry(tk, text_color='#FFF', fg_color='#123', width=255, height=60)
texte.place(x=95, y=10)

#Je créé tous les boutons de ma calculatruce classique

mode = customtkinter.CTkButton(master=tk, text="Mode", width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
mode.place(x=10, y=10)

pourcent = customtkinter.CTkButton(master=tk, text="%", command=lambda: button_click('/100'), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
pourcent.place(x=10, y=85)

c = customtkinter.CTkButton(master=tk, text="C", command=clear, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
c.place(x=95, y=85)

ce = customtkinter.CTkButton(master=tk, text="CE", command=clear, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
ce.place(x=180, y=85)

DEL = customtkinter.CTkButton(master=tk, text="DEL", command=enlever, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
DEL.place(x=265, y=85)

sur1 = customtkinter.CTkButton(master=tk, text="1/x", command=lambda: button_click('1/'), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
sur1.place(x=10, y=150)

carre = customtkinter.CTkButton(master=tk, text="x²", command=lambda: button_click('**2'), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
carre.place(x=95, y=150)

bouton7 = customtkinter.CTkButton(master=tk, text="²√x",  width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
bouton7.place(x=180, y=150)

sur = customtkinter.CTkButton(master=tk, text="/", command=lambda: button_click('/'), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
sur.place(x=265, y=150)

sept = customtkinter.CTkButton(master=tk, text="7", command=lambda: button_click('7'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
sept.place(x=10, y=215)

huit = customtkinter.CTkButton(master=tk, text="8", command=lambda: button_click('8'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
huit.place(x=95, y=215)

neuf = customtkinter.CTkButton(master=tk, text="9", command=lambda: button_click('9'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
neuf.place(x=180, y=215)

x = customtkinter.CTkButton(master=tk, text="X", command=lambda: button_click('*'), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
x.place(x=265, y=215)

quatre = customtkinter.CTkButton(master=tk, text="4", command=lambda: button_click('4'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
quatre.place(x=10, y=280)

cinq = customtkinter.CTkButton(master=tk, text="5", command=lambda: button_click('5'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
cinq.place(x=95, y=280)

six = customtkinter.CTkButton(master=tk, text="6", command=lambda: button_click('6'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
six.place(x=180, y=280)

moins = customtkinter.CTkButton(master=tk, text="-", command=lambda: button_click('-'), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
moins.place(x=265, y=280)

un = customtkinter.CTkButton(master=tk, text="1", command=lambda: button_click('1'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
un.place(x=10, y=345)

deux = customtkinter.CTkButton(master=tk, text="2", command=lambda: button_click('2'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
deux.place(x=95, y=345)

trois = customtkinter.CTkButton(master=tk, text="3", command=lambda: button_click('3'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
trois.place(x=180, y=345)

plus = customtkinter.CTkButton(master=tk, text="+", command=lambda: button_click('+'),  width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
plus.place(x=265, y=345)

signe = customtkinter.CTkButton(master=tk, text="+/-", width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
signe.place(x=10, y=410)

zero = customtkinter.CTkButton(master=tk, text="0", command=lambda: button_click('0'), width=80, height=60, text_color="#000" , fg_color="#FFF", hover_color="#FFC0D9")
zero.place(x=95, y=410)

virgule = customtkinter.CTkButton(master=tk, text=",", command=lambda: button_click(','), width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
virgule.place(x=180, y=410)

egal = customtkinter.CTkButton(master=tk, text="=", command=calculEgal, width=80, height=60, fg_color="#F875AA", hover_color="#FFC0D9")
egal.place(x=265, y=410)

tk.mainloop()
