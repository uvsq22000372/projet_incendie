#info groupe
#########################################
# MPCI TD3
# équipe 2
# Lalasoa RATOVONDRANTO
# Maxime DANNEVILLE
# Elias SAUVAGE 
# El Fahad ASSOUMANI (absent)
# https://github.com/uvsq22000372/projet_terrain
#########################################

#import librairies
import tkinter as tk
import random as rd


#definition constantes
COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
coul_eau = ["dodgerblue2"]
coul_terre = ["burlywood3"]
coul_bordure =["grey60"]


#definition variables globales 
nombre_eau = []
nombre_terre = []
l_carré = []
bordure = []
ListeTropGenial = []
mouv_sauv = []

nb_case = 50
COTE = 13
LARGEUR = COTE*(nb_case + 2)
HAUTEUR = LARGEUR
n = 4
k = 1
counter = 0
T = 5
p = 0.5
x = 0
c = 0
lgt1 = 0
rep = 0
z = 0
b = 2 * k
l = nb_case + b
nb_bonhomme = 0


#definition des fonctions

def Carre():
    """création de carré d'eau pour la taille du terrain  initial"""
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
    """creation du terrain avec les cases d'eau et de terre selon 
        la probabilité de présence de l'eau, ainsi qu'une bordure"""
    global nombre_terre, nombre_eau, bordure

    for i in range(len(l_carré)):
        if  (int(l_carré[i]) <= l + rep or int(l_carré[i]) > (l**2 - l) + rep or int((l_carré[i]) - 1) % l 
                - nb_bonhomme == 0 or int(l_carré[i]) % l - nb_bonhomme == 0):
            canvas.itemconfig((l_carré[i]) , fill=coul_bordure[0])
            bordure.append(l_carré[i])
    
        r = rd.randint(0, 100)
        if (r > p*100  and int(l_carré[i]) > l + rep and int(l_carré[i]) <= (l**2 - l) 
                + rep and int((l_carré[i]) - 1) % l - nb_bonhomme != 0 and 
                int(l_carré[i]) % l - nb_bonhomme != 0):
            canvas.itemconfig((l_carré[i]) , fill=coul_terre[0])
            nombre_eau.remove(l_carré[i])
            nombre_terre.append(l_carré[i])
            

def tri():
    """tri les fonctions (normalement pas nécessaire, est au cas où)"""
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


def Bonhomme():
    """création du personnage, défini par un cercle rouge"""
    global c
    global nb_bonhomme
    lgt = 0
    dx = COTE
    dy = COTE
    while lgt != 1:
        for i in range(len(l_carré)):
            if l_carré[i] in nombre_terre:
                x0, y0, x1, y1 = canvas.coords(l_carré[i]) 
                bonhomme = canvas.create_oval(x0,y0, x1, y1,fill="red", width=0)
                c = i
                lgt = 1
                nb_bonhomme += 1
                break
    return [bonhomme, dx, dy]
            

def automate():
    """automate, avec definitions du nombres de cases terre/eau dans le voisinage"""
    global counter, nombre_terre, nombre_eau, ListeTropGenial, x
    canvas.delete(automate)
    for y in range(n):
        for i in range(len(l_carré)):

            if l_carré[i] in nombre_terre: 

                if (int(l_carré[i]) > l + rep and int(l_carré[i]) <= (l**2 - l) + rep and 
                    int((l_carré[i]) - 1) % l - nb_bonhomme != 0 and int(l_carré[i]) % l 
                    - nb_bonhomme != 0):

                    if (l_carré[i+k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-l]) in nombre_eau:
                        counter += 1
                    if (l_carré[i+l]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-l+k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i+l+k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i-l-k]) in nombre_eau:
                        counter += 1
                    if (l_carré[i+l-k]) in nombre_eau:
                        counter += 1
                    if counter >= T:
                        ListeTropGenial.append(l_carré[i])
                        counter = 0
                    if counter < T:
                        counter = 0

            if l_carré[i] in nombre_eau: 

                if (int(l_carré[i]) > l + rep and int(l_carré[i]) <= (l**2 - l) + rep and 
                        int((l_carré[i]) - 1) % l - nb_bonhomme != 0 and 
                        int(l_carré[i]) % l - nb_bonhomme != 0):
                    if (l_carré[i+k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-l]) in nombre_terre:
                        counter += 1
                    if (l_carré[i+l]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-l+k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i+l+k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i-l-k]) in nombre_terre:
                        counter += 1
                    if (l_carré[i+l-k]) in nombre_terre:
                        counter += 1
                    if counter >= T:
                        ListeTropGenial.append(l_carré[i])
                        counter = 0
                    if counter < T:
                        counter = 0
        ChangementDeCoul()


