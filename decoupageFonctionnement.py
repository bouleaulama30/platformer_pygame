import pygame
from pygame.locals import *
from constante import *
from fonts import affiche
from player import Epouvantail
from math import sin, pi


def start(display, pressed_keys, state) :
	if state == "init" :
		affiche(display, "WelcomeInWonderland")
		global nbFrames
		nbFrames = 0
		global mot 
		mot = ["WelcomeInWonderland"]
		return ("start","keepDisplayingFonts")

	elif state == "keepDisplayingFonts" :
		if nbFrames>=100 :
			if len(mot) == 1 :
				mot = ["WelcomeInWonderland", "startEnter"]
			else :
				mot = ["WelcomeInWonderland"]
			nbFrames = 0
		if not pressed_keys[K_RETURN] :
			nbFrames+=1
			affiche(display, mot)
			return ("start","keepDisplayingFonts")
		nbFrames = 0
		return ("start","sw_chooseCharacter")
	if state == "sw_chooseCharacter" :
		global alice, lapin
		alice = Epouvantail(3*largeur_fenetre//10, hauteur_fenetre//4, "A")
		lapin = Epouvantail(largeur_fenetre - 4*largeur_fenetre//10, hauteur_fenetre//4, "L")
		return ("start","chooseCharacter")
	if state == "chooseCharacter" :
		affiche(display, ["ChoixPerso"])
		alice.agrandit( sin(2*pi*nbFrames)/40, "centré") #on modifie la taille (initialisée à chaque tick)
		lapin.agrandit( sin(2*pi*nbFrames)/40, "centré" )

		


		alice.dessine(display)
		lapin.dessine(display)
		print(alice.taille)
		if pressed_keys[K_UP] :
			return ("start","switch")
		nbFrames += 0.03
		return ("start","chooseCharacter")

	
	if state == "switch" :
		return ("charging","init")