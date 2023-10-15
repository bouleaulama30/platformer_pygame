import pygame
from pygame.locals import *
from constante import *
from fonts import affiche


def start(display, pressed_keys, state, t, dt) :
	if state == "init" :
		affiche(display, "WelcomeInWonderland")
		t = 0
		return ("start","keepDisplayingFonts", t)

	elif state == "keepDisplayingFonts" :
		if t < 5 and not pressed_keys[K_RETURN] :
			affiche(display, "WelcomeInWonderland")
			t += dt
			return ("start","keepDisplayingFonts", t)
		t = 0
		return ("start","chooseCharacter", t)

	if state == "chooseCharacter" :
		return ("start","switch", t)
	
	if state == "switch" :
		return ("charging","init", t)