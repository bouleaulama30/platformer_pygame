import pygame
from pygame.locals import *
from player import Player
from block import *
from constante import *
from sounds import *
#from fonts import affiche
from decoupageFonctionnement import *

#1 player = 2 blocs de haut

#paramètres d'entrée
pygame.init() # important
display = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre
background = bg_play4

# definir une clock
clock= pygame.time.Clock()
FPS = 200
last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


### Creation des blocs
t_blocks = []
make_gros_triangle(50, 200, 5, "n", "SO", t_blocks)
make_gros_bloc(40, 500, 2, 15, "n",t_blocks)
make_gros_bloc(500, 500, 2, 15, "s",t_blocks)
make_gros_bloc(150, 0, 2, 3, "n", t_blocks)
make_gros_bloc(400,400,1,3,"j", t_blocks)


		
etape = "start" #can be "play", "start", "end", "charging" , "mini_jeu"
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
			play_bg("tea")
			player= Player(50,10,perso)
			state="ongoing"
		display.blit(background, (0,0))
		player.dessine(display)
		if pressed_keys[K_b]:
			etape="play"
			state="init"
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
		display.blit(background, (0,0))
		player.dessine(display)
	
		#test fonction fill
		fill(display, t_blocks)


	pygame.display.update() # Mise à jour de l'affichage 

	# fixer le nombre de fps sur ma clock
	clock.tick(FPS)


pygame.quit() # important

