import pygame
from pygame.locals import *
from constante import *
from fonts import affiche
from player import Epouvantail
from math import sin, pi
from sounds import *


def start(display, pressed_keys, state, events) :
	if state == "init" :
		play_bg('mysterious_short')
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
		len_x = largeur_fenetre//6
		len_y = largeur_fenetre//3
		global alice, lapin, chat, epouvantails, frame, frameTot
		alice = Epouvantail(largeur_fenetre//4, hauteur_fenetre//2 + 75, "A")
		lapin = Epouvantail(largeur_fenetre//2, hauteur_fenetre//2 + 75, "L")
		chat = Epouvantail(3*largeur_fenetre//4, hauteur_fenetre//2 + 75, "C")
		epouvantails = [alice, lapin, chat]
		frame = [0,0,0]
		frameTot = 0
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
					global characChoisi
					characChoisi = nameScarecrow
					return("start","switch", characChoisi)
			elif frame[i] != frameTot :
				frame[i] =frameTot
			scarecrow.dessine(display)
			frame[i] += 0.02
		frameTot += 0.02
  
		if pressed_keys[K_UP] :
			characChoisi = "A"
			return ("start","switch", "")

		return ("start","chooseCharacter", "")
	

	if state == "switch" :
		arreteMusique()
		return ("charging","init", characChoisi)
