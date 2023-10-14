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

		if self.type in ["n", "j", "s", "f"] :
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
		## todo : créer les blocs en coin pour le skin fill
		
	def dessine(self, display) :	
		display.blit(self.image, (self.posx, self.posy))
		# if self.isTriangle :
		# 	x = self.posx
		# 	y = self.posy
		# 	cote = self.w 
		# 	no = (x, y)
		# 	ne = (x+cote, y)
		# 	se = (x+cote, y+cote)
		# 	so = (x, y+cote)

		# 	display.blit(self.image, no)
		# else :
		# 	display.blit(self.image, (self.posx, self.posy))
			#pygame.draw.rect(display, (255,0,0), ((self.posx, self.posy), (self.w, self.h)))

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

