# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:36:19 2023

@author: kerva
"""
import tkinter, os
import Joueur as JR
import Dérouler as drl

CL_fenetre_fond = "#E1EE60"

fenetre_fond = tkinter.Tk()
fenetre_fond.title("Monopolie")
fenetre_fond.config(bg=CL_fenetre_fond)
fenetre_fond.geometry("1500x500")


def définir_joueurs(nbr_joueur):
    """
    Implémente le nombre de joueur dans la partie
    et leur attribut un pseudo

    Parameters
    ----------
    nbr_joueur : int
        le nombre de joueur dans la partie.

    Returns
    -------
    liste_joueur : list
        liste toute les informations des joueurs.
    nom_joueur : list
        liste de pseudo des joueurs.
    """
    liste_joueur, nom_joueur = [], []
    for i in range(nbr_joueur):
        liste_joueur.append(JR.Joueur())
        nom_joueur.append(input(f"Quel est le nom du joueur {i+1} "))
    os.system('cls')
    return liste_joueur, nom_joueur

#modifier le input avec un bouton et un label




def lancement () :
    s.pack()
    ok.pack()
    lancement.pack_forget()
    while ok(state) == "active":
        pass
    Game = drl.dérouler(s)
    Joueur.pack()
    for i in range (nbr_joueur) :
        Joueur.config(text = f"C'est au tour de {Game.nom_joueur[i]} !!!")

# a modifier    
    
    



Joueur = tkinter.Label(fenetre_fond,
                       fg = "red", bg = CL_fenetre_fond)

lancement = tkinter.Button(fenetre_fond,
                         fg = 'red',
                         text = "Lancer",
                         command = lancement)

ok = tkinter.Button(fenetre_fond,
                         fg = 'red',
                         text = "ok",
                         state ="active")

s = tkinter.Spinbox(fenetre_fond, from_=2, to=4)

entrer = tkinter.Entry(fenetre_fond)


arreter = tkinter.Button(fenetre_fond,
                         fg = 'red',
                         text = "Quitter",
                         command = fenetre_fond.destroy)

lancement.pack()
arreter.pack()
fenetre_fond.mainloop()

