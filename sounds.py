import pygame
from pygame.locals import *

pygame.mixer.init()

musics = {
        "welcome" : pygame.mixer.music.load("sons/welcome_to_wonderland.mp3")
}

sounds = {
        'rebond': pygame.mixer.Sound("sons/rebond.mp3"),
        'jump': pygame.mixer.Sound("sons/jump.mp3"),
        'R_is_pressed': pygame.mixer.Sound("sons/R_is_pressed.mp3")
}


def play (name):
    sounds[name].play()