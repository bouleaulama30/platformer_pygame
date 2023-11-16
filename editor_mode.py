from block import *
from mini_jeu import *

#c'est peut-être brouillon mais j'ai bidouillé pour que t_blocks reste fixe si on ajoute pas de nouveaux blocks au fil des frames
def read_file_map(filename,t_blocks,list):
	f=open(filename,'r')
	lines=f.readlines()
	tmp_l=[] #contient que les nouvelles ligne du fichier
	for elm in lines:
		new=elm.split(",")
		if new[0:3] not in list:
			list.append(new[0:3])
			tmp_l.append(new)
	if len(tmp_l)!=0:
		for blocks in tmp_l:
			blocks[-1]=blocks[-1][0:2] #pour enlever le '\n' génant dans le cas du triangle
			t_blocks.append(Block(int(blocks[0]),int(blocks[1]),blocks[2],int(blocks[3]),blocks[4]))
	f.close()


def write_file_map(filename,state,triangle=False,orientation=""):
	f=open(filename,'a')
	if triangle:
		x_mouse,y_mouse=pygame.mouse.get_pos()
		f.write(f"{x_mouse},{y_mouse},{state},1,{orientation}\n")

	else:
		x_mouse,y_mouse=pygame.mouse.get_pos()
		f.write(f"{x_mouse},{y_mouse},{state},0,\n")
		f.close()


# on supprime bien la ligne du fichier mais il faut arriver à supprimer le block correspondant dans t_blocks
# le problème c'est que l'objet Block n'a pas de méthode pour comparer deux blocks entre eux
# donc je ne sais pas comment faire pour supprimer le block correspondant dans t_blocks
def delete_line_file_map(filename,t_blocks,list):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	f=open(filename,'r')
	lines=f.readlines()
	f=open(filename,'w')
	for line in lines:
		i= index_second_coma(line)
		if (f'{x_mouse},{y_mouse}')!=line[:i]:
			f.write(line)
			
		else:
			blocks=line.split(",") 
			if blocks[0:3] in list:
				list.remove(blocks[0:3])
			blocks[-1]=blocks[-1][0:2] 
			B1=Block(int(blocks[0]),int(blocks[1]),blocks[2],int(blocks[3]),blocks[4]) 
			for block in t_blocks:
				if compare_blocks(B1,block):
					t_blocks.remove(block)
	f.close()

def compare_blocks(block1,block2):
	if block1.posx==block2.posx and block1.posy==block2.posy:
		return True
	return False

def read_file_keys(filename,key_list,list):
	f=open(filename,'r')
	lines=f.readlines()
	tmp_l=[] #contient que les nouvelles ligne du fichier
	for elm in lines:
		new=elm.split(",")
		if new not in list:
			list.append(new)
			tmp_l.append(new)
	if len(tmp_l)!=0:
		for key in tmp_l:
			key_list.append(Key(int(key[0]),int(key[1])))
	f.close()


def write_file_keys(filename):
	f=open(filename,'a')
	x_mouse,y_mouse=pygame.mouse.get_pos()
	f.write(f"{x_mouse},{y_mouse},\n")
	f.close()


def read_file_door(filename, door_list, listReadDoor, level):
	f=open(filename,'r')
	lines=f.readlines()
	tmp_l=[] #ne contient que les nouvelles lignes du fichier
	for elm in lines:
		new=elm.split(",")
		if new not in listReadDoor:
			listReadDoor.append(new)
			tmp_l.append(new)
	if len(tmp_l)!=0:
		for door in tmp_l:
			door_list.append(Door(int(door[0]),int(door[1]), level))
	f.close()


def write_file_door(filename) :
    f=open(filename,'a')
    x_mouse,y_mouse=pygame.mouse.get_pos()
    f.write(f"{x_mouse},{y_mouse},\n")
    f.close()


def delete_line_file_keys(filename,key_list,list):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	f=open(filename,'r')
	lines=f.readlines()
	f=open(filename,'w')
	for line in lines:
		i= index_second_coma(line)
		if (f'{x_mouse},{y_mouse}')!=line[:i]:
			f.write(line)
			
		else:
			keys=line.split(",") 
			if keys in list:
				list.remove(keys) #on l'enlève aussi de la liste global car sinon on ne peut pas ajouter une nouvelle clé au même endroit
			k1=Key(int(keys[0]),int(keys[1]))
			for key in key_list:
				if compare_keys(k1,key):
					key_list.remove(key)
	f.close()
def delete_line_file_door(filename,key_list,list, level):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	f=open(filename,'r')
	lines=f.readlines()
	f=open(filename,'w')
	for line in lines:
		i= index_second_coma(line)
		if (f'{x_mouse},{y_mouse}')!=line[:i]:
			f.write(line)
			
		else:
			keys=line.split(",") 
			if keys in list:
				list.remove(keys) #on l'enlève aussi de la liste global car sinon on ne peut pas ajouter une nouvelle clé au même endroit
			k1=Door(int(keys[0]),int(keys[1]), level)
			for key in key_list:
				if compare_keys(k1,key):
					key_list.remove(key)
	f.close()

def compare_keys(key1,key2):
	if key1.posx==key2.posx and key1.posy==key2.posy:
		return True
	return False

def index_second_coma(string):
    i=0
    count=0
    for elm in string:
        if elm==",":
            count+=1
        if count==2:
            return i
        i+=1
    return -1




def move_right_mouse(nbr_pixels):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	pygame.mouse.set_pos(x_mouse+nbr_pixels,y_mouse)

def move_left_mouse(nbr_pixels):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	pygame.mouse.set_pos(x_mouse-nbr_pixels,y_mouse)

def move_up_mouse(nbr_pixels):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	pygame.mouse.set_pos(x_mouse,y_mouse-nbr_pixels)

def move_down_mouse(nbr_pixels):
	x_mouse,y_mouse= pygame.mouse.get_pos()
	pygame.mouse.set_pos(x_mouse,y_mouse+nbr_pixels)

def reset_mouse():
	pygame.mouse.set_pos(0,0)
	
	