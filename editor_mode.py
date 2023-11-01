from block import *

#c'est peut-être brouillon mais j'ai bidouillé pour que t_blocks reste fixe si on ajoute pas de nouveaux blocks au fil des frames
def read_file_map(filename,t_blocks,list):
	f=open(filename,'r')
	lines=f.readlines()
	tmp_l=[] #contient que les nouvelles ligne du fichier
	for elm in lines:
		new=elm.split(",")
		if new not in list:
			list.append(new)
			tmp_l.append(new)
	if len(tmp_l)!=0:
		for blocks in tmp_l:
			blocks[-1]=blocks[-1][0:2] #pour enlever le '\n' génant dans le cas du triangle
			t_blocks.append(Block(int(blocks[0]),int(blocks[1]),blocks[2],int(blocks[3]),blocks[4]))
	f.close()
	


def write_file_map(filename,state):
	f=open(filename,'a')
	x_mouse,y_mouse=pygame.mouse.get_pos()
	f.write(f"{x_mouse},{y_mouse},{state},0,\n")
	f.close()

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
	print("hey")
	