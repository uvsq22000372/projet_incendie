#info groupe
#########################################
# groupe MPCI 3
# Lalasoa RATOVONDRANTO
# Ahmadou Bamba SOIM
# Maxime DANNEVILLE
# Elias SAUVAGE
# https://github.com/uvsq22000372/projet_incendie
#########################################

#import librairies
import tkinter as tk
import random

#definition constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
LARGEUR = 500
HAUTEUR = 500
COTE = 5
DUREE_FEU = 4 #secondes
DUREE_CENDRES = 10 #secondes

#definition variables globales 
nombre_eau = 0
nombre_prairie = 0
nombre_foret = 0

#definition des fonctions
def quadrillage():
    '''Affiche un quadrillage constitué de carrés de côtés COTE'''
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += COTE

def xy_to_cl(x, y):
    '''Retourne la colonne et la ligne du tableau correspondant aux coordonnées (x, y) du canevas'''
    #à faire
    return 0, 0

def random_terrain():
    pass







########################
# programme principal

racine = tk.Tk()
racine.title("Simulation incendie")
# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)

# positionnement
canvas.grid()

# gestion des événements
canvas.bind("<Button-1>")

# autres fonctions
quadrillage()


# boucle principal
racine.mainloop()