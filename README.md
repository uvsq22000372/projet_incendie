# projet_terrain

Ce programme à pour but de créer un terrain de jeu vidéo aléatoire, réalisé en python avec Tkinter
Le personnage est automatiquement placé sur le premier carré de terre. 
Pour le déplacer sur un autre espace de terre, il faut cliquer (clic gauche de la souris) sur le cercel rouge. Cela le fait disparaitre. 
Pour le faire réapparaitre il suffit de cliquer (Clic gauche de la souris) sur un autre carré de terre (et comme pous pouvez vous en doutez, on ne peut pas le lacher dans l'eau). 

Une fois placé, le personnage se déplace grâce aux touches suivantes :
    z = vers le haut 
    s = vers le bas
    q = vers la gauche
    d = vers la droite

Il est possible de maintenir enfoncée ces touches pour un déplacement rapide et continu. 
Notre bonhomme rouge a la faculté de réfléchir, et donc en s'approchant d'une côte, ne va pas sauter dans l'eau.


Pour revenir en arrière, il y a un bouton "Retour" sur la droite de l'affichage. Celui-ci permet de revenir jusqu'à la toute première position du personnage si besoin.
Le changer de position remet a zéro son déplacement de sauvegarde.


##### Deux autres boutons permettent de sauvegarder le terrain actuel, et de charger le dernier terrain sauvegardé. (La sauvegarde fonctionne, mais nous n'avons pas réussi à faire fonctionner la recharge.)

Les 3 curseurs permettent de faire varier les paramètres du programme :

	Il y a le nombre de répétitions de l'automate (notée "nombre répétitions"), 
	la probabilité qu'une case soit de l'eau (notée "proba eau"), le nombre de cases d'eau nécessaire autour d'une case pour que celle-ci devienne de l'eau (notée 
	"nombre eau"), 

2 curseurs optionnels sont dans le programme (car trop conflictueux) permettant de modifier :

	la distance du voisinage de Moore (notée "distance Moore") et les dimensions du terrain (notée "dimensions terrain")




