from constante import*


class Key:
    
    def __init__(self,posx,posy):
        self.posx=posx
        self.posy=posy
        self.image= key
        

    
    def dessine_key(self, display):
        display.blit(self.image, (self.posx, self.posy))



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
        loading_text=self.font.render(f"chargement {self.loading}%", True, (255,255,255))
        display.blit(loading_text, ((2.2/3)*largeur_fenetre,(7/8)*hauteur_fenetre))
        count = count + 1
        if count >5:
            self.add_loading()
            count=0
    
    def get_loading(self):
        return self.loading






    