def ChangementDeCoul():
    """réutilise ce qu'à donner l'automate et change chaque case ciblé en son inverse"""
    global ListeTropGenial, x
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


def deplacementHaut(event):
    """déplacement vers le haut"""
    global c 
    if l_carré[c - 52 ] in nombre_terre:
        canvas.move(bonhomme[0], 0, -bonhomme[2])
        c -= 52
        mouv_sauv.append("z")
    

def deplacementBas(event):
    """déplacement vers le bas"""
    global c 
    if l_carré[c + 52] in nombre_terre:
        canvas.move(bonhomme[0], 0, bonhomme[2])
        c += 52
        mouv_sauv.append("s")


def deplacementGauche(event):
    """déplacement vers la gauche"""
    global c
    if l_carré[c - 1] in nombre_terre:
        canvas.move(bonhomme[0], -bonhomme[1],0)
        c -= 1
        mouv_sauv.append("q")


def deplacementDroite(event):
    """déplacement vers la droite"""
    global c
    if l_carré[c + 1] in nombre_terre:
        canvas.move(bonhomme[0], bonhomme[1],0)
        c += 1
        mouv_sauv.append("d")


def PlacementSouris(event):
    """Placement du personnage"""
    global bonhomme
    global c
    global lgt1
    global nb_bonhomme
    global mouv_sauv

    I = str(canvas.find_closest(event.x, event.y)) 
    i1 = int(I[I.find('(') + 1 : I.find( ',')])
    i2 = int(I[I.find('(') + 1 : I.find( ',')]) - rep
    dx = COTE
    dy = COTE

    if lgt1 == 1 and l_carré[i2 - 1] in nombre_terre:
        x0, y0, x1, y1 = canvas.coords(l_carré[i2 - 1]) 
        bonhomme = canvas.create_oval(x0,y0, x1, y1,fill="red", width=0)
        bonhomme = [bonhomme, dx, dy]
        c = i2 - 1
        nb_bonhomme += 1
        lgt1 = 0

    if bonhomme != []:
        if i1 == bonhomme[0] and lgt1 != 1:
            canvas.delete(bonhomme[0])
            bonhomme = []
            mouv_sauv = []
            lgt1 += 1
    else:
        pass
    

def RetourArriere():
    """retour en arrière a l'aide d'une liste de sauvegarde des mouvement."""
    global c
    global bonhomme
    global mouv_sauv

    if mouv_sauv == []:
        pass

    elif mouv_sauv[-1] == "z":
        canvas.move(bonhomme[0], 0, bonhomme[2])
        c += 52
        del mouv_sauv[-1]
    elif mouv_sauv[-1] == "q":
        canvas.move(bonhomme[0], bonhomme[1],0)
        c += 1
        del mouv_sauv[-1]
    elif mouv_sauv[-1] == "s":
        canvas.move(bonhomme[0], 0, -bonhomme[2])
        c -= 52
        del mouv_sauv[-1]
    elif mouv_sauv[-1] == "d":
        canvas.move(bonhomme[0], -bonhomme[1],0)
        c -= 1
        del mouv_sauv[-1]


def Redemarrage():
    """Fonction qui redémarre le programme avec les nouvels valeur des curseurs. """
    global counter, nombre_terre, nombre_eau, l_carré, bonhomme, mouv_sauv
    global lgt1, bordure, n, k, p, T, LARGEUR, HAUTEUR, rep, z, l, b, x, c

    canvas.delete("all")

    nombre_eau = []
    nombre_terre = []
    l_carré = []
    bordure = []
    mouv_sauv = []
    bonhomme = []

    nb_case = 50
    COTE = 13
    LARGEUR = COTE*(nb_case + 2)
    HAUTEUR = LARGEUR 
    n = curseur_nombre_repetitions.get()
    k = 1
    counter = 0
    T = curseur_nombre_eau.get()
    p = curseur_proba_eau.get()
    x = 0
    c = 0
    lgt1 = 0
    z += 1
    rep = (l**2)* z + nb_bonhomme
    b = 2 * k
    l = nb_case + b

    Carre()
    creation_terrain()
    automate()
    bonhomme = Bonhomme()


