import pygame
from pygame.locals import *
from player import Player
from block import *
from constante import *
from sounds import *




#1 player = 2 blocs de haut

pygame.init() # important
# definir une clock
clock= pygame.time.Clock()
FPS = 200


display = pygame.display.set_mode((1366, 768)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre
background = pygame.transform.scale(pygame.image.load("SpritesBackground/background_key.jpg"), (largeur_fenetre, hauteur_fenetre))


last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


player= Player(50,10,300, "persoTest") #initialisation du joueur

jump_count=0 #initialisation compteur de frame pour faire condition sur le jump
vel=800 #vitesse pour le jump arbitraire
g=5 #pour rendre jump plus  réaliste
facteur_r=100 #argument pour move_right 
facteur_l=100 #argument pour move_left


### Creation des blocs

t_blocks = []
make_gros_triangle(50, 200, 5, "n", "SO", t_blocks)
make_gros_bloc(40, 400, 2, 15, "s",t_blocks)
make_gros_bloc(150, 0, 2, 3, "s", t_blocks)
make_gros_bloc(250,400,1,3,"j", t_blocks)


		

# Boucle de rendu
end = False
while not end:
	for event in pygame.event.get():
		if event.type == QUIT: # vrai quand l'utilisateur essaye de fermer la fenêtre
			end = True

	display.fill((250, 250, 250)) # remplit l'écran avec la couleur ((rouge, vert, bleu)) (entre 0 et 255)
	
	current_time = pygame.time.get_ticks() 
	dt = (current_time - last_time) / 1000.0 # dt = temps écoulé depuis la dernière frame en secondes
	last_time = pygame.time.get_ticks() # ne pas oublier de réinitialiser le chronomètre

	#traitement des entrées clavier
	pressed_keys = pygame.key.get_pressed()
	player.deplacement(200,200, dt, pressed_keys, t_blocks)
	
	player.dy = 300

    #condition de contact test 
	#collision()

	if (pressed_keys[K_UP] or pressed_keys[K_SPACE]) and player.is_grounded :
		player.vely= -800
		play('jump')
	
	


	
	# Ici se fera le calcul de la physique du jeu
	
	
	
	
	

	# Ici se fera le dessin de la scène
	display.blit(background, (0,0))
	player.dessine(display)
	

	
	#test fonction fill
	fill()

	#display.blit(player.image, (player.posx, player.posy))
	#player= Player(player.posx,player.posy,50,50,player.dy) #maj du joueur
	pygame.display.update() # Mise à jour de l'affichage 

	# fixer le nombre de fps sur ma clock
	clock.tick(FPS)

pygame.quit() # important
