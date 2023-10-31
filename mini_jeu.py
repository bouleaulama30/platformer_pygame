from constante import*
from sounds import *


class Key:
    
    def __init__(self,posx,posy):
        self.posx=posx
        self.posy=posy
        self.w= len_bloc
        self.h= 2*len_bloc
        self.vel=200
        self.image= key
        self.touched=False
        self.score_increment=10

        
    def is_colliding_key(self, player):
        if self.posx < player.posx + player.w and self.posx + self.w > player.posx and self.posy < player.posy + player.h and self.posy + self.h > player.posy:  
            return True
    

    
    def dessine_and_move_key(self, display,player, update,dt):
        if (not self.is_colliding_key(player)) and self.touched==False  :
            self.posy-= self.vel*dt
            display.blit(self.image, (self.posx, self.posy))
        else:
            if self.touched == False:
                play("keys_sound")
                update.add_score(self.score_increment)
            self.touched=True
    
    
def create_random_key(keys_list):
    global count_rd_keys
    global influence_vitesse_creation
    count_rd_keys = count_rd_keys + 1
    if count_rd_keys >influence_vitesse_creation:
        rd_pox=rd.randint(int((1/3)*largeur_fenetre),int((2/3)*largeur_fenetre)-len_bloc)
        rd_posy=hauteur_fenetre
        keys_list.append(Key(rd_pox,rd_posy))
        count_rd_keys=0

def fill_keys(display,player,update,keys_list,dt):
    create_random_key(keys_list)
    for k in keys_list:
        k.dessine_and_move_key(display,player,update,dt)
    



class Update_mini_game:

    def __init__(self):
        self.score=0
        self.loading=0
        self.font= pygame.font.SysFont("z003", 50)
        

    def add_score(self,point):
        self.score+=point

    def add_loading(self):
        self.loading+=1

    def update_score(self,display):
        
        score_text=self.font.render(f"Score: {self.score}", True, (255,255,255))
        display.blit(score_text, (20,20))
      
        
    def update_loading(self, display):
        global count
        global influence_vitesse_chargement
        loading_text=self.font.render(f"chargement {self.loading}%", True, (255,255,255))
        display.blit(loading_text, ((2.2/3)*largeur_fenetre,(7/8)*hauteur_fenetre))
        count = count + 1
        if count >influence_vitesse_chargement:
            self.add_loading()
            count=0
    
    def get_loading(self):
        return self.loading






    