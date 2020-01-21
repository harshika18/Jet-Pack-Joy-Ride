from back import *
from globalfunc import *


class person:
	def __init__(self):
		self.matrix=[]
	def return_matr(self):
		return self.matrix
	def Set_pos(self,x,y,background):
		Fit_in(self,x,y,background)
		self.x=x
		self.y=y
	def right_move(self,scene):
		if self.y+8<scene.start+SCREEN_WIDTH:
			self.Set_pos(self.x,self.y+self.speed,scene)
	def left_move(self,scene):
		if self.y-self.speed>scene.start:
			self.Set_pos(self.x,self.y-self.speed,scene)
	def up_move(self,scene):
		if self.x-self.speed>2:
			self.Set_pos(self.x-self.speed,self.y,scene)
	def gravity(self,scene):
		if(self.x<8):
			jump=1
		elif(self.x<17):
			jump=2
		elif(self.x+3<=32):
			jump=3
		elif(self.x+2<=32):
			jump=2
		else:
			jump=1
		self.Set_pos(self.x+jump,self.y,scene)
	def boss_shoot(self,x,y,scene):
		self.gun='>'
		self.Set_pos_gun(x,y,scene)
	def Set_pos_gun(self,x,y,background):
		Fit_in_shoot(self,x,y,background)
		
class Hero(person):
	def __init__(self):
		person.__init__(self)
		self.length=4
		self.width=9
		self.x=32
		self.y=2
		self.lives=3
		self.coin_collect=0
		self.enemy_killed=0
		self.obs_killed=0
		self.speed=2
		self.is_shield=0
		self.is_power=0
		#9*4 matrix
		#print("enter")
		if self.is_shield==0:
			self.matrix=[[' ',' ',' ',' ','(',')',' ',' ',' '],
							[ ' ', '/','/','|',' ',' ', '|','_','_'],
							['/','/',' ', '|','_','_','|',' ',' '],
							[' ',' ',' ','/',' ',' ','\\',' ',' ']]

	def shoot(self,scene):
		self.fire_len=49
		self.gun='>'
		self.Set_pos_gun(self.x+2,self.y+40,scene)
		#self.Set_pos_gun(self.x,self.y+40,scene)
		#self.Set_pos_gun(self.x,self.y+80,scene)
	
	def remove(self,x,y,background):
		remove_gun(self,x,y,background)
		#self.Set_pos(32,2)

	'''   ()   
	   //|  |__     hero
	  // |__|
	     /  \
	'''
	def shield(self):
		q= Style.BRIGHT + colors['Green'] + '(' + RESET
		w= Style.BRIGHT + colors['Green'] + ')' + RESET
		e= Style.BRIGHT + colors['Green'] + '|' + RESET
		r= Style.BRIGHT + colors['Green'] + '/' + RESET
		t= Style.BRIGHT + colors['Green'] + '\\' + RESET
		y= Style.BRIGHT + colors['Green'] + '_' + RESET
		self.matrix=[[' ',' ',' ',' ',q,w,' ',' ',' '],
					[ ' ', r,r,e,' ',' ', e,y,y],
					[r,r,' ', e,y,y,e,' ',' '],
					[' ',' ',' ',r,' ',' ',t,' ',' ']]

	def remove_shield(self):
		self.matrix=[[' ',' ',' ',' ','(',')',' ',' ',' '],
					[ ' ', '/','/','|',' ',' ', '|','_','_'],
					['/','/',' ', '|','_','_','|',' ',' '],
					[' ',' ',' ','/',' ',' ','\\',' ',' ']]
	def magnet(self,scene):
		if(self.y>70 and self.y<130 and self.x<15):
			if self.y<100:
				self.right_move(scene)
			else:
				self.left_move(scene)


class enemy(person):
	def __init__(self,x,y):
		person.__init__(self)
		self.length=2
		self.width=2
		self.x=x
		self.y=y
		self.matrix=[['^','^'],
					['/','\\']]

		'''
		 ^^
		 /\
		 '''

class dragon(person):
	def __init__(self,x,y):
		person.__init__(self)
		self.length=14
		self.width=46
		self.x=x
		self.y=y
		self.speed=2
		self.lives=3
		self.gun='O'
		self.matrix=[[] for i in range(0,50)]
		self.matrix[0]  = ("              ______________                  ")
		self.matrix[1]  = ("        ,===:'.,            `-._              ")
		self.matrix[2]  = ("             `:.`---.__         `-._          ")
		self.matrix[3]  = ("               `:.     `--.         `.        ")        
		self.matrix[4]  = ("                 \.        `.         `.      ")
		self.matrix[5]  = ("         (,,(,    \.         `.   ____,-`.,   ")
		self.matrix[6]  = ("      (,'     `/   \.   ,--.___`.'            ")
		self.matrix[7]  = ("  ,  ,'  ,--.  `,   \.;'         `            ")
		self.matrix[8]  = ("   `{D, {    \  :    \;                       ") 
		self.matrix[9]  = ("     V,,'    /  /    //                       ")
		self.matrix[10] = ("     j;;    /  ,' ,-//.    ,---.              ") 
		self.matrix[11] = ("     \;'   /  ,' /  _  \  /  _  \   ,'/       ")
		self.matrix[12] = ("           \   `'  / \  `'  / \  `.' /        ")
		self.matrix[13] = ("            `.___,'   `.__,'   `.__,'         ")
	
	def boss_shoot(self,scene,hero_pos):
		self.gun='O'
		self.Set_pos_gun(hero_pos,self.y-26,scene)
		self.Set_pos_gun(hero_pos+2,self.y-26,scene)
		#self.Set_pos_gun(self.x+10,self.y-26,scene)
	def remove(self,x,y,background):
		remove_boss_gun(self,x,y,background)

	def gravity(self,scene):
		self.Set_pos(self.x+2,self.y,scene)

