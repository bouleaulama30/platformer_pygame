from constante import *
from sounds import *


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
        elif perso == "blocTest" :
            self.skin = {"still_left" : persoTest, "still_right":persoTest, "run_right" : persoTest, "run_left" : persoTest, "jump_left" : persoTest, "jump_right":persoTest}
        else :
            print("character undefined")
            exit()
        self.image= self.skin["still_left"]

    def is_colliding(self, t_blocks):
        l=[False,False,False]
        for b in t_blocks:
            if self.posx < b.posx + b.w and self.posx + self.w > b.posx and self.posy < b.posy + b.h and self.posy + self.h > b.posy:
                if not b.isTriangle :
                    if b.type=='j':
                        l=[True,True,False]
                        return l
                    if b.type=='s':
                        l=[True,False,True]
                    else:
                        l=[True,False,False]
                        return l
                    
                elif b.orientation == "NE" :
                    if not (self.posx + self.w < b.posx + (self.posy - b.posy)  and  (self.posy > b.posy + b.h - (self.posx + self.w - b.posx))) :
                        l=[True,False,False]
                        return l
                elif b.orientation == "NO" :
                    if not (self.posx > b.posx + b.w - (self.posy - b.posy) and self.posy > b.posy + b.h - (self.posx - b.posx)) :
                        l=[True,False,False]
                        return l
                elif b.orientation == "SE" :
                    if not (self.posx + self.w < b.posx + b.w - (self.posy - b.posy) and self.posy+self.h > b.posy - self.posx + self.w - b.posx) :
                        l=[True,False,False]
                        return l
                elif b.orientation == "SO" :
                    if not (self.posx > b.posx + (b.posy + b.h  - (self.posy + self.h)) and self.posy + self.h < b.posy + self.posx - b.posx) :
                        l=[True,False,False]
                        return l
        return l

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
        if self.is_colliding(t_blocks)[1]:
            self.posx-=depx

        self.is_grounded=False
        
        
        
        self.posy+= self.vely *dt
        
        #pour le jump du champignon
        if self.is_colliding(t_blocks)[1]: 
            self.vely=-800
            self.vely+=2000*dt
            self.posy+=self.vely*dt
            play('rebond')
            
            

        #pour la glace
        if self.is_colliding(t_blocks)[2]: 
            if self.image == self.skin["still_right"] or self.image == self.skin["run_right"] or self.image == self.skin["jump_right"]:
                if depx!=0:
                    self.posx-=depx
                self.posx+=facteur_r*dt/3  
            else:
                if depx!=0:
                    self.posx-= depx
                self.posx-= facteur_r*dt/3

        
        if self.is_colliding(t_blocks)[0]:
            self.is_grounded= True
            self.posy-=(self.vely*dt)
            self.vely*=0
            

        if pressed_keys[K_r]:
            self.posx, self.posy=50,10
            self.vely=0
            self.is_grounded=False
        
        if not self.is_grounded :
            if (self.image == self.skin["jump_right"] or self.image == self.skin["run_right"] or self.image == self.skin["still_right"]) :
                self.image = self.skin["jump_right"]
            else :
                self.image = self.skin["jump_left"]
        else :
            if self.image == self.skin["jump_left"] :
                self.image = self.skin["still_left"]
            elif self.image == self.skin["jump_right"] :
                self.image = self.skin["still_right"]
        
        
		
    def dessine(self, display) :
        display.blit(self.image, (self.posx, self.posy))
		
