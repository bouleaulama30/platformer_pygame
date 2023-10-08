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
#		self.image=  #à changer avec le sprite

	def move_right(self,facteur):
		if pressed_keys[K_RIGHT]:
			self.posx += facteur*dt

	def move_left(self,facteur):
		if pressed_keys[K_LEFT]:
			self.posx -= facteur*dt	
						
			
	def dessine(self) :
		pygame.draw.rect(display, (255,0,0), ((self.posx, self.posy), (self.w, self.h)))

class Block: 

	def __init__(self, posx, posy,type, triangle, orientation):
		self.posx= posx
		self.posy= posy
		self.w = 1*len_bloc
		self.h = 1*len_bloc
		self.type= type
		self.isTriangle = triangle
		self.orientation = orientation #le point cardinal definit le coin qui existe
		self.image= pygame.draw.rect(display, (255,0,0), ((posx, posy), (self.w, self.h)))


	def dessine(self) :
		if self.isTriangle :
			x = self.posx
			y = self.posy
			cote = self.w 
			no = (x, y)
			ne = (x+cote, y)
			se = (x+cote, y+cote)
			so = (x, y+cote)
			if self.orientation == "SO" :
				pygame.draw.polygon(display, (255,0,0), (no, so, se))

			elif self.orientation == "NO" :
				pygame.draw.polygon(display, (255,0,0), (no, so, ne))

			elif self.orientation == "NE" :
				pygame.draw.polygon(display, (255,0,0), (no, se, ne))

			elif self.orientation == "SE" :
				pygame.draw.polygon(display, (255,0,0), (so, se, ne))
				#print()

			else :
				print ("erreur definition triangle")

		else :
			pygame.draw.rect(display, (255,0,0), ((self.posx, self.posy), (self.w, self.h)))



display = pygame.display.set_mode((1366, 768)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre

last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


player= Player(10,10,300) #initialisation du joueur
block_test= Block(10,200,'n',False,'SE') #initialisation block test

### Creation des blocs

t_blocks = []

def make_gros_bloc (x, y, nb_h, nb_w, type) :
	# coin haut gauche, nb de bloc en hauteur, nb bloc en largeur, type
	for i  in range (nb_h) :
		for j in range (nb_w) :
			x_b = x + j * len_bloc 
			y_b = y + i * len_bloc
			t_blocks.append(Block(x_b, y_b, type, False, ""))

def make_gros_triangle (x, y, len_cote, type, orientation) :
	if orientation == "SO" :
		for i in range (1, len_cote) :
			for j in range (i) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, type, False, ""))
		for k in range (len_cote) :
			x_b = x + k * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))

	elif orientation == "NO" :
		for i in range (len_cote - 1) :
			for j in range (len_cote - i - 1) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, type, False, ""))
		for k in range (len_cote) :
			x_b = x + (len_cote - k - 1) * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))
	
	elif orientation == "NE" :
		for i in range (len_cote - 1) :
			for j in range (i + 1, len_cote) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, type, False, ""))
		for k in range (len_cote) :
			x_b = x + k * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))

	elif orientation == "SE" :
		for i in range (1, len_cote) : 
			for j in range (len_cote - i, len_cote) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, type, False, ""))
		for k in range (len_cote) :
			x_b = x + (len_cote - k - 1)  * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))

	else :
		print ("erreur creation gros bloc triangle")

def fill () :
	for b in t_blocks :
		b.dessine()


make_gros_bloc(600, 530, 6, 4, "n")
make_gros_triangle(100, 100, 3, "n", "SO")
make_gros_triangle(200, 200, 4, "n", "NO")
make_gros_triangle(300, 300, 5, "n", "SE")
make_gros_triangle(400, 400, 7, "n", "NE")

jump_count=0 #initialisation compteur de frame pour faire condition sur le jump
vel=800 #vitesse pour le jump arbitraire
contact=False #nécessaire pour jump (pour l'instant)

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
	


    #condition de contact test 
	if player.posy +player.w  >= block_test.posy and player.posx<=block_test.posx+100:
		player.dy=0
		contact= True
	else: 
		player.dy= 300
		contact=False
		


	if pressed_keys[K_UP] :
		player.posy-=vel*dt 
		jump_count+=1
		if jump_count>50: #condition sinon le jump est infini
			vel= -player.dy #on remet la gravité
			
	else:
		if contact:
			#on reset jump_count et vel pour pouvoir re jumper
			jump_count=0 
			vel=800
		player.posy+= player.dy*dt #gravité		



	
	# Ici se fera le calcul de la physique du jeu
	
	
	
	
	

	# Ici se fera le dessin de la scène
	block_test.dessine()
	player.dessine()

	#test fonction fill
	fill()

	#display.blit(player.image, (player.posx, player.posy))
	#player= Player(player.posx,player.posy,50,50,player.dy) #maj du joueur
	pygame.display.update() # Mise à jour de l'affichage 

pygame.quit() # important
