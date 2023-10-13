from constante import *


class Player: 

    def __init__(self, posx, posy,dy, perso):
        self.posx= posx
        self.posy= posy
        self.w = 1*len_bloc
        self.h = 2*len_bloc
        self.dy= dy
        self.character = perso #"A" pour Alice, "L" pour Lapin
        self.vely=0
        self.is_grounded=False

        if perso == "A" :
            self.skin = {"still_left" : AliceStill_left, "still_right":AliceStill_right, "run_right" : AliceRun_right, "run_left" : AliceRun_left, "jump_left" : AliceJump_left, "jump_right":AliceJump_right}
        elif perso == "L" :
            self.skin = {"still_left" : LapinStill_left, "still_right":LapinStill_right, "run_right" : LapinRun_right, "run_left" : LapinRun_left, "jump_left" : LapinJump_left, "jump_right":LapinJump_right}
        else :
            print("character undefined")
            exit()
        self.image= self.skin["still_left"]

    def is_colliding(self, t_blocks):
        for b in t_blocks:
            if self.posx < b.posx + b.w and self.posx + self.w > b.posx and self.posy < b.posy + b.h and self.posy + self.h > b.posy:
                return True
        return False

    def deplacement(self,facteur_l,facteur_r, dt, pressed_keys, t_blocks):

        depx= 0
        self.vely+=2000*dt
        
        if pressed_keys[K_RIGHT]:
            depx += facteur_r
            self.image = self.skin["run_right"]
        elif self.image == self.skin["still_right"] or self.image == self.skin["run_right"] :
            self.image = self.skin["still_right"]	

        if pressed_keys[K_LEFT]:
            depx-= facteur_l
            self.image = self.skin["run_left"]
        elif self.image == self.skin["still_left"] or self.image == self.skin["run_left"] :
            self.image = self.skin["still_left"]
        depx*=dt
        self.posx+=depx
        if self.is_colliding(t_blocks):
            self.posx-=depx

        self.is_grounded=False
        self.posy+= self.vely *dt
        if self.is_colliding(t_blocks):
            self.is_grounded= True
            self.posy-=self.vely*dt
            self.vely*=0
        
		
    def dessine(self, display) :
        display.blit(self.image, (self.posx, self.posy))
		
