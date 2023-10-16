import pygame
from pygame.locals import *
from constante import *
from fonts import affiche
from player import Epouvantail
from math import sin, pi


def start(display, pressed_keys, state, events) :
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
		global alice, lapin, epouvantails, frame
		alice = Epouvantail(3*largeur_fenetre//10, hauteur_fenetre//4, "A")
		lapin = Epouvantail(largeur_fenetre - 4*largeur_fenetre//10, hauteur_fenetre//4, "L")
		epouvantails = [alice, lapin]
		frame = [0,0]
		return ("start","chooseCharacter")


	if state == "chooseCharacter" :
		affiche(display, ["ChoixPerso"])
		for i in range(len(epouvantails)) :
			perso = epouvantails[i]
			perso.agrandit( sin(2*pi*frame[i])/75, "centré") #on modifie la taille (initialisée à chaque tick)
			if perso.mouseOn() :
				frame[i] -= 0.02
				perso.agrandit(sin(2*pi*frame[i])/75, "centré")
			if perso.getClicked()[0] :
				return("start","switch")
			perso.dessine(display)
			frame[i] += 0.02
		
		if pressed_keys[K_UP] :
			return ("start","switch")
		return ("start","chooseCharacter")

	
	if state == "switch" :
		return ("charging","init")