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
			self.Set_pos(self.x,self.y+2,scene)
	def left_move(self,scene):
		if self.y-2>scene.start:
			self.Set_pos(self.x,self.y-2,scene)
	def up_move(self,scene):
		if self.x-2>2:
			self.Set_pos(self.x-2,self.y,scene)
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
		#9*4 matrix
		#print("enter")
		self.matrix=[[' ',' ',' ',' ','(',')',' ',' ',' '],
					[ ' ', '/','/','|',' ',' ', '|','_','_'],
					['/','/',' ', '|','_','_','|',' ',' '],
					[' ',' ',' ','/',' ',' ','\\',' ',' ']]

	def shoot(self,scene):
		self.gun='>>>>>'
		self.Set_pos_gun(self.x+2,self.y+40,scene)
		#self.Set_pos_gun(self.x,self.y+40,scene)
		#self.Set_pos_gun(self.x,self.y+80,scene)
	def Set_pos_gun(self,x,y,background):
		Fit_in_shoot(self,x,y,background)
	def remove(self,x,y,background):
		remove_gun(self,x,y,background)
		#self.Set_pos(32,2)

	'''   ()   
	   //|  |__     hero
	  // |__|
	     /  \
	'''


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