Explication plus détaillé du fonctionnement du programme:

	Tout d'abord, les variables sont assez complexes car, même en supprimant les canvas, leur tag initial (qui a été utilisé dans presque toute les fonctions) reste en
	mémoire.
	rep = (l**2)* z + nb_bonhomme correspond au nombre total de canvas créé tout au long du programme (permet de se synchroniser avec les tags, qui eux sont indépendant de
	la suppression des canvas.),
	avec l le nombre de case jouable + bordure, z le nombre de répétitions du redémarrage et nb_bonhomme le nombre de fois que le canvas bonhomme est créé (tout ceci 
	permettant donc de synchroniser les tags . 
	donc tout ce qui est en rapport avec la taille et leur tag est associé a ce rep.
	
	le programme repose sur l'utilisation de listes :
 	l_carré correspond a la liste de tout les carrés, eau comme terre; nombre_terre, comme vous l'aurez deviner, correspond au nombre de case de terre; nombre_eau a celle
	d'eau; et bordure celle des cases de bordure.
	ListeTropGénial (étant trop génial parce que c'est la liste qui fait tout marcher comme sur des roulettes) sera expliquer dans automate()

	Carre(): 

		C'est la base du terrain. C'est lui qui crée les carrés initiaux (en eau) qui sont ensuite modifier avec creation_terrain() et automate().
		Il crée des lignes de carré, et quand arrive au nombre de carré dans une ligne, saute la ligne, réitère, jusqu'à arriver au même nombre de case dans une ligne
		(le terraine est carré).
		La variable "nb_case" utilisé correspond au terrain jouable sans les bordure, et les lignes créant le carré comprend les bordures.

		Ces carrés sont un par un ajouté a la liste l_carré, nombre_eau (car tous eau initialement), et bordure. 
		Leur tag est rangé dans l'ordre de création (donc décroissant), donnant un ordore de balayage de gauche a droite et de haut en bas. (utiliser dans toute les
		fonctions qui précéderont)

	creation_terrain():
		
		C'est la fonction qui va crée un terrain aléatoire de case terre ou eau, variant avec p.
		on utiliser la fonction random.randint(100) de la librairie random qui nous sort un entier aléatoire de 0 a 100, et p (compris entre 0 et 1 d'après l'énoncé)
		correspond a la valeur seuil, décidant de si c'est une case eau ou terre.
		En effet, p est comme une barrière ici : ceux a droite de p sont eau, ceux a gauche sont terre ( a gauche = < et a droite = >, mathématiquement).

		Cette fonction créer la bordure et donc l'aléatoire entre eau et terre. Elle parcourt chaque carré, ligne par ligne, dans l'ordre de balayage imposé, grâce a
		leur numero de tag (la première ligne a ses tags de 0 à 

	tri():

		Cette fonction tri simplement par odre décroissant en ne laissant qu'une unique fois le tag. Cela empêche juste les bugs (car la taille des listes, et leur
		positions sont importantes.),
		même si normalement toute les listes sont censés être déjà sous cette forme.

	bonhomme():

		Cette fonction crée le bonhomme dés lors que dans son balayage, il croise une case terre, et prend les coordoonées de cette case terre.
	
	automate():

		Constitue le coeur, avec ChangementDeCoul(). C'est ce qui va crée le terrain jouable. 

		Il va balayé la liste de tout les carrées, et pour chaque carrés, va voir si pour chaque carrés voisin suivant le voisinage de Moore, il est de la terre ou de
		l'eau. 
		Si le carré étudié est de l'eau, et qu'il y a plus de T carré de terre, il devient de la terre, et inversement pour la terre.

		La bordure compte toujours comme une case du même type que le la case étudié (c'est une case "fantôme". Elle sert juste a créer un cas général du voisinage de
		Moore. 
		Car pour les carrés en bordure, il ne peut pas étudier des carrés qui sont hors de la liste, ou qui n'existe pas.)

		Quand une case doit être changé en terre, il l'incrémente dans la ListeTropGénial. Lorsque tout a été traité, ChangementDeCouleur opère.

	ChangementDeCouleur():
		
		C'est ce qui constitue les pâtes de automate(). Il va juste tout simplement rendre chaque case eau en case terre, et chaque case terre en case eau.
		Il était primordial de devoir le rendre indépendant du balayage, car sinon, comme le traitement est fait ligne par ligne et pas tout d'un coup, les lignes déja
		modifié rendait l'indentification fausse.
		Sans cette indépendance, le programme n'aurait jamais pus marché (c'est pourquoi cette list est trop génial).
	Deplacement(): 

		Chaque déplacement marche de la même forme : une direction par rapport a l'axe des pixels donné (de gauche à droite, et de bas en haut) comme base (dx, dy), où
		dx et dy = une case.
		On module le signe et si il est nulle pour chaque mouvement précis.
	RetourArrière():

		Chaque mouvement (désigné par sa lettre d'action) est incrémenté dans une liste, qui a donc les mouvement dans un odre temporel, 
		et quand on exprime la fonction. Elle va traiter la liste dans l'odre inverse, et lorsque qu'un mouvement, par exemple haut, est lu, 
		elle va éxecuter le mouvement inverse, donc ici bas, et supprimer le dernier mouvement dans la liste, pour pouvoir ensuite recommencer.

		Quand la liste est vide, la fonction est donce en pass, cela va de soit, et lorsqu'on déplace le personnage, on vide la liste, et donc on ne peut plus refaire
		les mouvement de retour en arrière.
	
	 Redemarrage():
		
		La fonction redémarre le programme avec les nouvels valeur des curseurs tout en supprimant tout canvas, et vidant toute liste. 
		Elle va aussi donc ajouté une rep, et un z a chaque fois que la fonction est lu. 
		Cela permet comm expliqué précédemment de pouvoir faire marcher le programme en tenant compte que les tag ne sont pas réinitialisé avec leur suppréssion.
