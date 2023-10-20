import pygame
from pygame.locals import *

pygame.mixer.init()

musics = {
        'welcome' : "sons/mysterious_alice_theme.mp3",
        "quadrille" : "sons/rebond_troll.mp3",
        "explore" :"sons/welcome_to_wonderland.mp3",
        "end" : "sons/welcome_to_wonderland.mp3",
        'rebond': "sons/rebond_troll.mp3"
}

sounds = {
        'rebond': pygame.mixer.Sound("sons/rebond_troll.mp3"),
        'jump': pygame.mixer.Sound("sons/jump_troll.mp3"),
        'R_is_pressed': pygame.mixer.Sound("sons/R_is_pressed.mp3")
}


def play(name):
        sounds[name].play()

def play_bg(name) :
        pygame.mixer.music.load(musics[name])
        pygame.mixer.music.play(-1)