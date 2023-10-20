from constante import *
from sounds import *

class Player: 

    def __init__(self, posx, posy, perso):
        self.posx= posx
        self.posy= posy
        self.w = 1*len_bloc
        self.h = 2*len_bloc
        self.dy= 300
        self.character = perso #"A" pour Alice, "L" pour Lapin
        self.vely=0
        self.is_grounded=False
        self.K_r_pressed=False

        if perso == "A" :
            self.skin = {"still_left" : AliceStill_left, "still_right":AliceStill_right, "run_right" : AliceRun_right, "run_left" : AliceRun_left, "jump_left" : AliceJump_left, "jump_right":AliceJump_right}
        elif perso == "L" :
            self.skin = {"still_left" : LapinStill_left, "still_right":LapinStill_right, "run_right" : LapinRun_right, "run_left" : LapinRun_left, "jump_left" : LapinJump_left, "jump_right":LapinJump_right}
        elif perso == "persoTest" :
            self.skin = {"still_left" : persoTest, "still_right":persoTest, "run_right" : persoTest, "run_left" : persoTest, "jump_left" : persoTest, "jump_right":persoTest}
        else :
            print("character undefined")
            exit()
        self.image= self.skin["still_left"]
        
        self.coll = [False, False, False, ""]
        self.collisionPrecedente = [False, False, False, ""]

    def is_colliding(self, t_blocks):
        l=[False,False,False, ""] #l = [isColliding, isJumping, isSlipping, "shapeCollided"]
        if self.offlimits() :
            return [True, False, False, "rect"]
        
        for b in t_blocks:
            if self.posx < b.posx + b.w and self.posx + self.w > b.posx and self.posy < b.posy + b.h and self.posy + self.h > b.posy:
                if not b.isTriangle :
                    if b.type=='j':
                        l=[True, True, False, "rect"]
                        return l
                    elif b.type=='s':
                        l=[True, False, True, "rect"]
                    else:
                        l=[True, False, False, "rect"]
                        return l
                    
                elif b.orientation == "NE" :
                    if not (self.posx + self.w < b.posx + (self.posy - b.posy)  and  (self.posy > b.posy + b.h - (self.posx + self.w - b.posx))) :
                        l=[True, False, False, "NE"]
                        return l
                elif b.orientation == "NO" :
                    if not (self.posx > b.posx + b.w - (self.posy - b.posy) and self.posy > b.posy + b.h - (self.posx - b.posx)) :
                        l=[True, False, False, "NO"]
                        return l
                elif b.orientation == "SE" :
                    if not (self.posx + self.w < b.posx + b.w - (self.posy - b.posy) and self.posy+self.h > b.posy - self.posx + self.w - b.posx) :
                        l=[True, False, False, "SE"]
                        return l
                elif b.orientation == "SO" :
                    if not (self.posx > b.posx + (self.posy + self.h - b.posy) and self.posy + self.h < b.posy + self.posx - b.posx) :
                        l=[True, False, False, "SO"]
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
        
        if pressed_keys[K_r]:
            self.posx, self.posy=50,10
            self.vely=0
            self.is_grounded=False
            play('R_is_pressed')
        
        if (pressed_keys[K_UP] or pressed_keys[K_SPACE]) and self.is_grounded :
            self.vely= -800
            play('jump')
        
        #teste déplacement x
        depx*=dt
        self.posx+=depx
        collisionPenultieme = self.collisionPrecedente
        self.collisionPrecedente = self.coll
        self.coll = self.is_colliding(t_blocks)
        if self.coll[0]:
            self.posx-=depx
            if self.coll[3] != "rect" :
                if self.coll[3] == "NO" :
                    self.posy += abs(self.vely)*dt
                elif self.coll[3] == "NE" :
                    self.posy += abs(self.vely)*dt
                elif self.coll[3] == "SO" :
                    self.posy -= abs(self.vely)*dt
                elif self.coll[3] == "SE" :
                    self.posy -= abs(self.vely)*dt
            #Mais s'il se tape un rectangle, c'est peut-être qu'il était sur un triangle avant et devrait continuer à glisser
            #Urgh, il y a aussi le cas où il s'est retrouvé en l'air juste pendant 1 frame
            elif (self.collisionPrecedente[0] and self.collisionPrecedente[3] != "rect") or (not self.collisionPrecedente[0] and collisionPenultieme[0] and collisionPenultieme[3] != "rect") :
                if self.collisionPrecedente[3] == "NO" :
                    self.posy += abs(self.vely)*dt
                elif self.collisionPrecedente[3] == "NE" :
                    self.posy += abs(self.vely)*dt
                elif self.collisionPrecedente[3] == "SO" :
                    self.posy -= abs(self.vely)*dt
                elif self.collisionPrecedente[3] == "SE" :
                    self.posy -= abs(self.vely)*dt

                
                    
        #teste déplacement y
        self.is_grounded=False
        self.posy += self.vely*dt
        self.coll = self.is_colliding(t_blocks)
        
        #pour le jump du champignon
        if self.coll[1]: 
            self.vely= -800
            self.vely+=2000*dt
            self.posy+=self.vely*dt
            play('rebond')
        
        self.coll = self.is_colliding(t_blocks)
        #pour la glace
        if self.coll[2]: 
            if self.image == self.skin["still_right"] or self.image == self.skin["run_right"] or self.image == self.skin["jump_right"]:
                if depx!=0:
                    self.posx-=depx
                self.posx+=facteur_r*dt/3  
            else:
                if depx!=0:
                    self.posx-= depx
                self.posx-= facteur_r*dt/3
        
        self.coll = self.is_colliding(t_blocks)   
        if self.coll[0]:
            self.is_grounded= True
            self.posy-=self.vely*dt
            if self.coll[3] != "rect" :
                if self.coll[3] == "NO" :
                    self.posx += abs(self.vely)*dt
                elif self.coll[3] == "NE" :
                    self.posx -= abs(self.vely)*dt
                elif self.coll[3] == "SO" :
                    self.posx += abs(self.vely)*dt
                elif self.coll[3] == "SE" :
                    self.posx -= abs(self.vely)*dt
            #Mais s'il se tape un rectangle, c'est peut-être qu'il était sur un triangle avant et devrait continuer à glisser
            #Urgh, il y a aussi le cas où il s'est retrouvé en l'air juste pendant 1 frame
            #Il y a aussi le cas triangle -> coin rectangle -> air -> coin rectangle, mais franchement flemme
            #Faudrait s'y prendre d'une autre manière...
            elif (self.collisionPrecedente[0] and self.collisionPrecedente[3] != "rect") or (not self.collisionPrecedente[0] and collisionPenultieme[0] and collisionPenultieme[3] != "rect") :
                if self.collisionPrecedente[3] == "NO" :
                    self.posy += abs(self.vely)*dt
                elif self.collisionPrecedente[3] == "NE" :
                    self.posy += abs(self.vely)*dt
                elif self.collisionPrecedente[3] == "SO" :
                    self.posy -= abs(self.vely)*dt
                elif self.collisionPrecedente[3] == "SE" :
                    self.posy -= abs(self.vely)*dt
            else :
                self.vely*=0
        
            #normalement, il ne devrait plus rien toucher
            #S'il était en train de collide avec la tête, il ne faut pas qu'il soit grounded ! Testons ça
            self.posy -= 2000*dt #on le remonte un poil
            if self.is_colliding(t_blocks)[0] :
                self.is_grounded = False
            self.posy += 2000*dt #on le redescend à l'état avant-test
        
        
        
        #gère les changements de skins pendant/juste après un saut
        if not self.is_grounded :
            if self.image == self.skin["jump_right"] or self.image == self.skin["run_right"] or self.image == self.skin["still_right"] :
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
    
    def offlimits(self) :
        """
        retourne True si le player est hors de l'écran
        """
        if self.posx < 0 or self.posy < 0 or self.posx + self.w > largeur_fenetre or self.posy + self.h >= hauteur_fenetre :
            return True
        return False
		
