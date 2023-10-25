import pygame
from pygame.locals import *
##Attention, quadrillage = 40 blocs * 80 blocs
hauteur_fenetre = 800
largeur_fenetre = hauteur_fenetre*2
len_bloc = hauteur_fenetre/40
longueur_saut = 2*len_bloc

#couleurs
white = (255, 255, 255)
black = (0,0,0)
gris = (150,150,150)
rouge = (255, 0,0)
pink = (255,20,147)

#initialisation collisions
rep = (False, "")

#constantes qui influencent la physique du player
g=2000 #gravité
facteur_mvt=200 #influence vitesse déplacement
vel_jump=-800 #influence le saut

#définition des images blocs, histoire que le code soit lisible...
blocFill = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_fill.png"), (len_bloc, len_bloc))

blocSlip = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_slip.png"), (len_bloc, len_bloc))
blocSlip_NO = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_slip_NO.png"), (len_bloc, len_bloc))
blocSlip_NE = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_slip_NE.png"), (len_bloc, len_bloc))
blocSlip_SO = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_slip_SO.png"), (len_bloc, len_bloc))
blocSlip_SE = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_slip_SE.png"), (len_bloc, len_bloc))

blocNeutral = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_neutral.png"), (len_bloc, len_bloc))
blocNeutral_NO = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_neutral_NO.png"), (len_bloc, len_bloc))
blocNeutral_NE = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_neutral_NE.png"), (len_bloc, len_bloc))
blocNeutral_SO = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_neutral_SO.png"), (len_bloc, len_bloc))
blocNeutral_SE = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_neutral_SE.png"), (len_bloc, len_bloc))

blocJump = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_jump.png"), (len_bloc, len_bloc))
blocJump_NO = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_jump_NO.png"), (len_bloc, len_bloc))
blocJump_NE = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_jump_NE.png"), (len_bloc, len_bloc))
blocJump_SO = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_jump_SO.png"), (len_bloc, len_bloc))
blocJump_SE = pygame.transform.scale(pygame.image.load("SpritesBlocks/bloc_jump_SE.png"), (len_bloc, len_bloc))

dicoBlocSkins = {"n" : {'rect' : blocNeutral, 'SO' : blocNeutral_SO, 'NO' : blocNeutral_NO, 'SE' : blocNeutral_SE, 'NE' : blocNeutral_NE}, 
                 "j" : {'rect' : blocJump, 'SO' : blocJump_SO, 'NO' : blocJump_NO, 'SE' : blocJump_SE, 'NE' : blocJump_NE},
                 "s" : {'rect' : blocSlip, 'SO' : blocSlip_SO, 'NO' : blocSlip_NO, 'SE' : blocSlip_SE, 'NE' : blocSlip_NE},
                 "f" : {'rect' : blocFill, 'SO' : blocFill, 'NO' : blocFill, 'SE' : blocFill, 'NE' : blocFill}}

#de même, def des images persos
AliceStill_left = pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_still_left.png"), (1*len_bloc, 2*len_bloc))
AliceStill_right = pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_still_right.png"), (1*len_bloc, 2*len_bloc))
AliceRun_right = pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_run_right.png"), (1*len_bloc, 2*len_bloc))
AliceRun_left = pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_run_left.png"), (1*len_bloc, 2*len_bloc))
AliceJump_left = pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_jump_left.png"), (1*len_bloc, 2*len_bloc))
AliceJump_right = pygame.transform.scale(pygame.image.load("SpritesPlayer/Alice/alice_jump_right.png"), (1*len_bloc, 2*len_bloc))

LapinStill_left = pygame.transform.scale(pygame.image.load("SpritesPlayer/Lapin/lapin_still_left.png"), (1*len_bloc, 2*len_bloc))
LapinStill_right = pygame.transform.scale(pygame.image.load("SpritesPlayer/Lapin/lapin_still_right.png"), (1*len_bloc, 2*len_bloc))
LapinRun_right = pygame.transform.scale(pygame.image.load("SpritesPlayer/Lapin/lapin_run_right.png"), (1*len_bloc, 2*len_bloc))
LapinRun_left = pygame.transform.scale(pygame.image.load("SpritesPlayer/Lapin/lapin_run_left.png"), (1*len_bloc, 2*len_bloc))
LapinJump_left = pygame.transform.scale(pygame.image.load("SpritesPlayer/Lapin/lapin_jump_left.png"), (1*len_bloc, 2*len_bloc))
LapinJump_right = pygame.transform.scale(pygame.image.load("SpritesPlayer/Lapin/lapin_jump_right.png"), (1*len_bloc, 2*len_bloc))

persoTest = pygame.transform.scale(pygame.image.load("SpritesBackground/background_circular.jpg"), (1*len_bloc, 2*len_bloc))

#def des images background
bg_play1 = pygame.transform.scale(pygame.image.load("SpritesBackground/background_sombre.jpg"), (largeur_fenetre, hauteur_fenetre))
bg_play2 = pygame.transform.scale(pygame.image.load("SpritesBackground/background_key.jpg"), (largeur_fenetre, hauteur_fenetre))
bg_play3 = pygame.transform.scale(pygame.image.load("SpritesBackground/background_tiles.jpg"), (largeur_fenetre, hauteur_fenetre))
bg_play4 = pygame.transform.scale(pygame.image.load("SpritesBackground/background_cartesEtThe.jpg"), (largeur_fenetre, hauteur_fenetre))
bg_play5 = pygame.transform.scale(pygame.image.load("SpritesBackground/background_hearts.jpg"), (largeur_fenetre, hauteur_fenetre))
bg_fall = pygame.transform.scale(pygame.image.load("SpritesBackground/background_circular.jpg"), (largeur_fenetre, hauteur_fenetre))
bg_choix = pygame.transform.scale(pygame.image.load("SpritesBackground/ecran_choix/ecran_choix_none.jpg"), (largeur_fenetre, hauteur_fenetre))