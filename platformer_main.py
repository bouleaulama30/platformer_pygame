import pygame
from pygame.locals import *
from player import Player
from block import *
from constante import *
from sounds import *
from mini_jeu import *
#from fonts import affiche
from decoupageFonctionnement import *


#1 player = 2 blocs de haut

#paramètres d'entrée
pygame.init() # important
display = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre
background_game = bg_play4
background_mini_game= bg_fall

# definir une clock
clock= pygame.time.Clock()
FPS = 200
last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


### Creation des blocs
t_blocks = []
make_gros_triangle(0, 200, 5, "n", "SO", t_blocks)
make_gros_bloc(0, 500, 2, 15, "n",t_blocks)
make_gros_bloc(500, 500, 2, 15, "s",t_blocks)
make_gros_bloc(400,400,1,3,"j", t_blocks)


update_mini_game= Update_mini_game()
keys_list=[]
		
etape = "start" #can be "play", "start", "end", "charging" , "mini_jeu"
"""
Hey Margot, ptit message pour tenter d'expliquer ce que j'ai amené avec mon merge (souffre)

la variable etape peut être "play", "start", "end", "charging", ... : permet de découper le jeu (et le code !) en morceaux distincts, indépendants et quasi autonomes 
par exemple le choix des personnages, l'écran de chargement avec quadrille du homard, le niveau de jeu, les crédits de fin...
Concrètement, à chaque itération du while, on teste si on est en train de faire telle ou telle étape, et on continue en conséquence

la variable state permet de définir des étapes dans les étapes : basiquement, on n'a besoin d'initialiser le Player qu'une seule fois, de démarrer la musique uniquement lors de la première itération
de l'étape, et d'éteindre la musique lors de la dernière itération... Mais on doit aussi afficher un texte pendant plusieurs frames, garder un suivi sur le player...
Le premier state d'une étape doit toujours être "init" (bah, parce que c'est là qu'on init les variables utilisées pendant l'étape), et son dernier state est défini comme "switch" (lors de ce dernier state par 
exemple on éteint la musique, mais surtout on change la valeur des variables etape et state pour enchainer sur le début d'une nouvelle étape). Y'aura besoin d'autres states,
mais ceux-là ont forcément des noms particuliers à chaque étape ^^

Je suppose que c'est pas très clair, je te réfère à la fonction start() dans decoupageFonctionnement.py pour voir comment c'est implémenté, et sinon n'hésite pas à m'appeler...
"""
etape = "start" 
state = "init"
# Boucle de rendu
end = False
while not end:
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT: # vrai quand l'utilisateur essaye de fermer la fenêtre
			end = True

	display.fill(black) # remplit l'écran avec la couleur ((rouge, vert, bleu)) (entre 0 et 255)
	
	current_time = pygame.time.get_ticks() 
	dt = (current_time - last_time) / 1000.0 # dt = temps écoulé depuis la dernière frame en secondes
	last_time = pygame.time.get_ticks() # ne pas oublier de réinitialiser le chronomètre

	#traitement des entrées clavier
	pressed_keys = pygame.key.get_pressed()
	if etape == "start" :
		etape, state, perso = start(display, pressed_keys, state, events)
		
	if etape == "charging" :
		if state == "init" :
			play_bg("quadrille")
			state = "switch"
		if state == "switch" :
			arreteMusique()
			etape = "mini_jeu"
			state = "init"

	if etape == "mini_jeu":
		if state == "init" :
			play_bg("bg_mini_jeu")
			play("wind_for_falling")
			player= Player(largeur_fenetre/2,(hauteur_fenetre/3)-2*len_bloc,perso)
			display.blit(background_mini_game, (0,0)) 
			player.dessine_deplacement_mini_jeu(display,pressed_keys,facteur_mvt_mini_jeu,dt,state)
			state="ongoing"
			vel_fall = 0
		
		display.blit(background_mini_game, (0,0))
		if state == "ongoing" :
			player.posy += 0.1 #tombe leeentement
			fill_keys(display,player,update_mini_game,keys_list,dt)

		if update_mini_game.get_loading()>=100:
			player.posy += 0.7 #accélère la chute quand il faut finir le chargement...
			fill_keys_fin(display,player,update_mini_game,keys_list,dt) #arrête de générer des clés
			state = "finishing"

		if player.posy >= hauteur_fenetre :
			state = "switch"
		update_mini_game.update_score(display)
		update_mini_game.update_loading(state,display)
		player.dessine_deplacement_mini_jeu(display,pressed_keys,facteur_mvt_mini_jeu,dt,state)
		if pressed_keys[K_b] or state == "switch" :
			etape="play"
			state="init"
			stop_sound("wind_for_falling")
			arreteMusique()

	
 
	if etape == "play" :
		if state == "init" :
			if perso == "" : #petite protection à enlever quand tout sera bien codé
							 #perso == "" si rien n'a été sélectionné pendant l'étape du choix (étape start)
				perso = "persoTest"
			play_bg("tea")
			player= Player(50,10, perso) #initialisation du joueur
			state = "ongoing"
		player.deplacement(facteur_mvt, vel_jump, dt, pressed_keys, t_blocks, g)
		# Ici se fera le dessin de la scène
		display.blit(background_game, (0,0))
		player.dessine(display)
		update_mini_game.update_score(display)
		
	
		#test fonction fill
		fill(display, t_blocks)


	pygame.display.update() # Mise à jour de l'affichage 

	# fixer le nombre de fps sur ma clock
	clock.tick(FPS)


pygame.quit() # important

