import pygame
from pygame.locals import *
from player import Player
from block import *
from constante import *
from sounds import *
from mini_jeu import *
#from fonts import affiche
from decoupageFonctionnement import *
from editor_mode import *


#1 player = 2 blocs de haut

#paramètres d'entrée
pygame.init() # important
display = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre)) # crée une surface pour la fenêtre (largeur, hauteur) de la fenetre
background_game = bg_play4
background_mini_game= bg_fall

# definir une clock
clock= pygame.time.Clock()
FPS = 200
last_time = pygame.time.get_ticks() # Pour le comptage du temps (get_ticks() renvoie le temps actuel en millisecondes)


### Creation des blocs
t_blocks = []
# make_gros_triangle(0, 200, 5, "n", "SO", t_blocks)
# make_gros_bloc(0, 500, 2, 15, "n",t_blocks)
# make_gros_bloc(500, 500, 2, 15, "s",t_blocks)
# make_gros_bloc(400,400,1,3,"j", t_blocks)


read_file_map("blocks.txt",t_blocks,list_map_file)


update_mini_game= Update_mini_game()
key_list_ingame=[]
door_list_ingame =[]
keys_list=[]

read_file_keys("keys.txt",key_list_ingame,list_key_map_file)
read_file_door("door.txt",door_list_ingame,list_door_map_file)
		
