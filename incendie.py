#info groupe
#########################################
# groupe MPCI 3
# Lalasoa RATOVONDRANTO
# Ahmadou Bamba SOIM
# Maxime DANEVILLE
# Elias SAUVAGE
# https://github.com/uvsq22000372/projet_incendie
#########################################

#import librairies
import tkinter as tk
import random

#definition constantes
LARGEUR = 500
HAUTEUR = 500
DUREE_FEU = 40 #secondes
DUREE_CENDRES = 80 #secondes

#definition variables globales 
nombre_eau = 0
nombre_prairie = 0
nombre_foret = 0


CANVAS_WIDTH, CANVAS_HEIGHT = LARGEUR, HAUTEUR







root = tk.Tk()
root.title("Simulation incendie")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief = "raised", borderwidth = 5)
canvas.grid(column = 1, row = 1, rowspan = 3, columnspan = 2)

root.mainloop()