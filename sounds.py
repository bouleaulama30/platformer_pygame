import pygame
from pygame.locals import *

pygame.mixer.init()

musics = {
        "mysterious" : "sons/mysterious_alice_theme.mp3",
        "mysterious_short" : "sons/mysterious_alice_theme_SHORTENED.mp3",
        "quadrille" : "sons/quadrille_des_homards.mp3",
        "tea" : "sons/mad_tea_party.mp3",
        "explore" :"sons/welcome_to_wonderland.mp3",
        "end" : "sons/welcome_to_wonderland.mp3",
        'rebond': "sons/rebond_troll.mp3",
        "bg_mini_jeu": "sons/bg_mini_jeu.mp3",
        "wind_for_falling": "sons/wind_for_falling.mp3"
}

"""
pour exporter sons youtube :
1) https://notube.io/fr/youtube-app-v102
2) https://clideo.com/fr/cut-audio
"""
sounds = {
        'rebond': pygame.mixer.Sound("sons/rebond.mp3"),
        'jump': pygame.mixer.Sound("sons/jump.mp3"),
        'R_is_pressed': pygame.mixer.Sound("sons/R_is_pressed.mp3"),
        'running_grass': pygame.mixer.Sound("sons/running_grass.mp3"),
        'ice_slid': pygame.mixer.Sound("sons/ice_slid.mp3"),
        'keys_sound':pygame.mixer.Sound("sons/keys_sound2.mp3"),
        "wind_for_falling": pygame.mixer.Sound("sons/wind_for_falling.mp3")

}


def play(name, channel=-1):
        sounds[name].set_volume(1)
        if channel==-1:
                if name =='rebond':
                        sounds[name].set_volume(0.2) 
                
                if name == "wind_for_falling":
                        sounds[name].set_volume(0.2)         
                
                sounds[name].play()  
        
        else:
                pygame.mixer.Channel(channel).play(sounds[name])

def stop_sound(name):
        sounds[name].set_volume(0)
                
        
#pour voir si le channel est encombrer
def is_playing(channel):
        return pygame.mixer.Channel(channel).get_busy()

def play_bg(name) :
        pygame.mixer.music.load(musics[name])
        pygame.mixer.music.set_volume(0.1) #c'était 0.3
        pygame.mixer.music.play(-1)

def arreteMusique() :
        pygame.mixer.music.fadeout(5)