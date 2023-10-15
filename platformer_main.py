import pygame
from pygame.locals import *
from player import Player
from block import *
from constante import *
from sounds import *


#paramètres d'entrée
pygame.init() # important
font = pygame.font.SysFont("Z003", 70)
display = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre
background = bg_play4

# definir une clock
clock= pygame.time.Clock()
FPS = 200
last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)

#music
musics["welcome"]
pygame.mixer.music.play(-1)

#player
player= Player(50,10,300, "A") #initialisation du joueur
jump_count=0 #initialisation compteur de frame pour faire condition sur le jump
vel=800 #vitesse pour le jump arbitraire
g=5 #pour rendre jump plus  réaliste
facteur_r=100 #argument pour move_right 
facteur_l=100 #argument pour move_left


### Creation des blocs

t_blocks = []
make_gros_triangle(50, 200, 5, "n", "SO", t_blocks)
make_gros_bloc(40, 500, 2, 15, "s",t_blocks)
make_gros_bloc(150, 0, 2, 3, "s", t_blocks)
make_gros_bloc(400,400,1,3,"j", t_blocks)


		
etape = "start" #can be "play", "start", "end", "charging"
state = ""
# Boucle de rendu
end = False
while not end:
	for event in pygame.event.get():
		if event.type == QUIT: # vrai quand l'utilisateur essaye de fermer la fenêtre
			end = True

	display.fill(black) # remplit l'écran avec la couleur ((rouge, vert, bleu)) (entre 0 et 255)
	
	current_time = pygame.time.get_ticks() 
	dt = (current_time - last_time) / 1000.0 # dt = temps écoulé depuis la dernière frame en secondes
	last_time = pygame.time.get_ticks() # ne pas oublier de réinitialiser le chronomètre

	#traitement des entrées clavier
	pressed_keys = pygame.key.get_pressed()
	if etape == "start" :
		if state == "" :
			welcome = font.render("Welcome", True, white)
			welcome_h = welcome.get_height()
			welcome_posx = largeur_fenetre//2 - welcome.get_width()//2
			welcome_posy = hauteur_fenetre//2.5 - welcome_h
			display.blit(welcome, (welcome_posx, welcome_posy))
		
			in_ = font.render("in", True, white)
			in_h = in_.get_height()
			in_posx = largeur_fenetre//2 - in_.get_width()//2
			in_posy = welcome_posy + 1.2*welcome_h 
			display.blit(in_, (in_posx, in_posy))
   
			wonderland = font.render("Wonderland", True, pink)
			wonderland_h = wonderland.get_height()
			wonderland_posx = largeur_fenetre//2 - wonderland.get_width()//2
			wonderland_posy = in_posy + 1.2*in_h
			display.blit(wonderland, (wonderland_posx, wonderland_posy))
			pygame.display.update()
			pygame.time.wait(4*1000)
   
		state = "switch"
		if state == "switch" :
			etape = "charging"
			state = ""
			musics["quadrille"]
			pygame.mixer.music.play(-1)

	if etape == "charging" :
		state = "switch"
		if state == "switch" :
			etape = "play"
			state = ""
			musics["explore"]
			pygame.mixer.music.play(-1)
   
 
	if etape == "play" :
		player.deplacement(200,200, dt, pressed_keys, t_blocks)
		player.dy = 300

		# Ici se fera le dessin de la scène
		display.blit(background, (0,0))
		player.dessine(display)
	
		#test fonction fill
		fill(display, t_blocks)

	

	pygame.display.update() # Mise à jour de l'affichage 

	# fixer le nombre de fps sur ma clock
	clock.tick(FPS)


pygame.quit() # important
