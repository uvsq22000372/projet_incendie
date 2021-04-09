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
import collections

#definition constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
LARGEUR = 650
HAUTEUR = 650
COTE = 13
n = 4
x = 0
k = 1

#definition variables globales 
nombre_eau = []
nombre_terre = []
l_carré = []
voisins = []

coul_eau = ["RoyalBlue1"]
coul_terre = ["salmon4"]


#definition des fonctions
def Carré():
    global nombre_eau
    x0, y0, x1, y1 = 0, 0, COTE, COTE
    while y0 < HAUTEUR and x1 <= LARGEUR:
        carré = canvas.create_rectangle(x0, y0, x1, y1,fill=coul_eau[0])
        l_carré.append(carré)
        nombre_eau.append(carré)
        x0 += COTE
        x1 += COTE
        if x0 == LARGEUR:
            x0 = 0
            x1 = COTE 
            y0 += COTE
            y1 += COTE

        


def random_terrain():
    global nombre_terre
    global nombre_eau
    for i in range(len(l_carré)):
        r = rd.randint(0, 1)
        if r == 0:
            canvas.itemconfig((l_carré[i]) , fill=coul_terre[0])
            nombre_terre.append(l_carré[i])
            nombre_eau.remove(l_carré[i])
    nombre_terre = sorted(nombre_terre)
    #print(nombre_terre)
    #print(nombre_eau)
            

def nombre_voisins():
    """rettourne le nombre de cases autour d'une case i"""
    for i in range(len(nombre_eau)):
        if (i + k) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i - k) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i + 50) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i - 50) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i + 50 + k) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i + 50 - k) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i - 50 - k) // (nombre_eau[i]) == 0:
            voisins.append(i)
        if (i - 50 + k) // (nombre_eau[i]) == 0:
            voisins.append(i)

def automate():
    counter=collections.Counter(voisins)
    print(counter)



def GetColor(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



# Idée a développer plus tard 
    # if carré x=mort, l_carré.delete[x] (évitez les surcharges)
    # 
    # utiliser "in" pour voir si c'est un bloc de terre
    #
    # 

########################
# programme principal

racine = tk.Tk()
racine.title("Generation de terrain")
# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR, bd = -2)

# positionnement
canvas.grid()

# gestion des événements
canvas.bind("<Button-1>")

# autres fonctions
Carré()
random_terrain()
nombre_voisins()
automate()


# boucle principal
racine.mainloop()
