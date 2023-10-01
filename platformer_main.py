import pygame
from pygame.locals import *



pygame.init() # important

#création class player
class Player: 

	def __init__(self, posx, posy,w,h):
		self.posx= posx
		self.posy= posy
		self.w =w
		self.h = h
		self.image= pygame.draw.rect(display, (255,0,0), ((posx, posy), (w, h))) 

	def move_right(self,facteur):
		if pressed_keys[K_RIGHT]:
			player.posx += facteur*dt

	def move_left(self,facteur):
		if pressed_keys[K_LEFT]:
			player.posx -= facteur*dt		

class Block: 

	def __init__(self, posx, posy,w,h,type):
		self.posx= posx
		self.posy= posy
		self.w =w
		self.h = h
		self.type= type
		self.image= pygame.draw.rect(display, (0,255,0), ((posx, posy), (w, h)))


vel=100 #importation vitesse (selon y), (à mettre dans classe?)

display = pygame.display.set_mode((1366, 768)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre

last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


player= Player(10,10,50,50) #initialisation du joueur
block_test= Block(10,500,100,100,'n') #initialisation block test




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
	player.move_right(100)
	player.move_left(100)
	

	
	# Ici se fera le calcul de la physique du jeu
	#condition de contact test 
	if player.posy +player.w  >= block_test.posy and player.posx<=block_test.posx+100:
		vel=0
	else: vel=100	
	
	player.posy+= vel*dt #gravité
	
	

	# Ici se fera le dessin de la scène
	block_test= Block(10,500,100,100,'n') #maj block
	player= Player(player.posx,player.posy,50,50) #maj du joueur
	pygame.display.update() # Mise à jour de l'affichage 

pygame.quit() # important

#Lyla a réussi son push
