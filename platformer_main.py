import pygame
from pygame.locals import *

import pygame
from pygame.locals import *


pygame.init() # important

display = pygame.display.set_mode((800, 800)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre

last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)

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

	pressed_keys = pygame.key.get_pressed()
	# Ici se fera le traitement des entrées clavier

	# Ici se fera le calcul de la physique du jeu

	# Ici se fera le dessin de la scène

	pygame.display.update() # Mise à jour de l'affichage 

pygame.quit() # important