from back import *

class person:
	def __init__(self):
		self.matrix=[]
	def return_matr(self):
		return self.matrix
	def Set_pos(self,x,y,background):
		Fit_in(self,x,y,background)
		
class Hero(person):
	def __init__(self):
		person.__init__(self)
		self.length=4
		self.width=9
		self.x=32
		self.y=2
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


scene = background()
Hero = Hero()
Hero.Set_pos(32,2,scene)
#make_back(scene)
back=scene.displayScene()
print(back)
	
