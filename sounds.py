import pygame
from pygame.locals import *

pygame.mixer.init()

sounds = {
        'rebond': pygame.mixer.Sound("sons/rebond_troll.mp3"),
        'jump': pygame.mixer.Sound("sons/jump_troll.mp3"),
        'R_is_pressed': pygame.mixer.Sound("sons/R_is_pressed.mp3")
}


def play (name):
    sounds[name].play()