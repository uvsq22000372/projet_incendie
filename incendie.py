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
import random as rd

#definition constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
LARGEUR = 800
HAUTEUR = 800
COTE = 20
DUREE_FEU = 4000 # en ms
DUREE_CENDRES = 10000 # en ms

#definition variables globales 
nombre_eau = []
nombre_prairie = []
nombre_foret = []

Couleur = ["dodger blue", "dodger blue", "green4", "green4", "green4", "green4", "green4", "yellow","yellow", "yellow" ]


#definition des fonctions
def Carré():
    x0, y0, x1, y1 = 0, 0, COTE, COTE
    while y0 <= HAUTEUR and x1 <= LARGEUR:
        i = rd.randint(0, 9)
        carré = canvas.create_rectangle(x0, y0, x1, y1,fill=Couleur[i])
        if i >= 0 and i < 2:
            nombre_eau.append(carré)
        elif i >= 2 and i < 6:
            nombre_foret.append(carré)
        elif i >= 6 and i < 10:
            nombre_prairie.append(carré)
        x0 += COTE
        x1 += COTE
        if x0 == LARGEUR:
            x0 = 0
            x1 = COTE 
            y0 += COTE
            y1 += COTE
    print(nombre_eau)
    print(nombre_foret)
    print(nombre_prairie)
        

def random_terrain():
    pass
def GetColor(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



# Idée a développer plus tard 
    # if carré x=mort, l_carré.delete[x] (évitez les surcharges)


########################
# programme principal

racine = tk.Tk()
racine.title("Simulation incendie")
# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR, bd = -2)

# positionnement
canvas.grid()

# gestion des événements
canvas.bind("<Button-1>")

# autres fonctions
Carré()


# boucle principal
racine.mainloop()