def sauvegarder():
    """Sauvegarde les valeurs du tableau dans le fichier sauvegarde.txt"""
    fic = open("sauvegarde_terrain.txt", "w")
    fic.write(str(nombre_terre) + '\n' + '\n')
    fic.write(str(nombre_eau) + '\n' + '\n')
    fic.write(str(l_carré))
    fic.close()


def charger():
    """Charger le fichier sauvegarde_terrain.txt pour modifier le terrain"""
    #fic = open("sauvegarde_terrain.txt", "r")
    #canvas.delete("all")
    #Carre()
    #for i in range(len(l_carré)):
        #if l_carré[i] in nombre_terre[i]:
            #print("yes")
    pass


########################
# programme principal
racine = tk.Tk()
racine.title("Generation de terrain")
texte_nombre_répétitions = tk.Label (text = "nombre répétitions", font = "1")
texte_nombre_répétitions.grid(row=1, column=1)


# texte et boutons 
BoutonRetour = tk.Button(racine, text = "Retour", command=RetourArriere, fg = "white", bg = "black", font = ("helvetica", "10"))
BoutonRestart = tk.Button(racine,text = "Redémarrer", command = Redemarrage, fg = "white", bg = "black", font = ("helvetica, 10"))
bout_sauv = tk.Button(racine, text="sauvegarder", command=sauvegarder, fg = "white", bg = "black", font = ("helvetica, 10"))
bout_charge = tk.Button(racine, text="charger", command=charger, fg = "white", bg = "black", font = ("helvetica, 10"))


texte_proba_eau = tk.Label (text = "proba eau", font = "1")
texte_proba_eau.grid(row=11, column=1)

texte_nombre_eau = tk.Label (text = "nombre eau", font = "1")
texte_nombre_eau.grid(row=21, column=1)

# texte des curseurs optionnel (liés aux curseurs optionnels)

# texte_distance_moore = tk.Label (text = "distance Moore", font = "1")
# texte_distance_moore.grid(row=41, column=1)

# texte_dimensions = tk.Label (text = "nombre de case jouable", font = "1")
# texte_dimensions.grid(row=31, column=1)


# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR, bd = -2)
canvas.grid(row=0, column=0, rowspan=50)


# positionnement
canvas.grid()
bout_sauv.grid(row=42, column=1)
bout_charge.grid(row=39, column=1)
BoutonRetour.grid(row=45, column=1)
BoutonRestart.grid(row=48, column=1)


# curseurs
curseur_nombre_eau = tk.Scale(orient = "horizontal", variable=T, from_=0, to=8, length=100)
curseur_nombre_eau.set(5)
curseur_nombre_eau.grid(row=22, column=1)


curseur_proba_eau = tk.Scale(orient = "horizontal", variable=p, from_=0.10, to=0.90, resolution=0.01, length=100)
curseur_proba_eau.set(0.5)
curseur_proba_eau.grid(row=12, column=1)

curseur_nombre_repetitions = tk.Scale(orient = "horizontal", variable=n, from_=0, to=10, length=100)
curseur_nombre_repetitions.set(4)
curseur_nombre_repetitions.grid(row=2, column=1)


# Curseur optionnel (apporte trop de conflit, à approfondir)

# curseur_dimensions = tk.Scale(orient = "horizontal", variable=nb_case, from_=30, to=70, resolution=0, length=100)
# curseur_dimensions.set(50)
# curseur_dimensions.grid(row=32, column=1)

# curseur_distance_moore = tk.Scale(orient = "horizontal", variable=k, from_=1, to=10, length=100)
# curseur_distance_moore.set(1)
# curseur_distance_moore.grid(row=42, column=1)


# appels de fonctions
Carre()
creation_terrain()
automate()
bonhomme = Bonhomme()


# gestion des événements
racine.bind("z", deplacementHaut)
racine.bind("s", deplacementBas)
racine.bind("q", deplacementGauche)
racine.bind("d", deplacementDroite)
racine.bind('<Button-1>', PlacementSouris)


# boucle principal
racine.mainloop()