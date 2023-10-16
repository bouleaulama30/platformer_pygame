import pygame
from pygame.locals import *
from constante import *


basic = "umpush"
def affiche(display, mot) :
	police = {
    "basic" : pygame.font.SysFont(basic, 70),
    "wonder" : pygame.font.SysFont("z003", 175),
    "little_basic" : pygame.font.SysFont(basic, 35)}
	
	if "WelcomeInWonderland" in mot:
		font = police["basic"]
		welcome = font.render("Welcome", True, white)
		welcome_h = welcome.get_height()
		welcome_posx = largeur_fenetre//2 - welcome.get_width()//2
		welcome_posy = hauteur_fenetre//2.5 - welcome_h
		display.blit(welcome, (welcome_posx, welcome_posy))

		in_ = font.render("in", True, white)
		in_h = in_.get_height()
		in_posx = largeur_fenetre//2 - in_.get_width()//2
		in_posy = welcome_posy + 0.5*welcome_h 
		display.blit(in_, (in_posx, in_posy))

		font = police["wonder"]
		wonderland = font.render("Wonderland", True, pink)
		#wonderland_h = wonderland.get_height()
		wonderland_posx = largeur_fenetre//2 - wonderland.get_width()//2
		wonderland_posy = in_posy + 0.85*in_h
		display.blit(wonderland, (wonderland_posx, wonderland_posy))

	if "startEnter" in mot :
		font = police["little_basic"]
		warn = font.render("press enter to start", True, gris)
		warn_posx = largeur_fenetre - warn.get_width()*1.1
		warn_posy = hauteur_fenetre - warn.get_height()*1.1
		display.blit(warn, (warn_posx, warn_posy))
	
	if "ChoixPerso" in mot :
		font = police["basic"]
		choix = font.render("Choose your character", True, white)
		choix_posx = largeur_fenetre//2 - choix.get_width()//2
		choix_posy = 0.6*choix.get_height()
		display.blit(choix, (choix_posx, choix_posy))