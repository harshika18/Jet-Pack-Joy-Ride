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
		self.Set_pos(self.x,self.y+2,scene)
	def left_move(self,scene):
		self.Set_pos(self.x,self.y-2,scene)
	def up_move(self,scene):
		self.Set_pos(self.x-2,self.y,scene)
	def gravity(self,scene):
		self.Set_pos(self.x+1,self.y,scene)
		
class Hero(person):
	def __init__(self):
		person.__init__(self)
		self.length=4
		self.width=9
		self.x=32
		self.y=2
		self.lives=3
		self.coin_collect=0
		#9*4 matrix
		#print("enter")
		self.matrix=[[' ',' ',' ',' ','(',')',' ',' ',' '],
					[ ' ', '/','/','|',' ',' ', '|','_','_'],
					['/','/',' ', '|','_','_','|',' ',' '],
					[' ',' ',' ','/',' ',' ','\\',' ',' ']]
		#self.Set_pos(32,2)

	'''   ()   
	   //|  |__     hero
	  // |__|
	     /  \
	'''


