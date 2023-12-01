from constante import *

class Block: 

	def __init__(self, posx, posy,type, triangle, orientation):
		self.posx= posx
		self.posy= posy
		self.w = 1*len_bloc
		self.h = 1*len_bloc
		self.type= type #should be 'n'(neutral), 's'(slip),'j'(jump), 'f' (fill)
		self.isTriangle = triangle
		self.orientation = orientation #le point cardinal définit le coin qui existe

		if self.type in ["n", "j", "s", "f","p"] :
			if self.isTriangle :
				if (self.orientation in ["SO", "NO", "SE", "NE"]) :
					self.image = dicoBlocSkins[self.type][self.orientation]
				else :
					print("erreur def Triangle")
					exit()
			else :
				self.image = dicoBlocSkins[self.type]["rect"]
		else :
			print("erreur def Type bloc")
			exit()
		
		#nécessaire pour condition de contact triangle
		if self.orientation == "SO" :
			self.pts = ((self.posx, self.posy), (self.posx + self.w, self.posy + self.h), (self.posx, self.posy + self.h))
			self.pts_rec = [(0,1), (0,0), (1,0), (1,0)]
			self.condInt = [True, False]
		elif self.orientation == "NE" :
			self.pts = ((self.posx, self.posy), (self.posx + self.w, self.posy + self.h), (self.posx+ self.w, self.posy))
			self.pts_rec = [(1,0), (0,1), (0,0), (1,1)]
			self.condInt = [False, True]
		elif self.orientation == "SE" :
			self.pts = ((self.posx + self.w, self.posy), (self.posx + self.w, self.posy+self.h), (self.posx, self.posy+self.h))
			self.pts_rec = [(1,1), (0,1), (0,0), (1,0)]
			self.condInt = [False, False]
		elif self.orientation == "NO" :
			self.pts = ((self.posx + self.w, self.posy), (self.posx, self.posy), (self.posx, self.posy+self.h))
			self.pts_rec = [(0,0), (0,1), (1,1), (1,0)]
			self.condInt = [True, True]
		#self.pts contient les points du triangle, nécessaire à son dessin
		#self.pts_rec réfère aux points du rectangle : (0,1) signifie le point (rec.posx + 0*rec.w, rec.posy + 1*rec.h)
		#	de plus, le premier point de pts_rec correspond au point que l'on veut en-dehors de la pente du triangle pour être sûr qu'il n'y a pas contact
		#self.condInt réfère à des conditions dans le cas où on veut tester le contact par la pente : voir fonction condInt dans player.py


		
	def dessine(self, display) :	
		display.blit(self.image, (self.posx, self.posy))

def make_gros_bloc (x, y, nb_h, nb_w, type, t_blocks) :
	# coin haut gauche, nb de bloc en hauteur, nb bloc en largeur, type
	for i  in range (nb_h) :
		for j in range (nb_w) :
			x_b = x + j * len_bloc 
			y_b = y + i * len_bloc
			t_skin = "f"
			if i == 0 :
				t_skin = type
			t_blocks.append(Block(x_b, y_b, t_skin, False, ""))

def make_gros_triangle (x, y, len_cote, type, orientation, t_blocks) :
	if orientation == "SO" :
		for i in range (1, len_cote) :
			for j in range (i) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, "f", False, ""))
		for k in range (len_cote) :
			x_b = x + k * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))

	elif orientation == "NO" :
		for i in range (len_cote - 1) :
			for j in range (len_cote - i - 1) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, "f", False, ""))
		for k in range (len_cote) :
			x_b = x + (len_cote - k - 1) * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))
	
	elif orientation == "NE" :
		for i in range (len_cote - 1) :
			for j in range (i + 1, len_cote) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, "f", False, ""))
		for k in range (len_cote) :
			x_b = x + k * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))

	elif orientation == "SE" :
		for i in range (1, len_cote) : 
			for j in range (len_cote - i, len_cote) :
				x_b = x + j * len_bloc
				y_b = y + i * len_bloc
				t_blocks.append(Block(x_b, y_b, "f", False, ""))
		for k in range (len_cote) :
			x_b = x + (len_cote - k - 1)  * len_bloc
			y_b = y + k * len_bloc
			t_blocks.append(Block(x_b, y_b, type, True, orientation))

	else :
		print ("erreur creation gros bloc triangle")



def fill(display, t_blocks) :
	for b in t_blocks :
		b.dessine(display)


class Door:
	def __init__(self, posx, posy, level):
		self.posx = posx
		self.posy = posy
		self.image = dicoPorteSkins[level]["fermée"]
		self.w, self.h = dicoPorteSkins[level]["dim"]
	
	def dessine(self, display) :	
		display.blit(self.image, (self.posx, self.posy))


def fill_door(display,door_list):
	for d in door_list:
		d.dessine(display)

def door_contact(p_posx, p_posy, p_w, p_h, doors, score, level) : #fonction renvoie la valeur de state 
	for d in doors :
		if p_posx <= d.posx + d.w and p_posx + p_w >= d.posx and p_posy <= d.posy + d.h and p_posy + p_h >= d.posy: #si collision
			if score >= scoreMin[level] :
				d.image = dicoPorteSkins[level]["ouverte"]
				d.w += len_bloc
				return "arrivée sortie"
			else : 
				None #il faudrait afficher un message genre "il te manque encore *n* clefs !!"
	return "ongoing"

class Pilule() :
	def __init__(self, pos) :
		const = 500
		if pos == "gauche" :
			self.posx = largeur_fenetre//2 - const - len_bloc
			self.id = "bleue"
			self.image = pilBleue
		else :
			self.posx = largeur_fenetre//2 + const
			self.id = "rouge"
			self.image = pilRouge
		self.posy = 10

	
	def dessine(self, display) :	
		display.blit(self.image, (self.posx, self.posy))

def descendre(pills) :
	v = 1 #vitesse
	if pills[0].posy < hauteur_fenetre - 6*len_bloc :
		pills[0].posy += v
		pills[1].posy += v