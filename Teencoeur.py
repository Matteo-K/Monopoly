# -*- coding: utf-8 -*-
import tkinter

def test():
    label.pack()
    Bouton.config(state="disabled")
    Bouton1.config(state="active")
    
def retire():
    label.pack_forget()
    Bouton.config(state="active")
    Bouton1.config(state="disabled")
       
fenetre_fond = tkinter.Tk()
fenetre_fond.title("Monopolie")
fenetre_fond.config(bg="#E1EE60")
fenetre_fond.geometry("1500x500")

x = 0

label = tkinter.Label(fenetre_fond,
                      text = f"OMG vous avez un QI de {x} !!!",
                      fg = "red",
                      bg = "green")

Bouton = tkinter.Button(fenetre_fond,
                        fg = "green",
                        activeforeground = "green",
                        text = "Lancer le jeu, pas par la fenetre_fond ...",
                        justify = "left",
                        state="active",
                        command = test
                        )
                        
Bouton1 = tkinter.Button(fenetre_fond,
                        fg = "green",
                        activeforeground = "green",
                        text = "arreter le label",
                        state="disabled",
                        command = retire
                        )

arreter = tkinter.Button(fenetre_fond,
                         fg = 'red',
                         text = "Quitter",
                         command = fenetre_fond.destroy
                         )

Bouton.pack()
Bouton1.pack()
arreter.pack()
fenetre_fond.mainloop()