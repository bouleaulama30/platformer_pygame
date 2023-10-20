import pygame
from pygame.locals import *
from constante import *
from fonts import affiche
from player import Epouvantail
from math import sin, pi
from sounds import *


def start(display, pressed_keys, state, events) :
	if state == "init" :
		play_bg('welcome')
		affiche(display, "WelcomeInWonderland")
		global nbFrames, mot
		nbFrames = 0
		mot = ["WelcomeInWonderland"]
		return ("start","keepDisplayingFonts", "")


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
			return ("start","keepDisplayingFonts", "")
		nbFrames = 0
		return ("start","sw_chooseCharacter", "")


	if state == "sw_chooseCharacter" :
		global alice, lapin, epouvantails, frame
		alice = Epouvantail(3*largeur_fenetre//10, hauteur_fenetre//4, "A")
		lapin = Epouvantail(largeur_fenetre - 4*largeur_fenetre//10, hauteur_fenetre//4, "L")
		epouvantails = [alice, lapin]
		frame = [0,0]
		return ("start","chooseCharacter", "")


	if state == "chooseCharacter" :
		affiche(display, ["ChoixPerso"])
		for i in range(len(epouvantails)) :
			scarecrow = epouvantails[i]
			scarecrow.agrandit( sin(2*pi*frame[i])/75, "centré") #on modifie la taille (initialisée à chaque tick)
			if scarecrow.mouseOn() :
				frame[i] -= 0.02
				scarecrow.agrandit(sin(2*pi*frame[i])/75, "centré")
			isClicked, nameScarecrow = scarecrow.getClicked()
			if isClicked :
				return("start","switch", nameScarecrow)
			scarecrow.dessine(display)
			frame[i] += 0.02
		
		if pressed_keys[K_UP] :
			return ("start","switch", "")
		return ("start","chooseCharacter", "")

	if state == "switch" :
		pygame.mixer.music.fadeout(5)
		return ("charging","init", "")