etape = "start" #can be "play", "start", "end", "charging" , "mini_jeu"
"""
Hey Margot, ptit message pour tenter d'expliquer ce que j'ai amené avec mon merge (souffre)

la variable etape peut être "play", "start", "end", "charging", ... : permet de découper le jeu (et le code !) en morceaux distincts, indépendants et quasi autonomes 
par exemple le choix des personnages, l'écran de chargement avec quadrille du homard, le niveau de jeu, les crédits de fin...
Concrètement, à chaque itération du while, on teste si on est en train de faire telle ou telle étape, et on continue en conséquence

la variable state permet de définir des étapes dans les étapes : basiquement, on n'a besoin d'initialiser le Player qu'une seule fois, de démarrer la musique uniquement lors de la première itération
de l'étape, et d'éteindre la musique lors de la dernière itération... Mais on doit aussi afficher un texte pendant plusieurs frames, garder un suivi sur le player...
Le premier state d'une étape doit toujours être "init" (bah, parce que c'est là qu'on init les variables utilisées pendant l'étape), et son dernier state est défini comme "switch" (lors de ce dernier state par 
exemple on éteint la musique, mais surtout on change la valeur des variables etape et state pour enchainer sur le début d'une nouvelle étape). Y'aura besoin d'autres states,
mais ceux-là ont forcément des noms particuliers à chaque étape ^^

Je suppose que c'est pas très clair, je te réfère à la fonction start() dans decoupageFonctionnement.py pour voir comment c'est implémenté, et sinon n'hésite pas à m'appeler...
"""
etape = "start" 
state = "init"
# Boucle de rendu
end = False
while not end:
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT: # vrai quand l'utilisateur essaye de fermer la fenêtre
			end = True

	display.fill(black) # remplit l'écran avec la couleur ((rouge, vert, bleu)) (entre 0 et 255)
	
	current_time = pygame.time.get_ticks() 
	dt = (current_time - last_time) / 1000.0 # dt = temps écoulé depuis la dernière frame en secondes
	last_time = pygame.time.get_ticks() # ne pas oublier de réinitialiser le chronomètre

	#traitement des entrées clavier
	pressed_keys = pygame.key.get_pressed()
	if etape == "start" :
		etape, state, perso = start(display, pressed_keys, state, events)
		
	if etape == "charging" :
		if state == "init" :
			play_bg("quadrille")
			state = "switch"
		if state == "switch" :
			arreteMusique()
			etape = "mini_jeu"
			state = "init"

	if etape == "mini_jeu":
		if state == "init" :
			play_bg("bg_mini_jeu")
			play("wind_for_falling")
			player= Player(largeur_fenetre/2,(hauteur_fenetre/3)-2*len_bloc,perso)
			display.blit(background_mini_game, (0,0)) 
			player.dessine_deplacement_mini_jeu(display,pressed_keys,facteur_mvt_mini_jeu,dt,state)
			state="ongoing"
			vel_fall = 0
		
		display.blit(background_mini_game, (0,0))
		if state == "ongoing" :
			player.posy += 0.1 #tombe leeentement
			fill_keys(display,player,update_mini_game,keys_list,dt,etape)

		if update_mini_game.get_loading()>=100:
			vel_fall += g*dt/30
			player.posy += 0.1 + vel_fall*dt #accélère la chute quand il faut finir le chargement...
			fill_keys_fin(display,player,update_mini_game,keys_list,dt,etape) #arrête de générer de nouvelles clés
			state = "finishing"

		if player.posy >= hauteur_fenetre :
			state = "switch"
		update_mini_game.update_score(display)
		update_mini_game.update_loading(state,display)
		player.dessine_deplacement_mini_jeu(display,pressed_keys,facteur_mvt_mini_jeu,dt,state)
		if pressed_keys[K_b] or state == "switch" :
			etape="play"
			state="init"
			stop_sound("wind_for_falling")
			arreteMusique()

	
 
	if etape == "play" :

		
		if state == "init" :
			if perso == "" : #petite protection à enlever quand tout sera bien codé
							 #perso == "" si rien n'a été sélectionné pendant l'étape du choix (étape start)
				perso = "persoTest"
			play_bg("tea")
			player= Player(50,15, perso) #initialisation du joueur
			state = "ongoing"
		player.deplacement(facteur_mvt, vel_jump, dt, pressed_keys, t_blocks, g)
		# Ici se fera le dessin de la scène
		display.blit(background_game, (0,0))
		player.dessine(display)
		fill_keys(display,player,update_mini_game,key_list_ingame,dt,etape)
		fill_door(display,door_list_ingame)
		update_mini_game.update_score(display)
		fill(display, t_blocks)
		if pressed_keys[K_e]:
			etape= "editor_mode"
			state= "init"
			
			
		



	if etape == "editor_mode":
		if state=='init':
			state='ongoing'

		if pressed_keys[K_n] and editor_count>20:
			state='n'
			write_file_map("blocks.txt",state)
			state='ongoing'
			editor_count=0
		if pressed_keys[K_j] and editor_count>20:
			state='j'
			write_file_map("blocks.txt",state)
			state='ongoing'
			editor_count=0
		if pressed_keys[K_s] and editor_count>20:
			state='s'
			write_file_map("blocks.txt",state)
			state='ongoing'
			editor_count=0

		if pressed_keys[K_f] and editor_count>20:
			state='f'
			write_file_map("blocks.txt",state)
			state='ongoing'
			editor_count=0
		
		#pour les blocks triangles (oui c'est moche)
		#pour les triangles 'n'
		if pressed_keys[K_0] and editor_count>20:
			state='n'
			write_file_map("blocks.txt",state,True,"SO")
			state='ongoing'
			editor_count=0
			
		if pressed_keys[K_1] and editor_count>20:
			state='n'
			write_file_map("blocks.txt",state,True,"NO")
			state='ongoing'
			editor_count=0
			
		if pressed_keys[K_2] and editor_count>20:
			state='n'
			write_file_map("blocks.txt",state,True,"NE")
			state='ongoing'
			editor_count=0

		if pressed_keys[K_3] and editor_count>20:
			state='n'
			write_file_map("blocks.txt",state,True,"SE")
			state='ongoing'
			editor_count=0

		#pour les triangles 's'
		if pressed_keys[K_4] and editor_count>20:
			state='s'
			write_file_map("blocks.txt",state,True,"SO")
			state='ongoing'
			editor_count=0
			
		if pressed_keys[K_5] and editor_count>20:
			state='s'
			write_file_map("blocks.txt",state,True,"NO")
			state='ongoing'
			editor_count=0
			
		if pressed_keys[K_6] and editor_count>20:
			state='s'
			write_file_map("blocks.txt",state,True,"NE")
			state='ongoing'
			editor_count=0

		if pressed_keys[K_7] and editor_count>20:
			state='s'
			write_file_map("blocks.txt",state,True,"SE")
			state='ongoing'
			editor_count=0


		#pour les triangles 'j'
		if pressed_keys[K_8] and editor_count>20:
			state='j'
			write_file_map("blocks.txt",state,True,"SO")
			state='ongoing'
			editor_count=0
			
		if pressed_keys[K_9] and editor_count>20:
			state='j'
			write_file_map("blocks.txt",state,True,"NO")
			state='ongoing'
			editor_count=0
			
		if pressed_keys[K_a] and editor_count>20:
			state='j'
			write_file_map("blocks.txt",state,True,"NE")
			state='ongoing'
			editor_count=0

		if pressed_keys[K_z] and editor_count>20:
			state='j'
			write_file_map("blocks.txt",state,True,"SE")
			state='ongoing'
			editor_count=0



		if pressed_keys[K_k] and editor_count>20:
			write_file_keys("keys.txt")
			editor_count=0
		if pressed_keys[K_SPACE] and editor_count>20:
			write_file_door("door.txt")
			print("ok")
			editor_count=0
			


		#pour le déplacement de la souris avec les flèches directionnelles
		if pressed_keys[K_RIGHT] and editor_count>15:
			move_right_mouse(len_bloc)
			editor_count=0
		if pressed_keys[K_LEFT] and editor_count>15:
			move_left_mouse(len_bloc)
			editor_count=0
		if pressed_keys[K_UP] and editor_count>15:
			move_up_mouse(len_bloc)
			editor_count=0
		if pressed_keys[K_DOWN] and editor_count>15:
			move_down_mouse(len_bloc)
			editor_count=0
		if pressed_keys[K_r] and editor_count>15:
			reset_mouse()
			editor_count=0

		if pressed_keys[K_d] and editor_count>15:
			delete_line_file_map("blocks.txt",t_blocks,list_map_file)
			editor_count=0
		
		if pressed_keys[K_y] and editor_count>15:
			delete_line_file_keys("keys.txt",key_list_ingame,list_key_map_file)
			editor_count=0
		
		if pressed_keys[K_RETURN] and editor_count>15:
			delete_line_file_door("door.txt",door_list_ingame,list_door_map_file)
			editor_count=0


		if pressed_keys[K_p]:
			etape = "play"
			state= "ongoing"
		
		
		read_file_keys("keys.txt",key_list_ingame,list_key_map_file)
		read_file_map("blocks.txt",t_blocks,list_map_file)
		read_file_door("door.txt", door_list_ingame,list_door_map_file)
		
		display.blit(bg_edition, (0,0))
		fill_keys(display,player,update_mini_game,key_list_ingame,dt,etape)
		fill_door(display, door_list_ingame)
		fill(display, t_blocks)
		editor_count+=1
		editor_count_read_file_map+=1




	



	pygame.display.update() # Mise à jour de l'affichage 

	# fixer le nombre de fps sur ma clock
	clock.tick(FPS)


pygame.quit() # important

