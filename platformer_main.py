import pygame
from pygame.locals import *


##Attention, quadrillage = 40 blocs * 80 blocs
hauteur_fenetre = 800
largeur_fenetre = hauteur_fenetre*2
len_bloc = hauteur_fenetre/40
longueur_saut = 2*len_bloc
#1 player = 2 blocs de haut

pygame.init() # important

#création class player
class Player: 

	def __init__(self, posx, posy,dy):
		self.posx= posx
		self.posy= posy
		self.w = 1*len_bloc
		self.h = 2*len_bloc
		self.dy= dy
		self.image= pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_run.png"), (1*len_bloc, 2*len_bloc))

	def move_right(self,facteur):
		if pressed_keys[K_RIGHT]:
			self.posx += facteur*dt

	def move_left(self,facteur):
		if pressed_keys[K_LEFT]:
			self.posx -= facteur*dt		
		
	def dessine(self) :
		display.blit(self.image, (self.posx, self.posy))
		#pygame.draw.rect(display, (255,0,0), ((self.posx, self.posy), (self.w, self.h)))

class Block: 

	def __init__(self, posx, posy,type, triangle, orientation):
		self.posx= posx
		self.posy= posy
		self.w = 1*len_bloc
		self.h = 1*len_bloc
		self.type= type
		self.isTriangle = triangle
		self.orientation = orientation #le point cardinal definit le coin qui existe par exemple bloc.orientation = "NE"
		self.image= pygame.draw.rect(display, (0,255,0), ((posx, posy), (self.w, self.h)))


	def dessine(self) :
		pygame.draw.rect(display, (255,0,0), ((self.posx, self.posy), (self.w, self.h)))



display = pygame.display.set_mode((1366, 768)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre

last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


player= Player(10,10,100) #initialisation du joueur
block_test= Block(10,500,False,"",'n') #initialisation block test




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
		player.dy=0
	else: player.dy= 100	
	
	player.posy+= player.dy*dt #gravité
	
	

	# Ici se fera le dessin de la scène
	block_test= Block(10,500,100,100,'n') #maj block
	block_test.dessine()
	player.dessine()
	#display.blit(player.image, (player.posx, player.posy))
	#player= Player(player.posx,player.posy,50,50,player.dy) #maj du joueur
	pygame.display.update() # Mise à jour de l'affichage 

pygame.quit() # important
