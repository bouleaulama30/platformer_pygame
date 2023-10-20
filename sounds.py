import pygame
from pygame.locals import *

pygame.mixer.init()

musics = {
        'welcome' : "sons/mysterious_alice_theme.mp3",
        "quadrille" : "sons/quadrille_des_homards.mp3",
        "explore" :"sons/welcome_to_wonderland.mp3",
        "end" : "sons/welcome_to_wonderland.mp3",
        'rebond': "sons/rebond_troll.mp3"
}

"""
pour exporter sons youtube :
1) https://notube.io/fr/youtube-app-v102
2) https://clideo.com/fr/cut-audio
"""
sounds = {
        'rebond': pygame.mixer.Sound("sons/rebond_troll.mp3"),
        'jump': pygame.mixer.Sound("sons/jump_troll.mp3"),
        'R_is_pressed': pygame.mixer.Sound("sons/R_is_pressed.mp3")
}


def play(name):
        sounds[name].set_volume(0.9)
        sounds[name].play()

def play_bg(name) :
        pygame.mixer.music.load(musics[name])
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)