class Epouvantail:
    def __init__(self, posx, posy, skin):
        self.posx = posx
        self.posy = posy
        self.posx_init = posx
        self.posy_init = posy
        self.taille = [largeur_fenetre//6, largeur_fenetre//3]
        self.character = skin
        if self.character == "A" :
            self.imagePATH = "SpritesPlayer/Alice/alice_still_left.png"
            self.centre = [self.posx + self.taille[0]*255/564, self.posy+self.taille[1]*579/1128]
        elif self.character == "L" :
            self.imagePATH = "SpritesPlayer/Lapin/lapin_still.png"
            self.centre = [0,0]
        else :
            print("Epouvantail : Perso non défini")
            exit()
    
    def getClicked(self) :
        """ return [bool, self.type]"""
        if pygame.mouse.get_pressed()[0] :
            collideBox = pygame.Rect(self.posx, self.posy, self.taille[0], self.taille[1])
            if collideBox.collidepoint(pygame.mouse.get_pos()) :
                return (True, self.character)
        return (False, "")
    
    def mouseOn(self) :
        m_posx, m_posy = pygame.mouse.get_pos()
        collideBox = pygame.Rect(self.posx, self.posy, self.taille[0], self.taille[1])
        if collideBox.collidepoint(m_posx, m_posy) :
            return True
        return False
    
    def dessine(self, display) :
        self.image = pygame.transform.scale(pygame.image.load(self.imagePATH), self.taille)
        display.blit(self.image, (self.posx, self.posy))
        
    def agrandit(self, facteur, pos = "coin") :
        self.tailleInit()
        if pos == "centré" :
            centre = (self.posx + self.taille[0]//2, self.posy + self.taille[1]//2)
            self.taille[0] *= 1+facteur
            self.taille[1] *= 1+facteur
            
            self.posx = centre[0] - self.taille[0]//2
            self.posy = centre[1] - self.taille[1]//2
        
        elif pos == "centrePerso" :
            vieilleTaille = self.taille
            self.taille[0] *= 1+facteur
            self.taille[1] *= 1+facteur
            self.posx = self.centre[0] - (self.centre[0]-self.posx)/vieilleTaille[0]*self.taille[0]
            self.posy = self.centre[1] - (self.centre[1]-self.posy)/vieilleTaille[1]*self.taille[1]
        
        elif pos == "coin" :
            self.taille[0] *= 1+facteur
            self.taille[1] *= 1+facteur
            
    def tailleInit(self) :
        self.taille = [largeur_fenetre//6, largeur_fenetre//3]
        self.posx = self.posx_init 
        self.posy = self.posy_init
        