#info groupe
#########################################
# MPCI TD3
# équipe 2
# Lalasoa RATOVONDRANTO
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
LARGEUR = 1000
HAUTEUR = 1000
COTE = 20
n = 4
x = 0

#definition variables globales 
nombre_eau = []
nombre_terre = []
l_carré = []

coul_eau = ["RoyalBlue1"]
coul_terre = ["salmon4"]


#definition des fonctions
def Carré():
    x0, y0, x1, y1 = 0, 0, COTE, COTE
    while y0 < HAUTEUR and x1 <= LARGEUR:
        carré = canvas.create_rectangle(x0, y0, x1, y1,fill=coul_eau[0])
        l_carré.append(carré)
        nombre_eau.append(carré)
        #if i >= 0 and i < 2:
        #   nombre_eau.append(carré)
        #elif i >= 2 and i < 6:
        #    nombre_foret.append(carré)
        #elif i >= 6 and i < 10:
        #    nombre_prairie.append(carré)
        x0 += COTE
        x1 += COTE
        if x0 == LARGEUR:
            x0 = 0
            x1 = COTE 
            y0 += COTE
            y1 += COTE
    print(l_carré)

        


def random_terrain():
    global nombre_eau
    global nombre_terre
    global x
    for i in (0, n):
        for i in l_carré:
            r = rd.randint(0, 1)
            if r == 0:
                pass
            else:
                canvas.itemconfig((l_carré[i]) , fill=coul_terre[0])
                nombre_terre.append(l_carré[i])
                del nombre_eau[i - x]
                x += 1
        print(nombre_eau)
        print(nombre_terre)


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
random_terrain()


# boucle principal
racine.mainloop()
