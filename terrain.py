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
counter = 0

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
        r = rd.randint(0, 2)
        if r != 0:
            canvas.itemconfig((l_carré[i]) , fill=coul_terre[0])
            nombre_terre.append(l_carré[i])
            nombre_eau.remove(l_carré[i])
    nombre_terre = sorted(nombre_terre)
    #print(nombre_terre)
    #print(nombre_eau)
            

def nombre_voisins():
    """retourne le nombre de cases autour d'une case i"""
    global counter
    for y in range(0,n):
        for i in range(len(nombre_eau)):
            if int(l_carré[i]) == 1:

                if (l_carré[i+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1                
                if (l_carré[i+50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1                
                if (l_carré[i+50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1


            if int(l_carré[i]) == 50:

                if (l_carré[i-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1                
                if (l_carré[i+50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1                
                if (l_carré[i+50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1


            if int(l_carré[i]) == 2401:

                if (l_carré[i+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1


            if int(l_carré[i]) == 2450:

                if (l_carré[i-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1               
                if (l_carré[i-50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
            
            if int(l_carré[i]) <= 50:

                if (l_carré[i+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-k]) in nombre_eau:
                        voisins.append(i)
                        counter += 1
                if (l_carré[i+50]) in nombre_eau:
                        voisins.append(i)
                        counter += 1
                if (l_carré[i+50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1

                
            if int(l_carré[i]) > 2450:

                if (l_carré[i+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1                
                if (l_carré[i-50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1               
            

            if int(l_carré[i]) % 50 == 0:

                if (l_carré[i-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1

            if int((l_carré[i]) - 1) % 50 == 0:

                if (l_carré[i+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1

            if int((l_carré[i]) - 1) % 50 != 0 and int(l_carré[i]) % 50 != 0 and int(l_carré[i]) < 2450 and int(l_carré[i]) > 50:
                if (l_carré[i+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50+k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i-50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1
                if (l_carré[i+50-k]) in nombre_eau:
                    voisins.append(i)
                    counter += 1

            
                if counter > 5 and l_carré[i] in nombre_terre:
                    canvas.itemconfig((l_carré[i]) , fill=coul_eau[0])
                    nombre_eau.append(l_carré[i])
                    nombre_terre.remove(l_carré[i])
                    print(counter)
                    counter = 0
                    print(counter)
                if counter <= 5:
                    counter = 0

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



# boucle principal
racine.mainloop()
