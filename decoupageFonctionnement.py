import pygame
from pygame.locals import *
from constante import *
from fonts import affiche


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
		return ("start","chooseCharacter")

	if state == "chooseCharacter" :
		return ("start","switch")
	
	if state == "switch" :
		return ("charging","init")