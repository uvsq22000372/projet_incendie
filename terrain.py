#info groupe
#########################################
# MPCI TD3
# équipe 2
# Lalasoa RATOVONDRANTO
# Maxime DANNEVILLE
# Elias SAUVAGE 
# El Fahad ASSOUMANI
# https://github.com/uvsq22000372/projet_terrain
#########################################

#import librairies
import tkinter as tk
import random as rd

#definition constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
LARGEUR = 676
HAUTEUR = 676
COTE = LARGEUR // 52
n = 4
k = 1
counter = 0
T = 5
p = 0.5
x = 0


#definition variables globales 
nombre_eau = []
nombre_terre = []
l_carré = []
bordure = []
ListeTropGenial = []

coul_eau = ["dodgerblue2"]
coul_terre = ["burlywood3"]
coul_bordure =["white"]


#definition des fonctions

#def répétitions(repet):
    #global n
    #n = repet

def Carré():
    global nombre_eau
    x0, y0, x1, y1 = 0, 0, COTE, COTE
    while y0 < HAUTEUR and x1 <= LARGEUR:
        carré = canvas.create_rectangle(x0, y0, x1, y1,fill=coul_eau[0], width = 0)
        l_carré.append(carré)
        nombre_eau.append(carré)
        x0 += COTE
        x1 += COTE
        if x0 == LARGEUR:
            x0 = 0
            x1 = COTE 
            y0 += COTE
            y1 += COTE




def creation_terrain():
    global nombre_terre
    global nombre_eau
    global bordure
    

    for i in range(len(l_carré)):
        if  int(l_carré[i]) <= 52 or int(l_carré[i]) > 2652 or int((l_carré[i]) - 1) % 52 == 0 or int(l_carré[i]) % 52 == 0:
            canvas.itemconfig((l_carré[i]) , fill=coul_bordure[0])
            nombre_eau.remove(l_carré[i])
            bordure.append(l_carré[i])
    
        r = rd.randint(0, 100)
        #print(r)
        if r > p*100  and int(l_carré[i]) > 52 and int(l_carré[i]) <= 2652 and int((l_carré[i]) - 1) % 52 != 0 and int(l_carré[i]) % 52 != 0:
            canvas.itemconfig((l_carré[i]) , fill=coul_terre[0])
            nombre_terre.append(l_carré[i])
            nombre_eau.remove(l_carré[i])

def tri():
    global nombre_terre, nombre_eau
    nombre_terre = sorted(nombre_terre)
    for i in nombre_terre:
        if nombre_terre.count(i) > 1:
            for y in range(0, (nombre_terre.count(i) - 1)):
                nombre_terre.remove(i)

    nombre_eau = sorted(nombre_eau)
    for i in nombre_eau:
        if nombre_eau.count(i) > 1:
            for y in range(0, (nombre_eau.count(i) - 1)):
                nombre_eau.remove(i)
            

def nombre_voisins():
    """automate, avec definitions du nombres de cases terre/eau dans le voisinage"""
    global counter
    global nombre_terre
    global nombre_eau
    global ListeTropGenial
    global x
    for y in range(n):
        for i in range(len(l_carré)):


            if l_carré[i] in nombre_terre:            

                if int(l_carré[i]) > 52 and int(l_carré[i]) <= 2652 and int((l_carré[i]) - 1) % 52 != 0 and int(l_carré[i]) % 52 != 0:

                    if (l_carré[i+k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-52]) in nombre_eau:
                        counter += 1
                    if (l_carré[i+52]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-52+k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i+52+k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-52-k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i+52-k]) in nombre_eau:
                        counter += 1
                    if counter >= T:
                        ListeTropGenial.append(l_carré[i])
                        counter = 0
                    if counter < T:
                        counter = 0

            if l_carré[i] in nombre_eau: 


                if int(l_carré[i]) > 52 and int(l_carré[i]) <= 2652 and int((l_carré[i]) - 1) % 52 != 0 and int(l_carré[i]) % 52 != 0:

                    if (l_carré[i+k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-52]) in nombre_terre:
                        counter += 1
                    if (l_carré[i+52]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-52+k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i+52+k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-52-k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i+52-k]) in nombre_terre:
                        counter += 1
                    if counter >= T:
                        ListeTropGenial.append(l_carré[i])
                        counter = 0
                    if counter < T:
                        counter = 0
        ChangementDeCoul()

def ChangementDeCoul():
    """gestion couleur terrain"""
    global ListeTropGenial
    global x
    x = 0
    ListeTropGenial = sorted(ListeTropGenial)
    for q in ListeTropGenial:
        if ListeTropGenial.count(q) > 1:
            for w in range(0, (ListeTropGenial.count(q) - 1)):
                ListeTropGenial.remove(q)


    for i in range(len(ListeTropGenial)):

        if x == 1:
            x = 0

        if ListeTropGenial[i] in nombre_terre and x != 1:
            canvas.itemconfig((ListeTropGenial[i]) , fill=coul_eau[0])
            nombre_eau.append(ListeTropGenial[i])
            nombre_terre.remove(ListeTropGenial[i])
            x = 1
        

        if ListeTropGenial[i] in nombre_eau and x != 1:
            canvas.itemconfig((ListeTropGenial[i]) , fill=coul_terre[0])
            nombre_terre.append(ListeTropGenial[i])
            nombre_eau.remove(ListeTropGenial[i])
            x = 1
        
        if x == 1:
            x = 0      
    ListeTropGenial = []
    tri()

    ListeTropGenial = sorted(ListeTropGenial)
    for q in ListeTropGenial:
        if ListeTropGenial.count(q) > 1:
            for w in range(0, (ListeTropGenial.count(q) - 1)):
                ListeTropGenial.remove(q)
        
        for z in range(len(ListeTropGenial)):

            if x == 1:
                x = 0

            if ListeTropGenial[z] in nombre_terre and x != 1:
                canvas.itemconfig((ListeTropGenial[z]) , fill=coul_eau[0])
                nombre_eau.append(ListeTropGenial[z])
                nombre_terre.remove(ListeTropGenial[z])
                x = 1
            

            if ListeTropGenial[z] in nombre_eau and x != 1:
                canvas.itemconfig((ListeTropGenial[z]) , fill=coul_terre[0])
                nombre_terre.append(ListeTropGenial[z])
                nombre_eau.remove(ListeTropGenial[z])
                x = 1
            
            if x == 1:
                x = 0
        ListeTropGenial = []
        tri()

def placement(event):
    pass

#def test(event):
    """test les repetitions de l'automate"""
    #global n
    #n += 1
    #nombre_voisins()


#ajouter curseurs (repetitions automate = n, distance = k, voisinage = T, probabilité eau = p)
#ajouter menu 
#deplacement personnage (dont deplacement)

########################
# programme principal
racine = tk.Tk()
racine.title("Generation de terrain")

# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR, bd = -2)
canvas.grid(row=0, column=0, rowspan=2)

#curseur = tk.Scale(orient = "horizontal", command=répétitions, from_=0, to=8, length=100)
#curseur.set(4)
#curseur.grid(row=1, column=1)

# positionnement
canvas.grid()

# gestion des événements
#canvas.bind("<Button-1>",test)
canvas.bind("<Button-1>", placement)

# autres fonctions
Carré()
creation_terrain()
nombre_voisins()



# boucle principal
racine.mainloop()
