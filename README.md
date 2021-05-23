# projet_terrain

Ce programme à pour but de créer un terrain de jeu vidéo aléatoire, réalisé en python avec Tkinter
Le personnage est automatqiuement placé sur le premier carré de terre. Pour le déplacer sur un autre espace de terre, il faut cliquer (clic gauche de la souris) sur sa tête, représentée par un cercle rouge. Cela le fait disparaitre. Pour le faire réapparaitre il suffit de cliquer (Clic gauche de la souris) sur un carré de terre. 

Une fois placé, le personnage se déplace grâce aux touches suivantes :
    z = vers le haut 
    s = vers le bas
    q = vers la gauche
    d = vers la droite

Il est possible de maintenir enfoncée ces touches pour un déplpacement rapide et continu. 
Pour revenir en arrière, il y a un bouton "Retour" sur la droite de l'affichage. Celui-ci permet de revenir jusqu'à la toute première position du personnage (après clic) si besoin. 

Deux autres boutons permettent de sauvegarder le terrain actuel, et de charger le dernier terrain sauvegardé. 

Les 5 curseurs permettent de faire varier les paramètres du programme. Il y a le nombre de répétitions de l'automate (notée "nombre répétitions"), la probabilité qu'une case soit de l'eau (notée "proba eau"), le nombre de cases d'eau nécessaire autour d'une case "i" pour que celle-ci devienne de l'eau (notée "nombre eau"), la distance du voisinage de Moore (notée "distance Moore") et les dimensions du terrain (notée "dimensions terrain")