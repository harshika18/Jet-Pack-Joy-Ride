from back import *
from globalfunc import *


class person:
	def __init__(self):
		self._matrix=[]
		self.__lives=3
	def return_matr(self):
		return self._matrix
	def Set_pos(self,x,y,background):
		Fit_in(self,x,y,background)
		self.x=x
		self.y=y
	def right_move(self,scene):
		#print(self.speed)
		if self.y+8<scene.start+SCREEN_WIDTH:
			self.Set_pos(self.x,self.y+self.speed,scene)
	def left_move(self,scene):
		#print(self.speed)
		if self.y-self.speed>scene.start:
			self.Set_pos(self.x,self.y-self.speed,scene)
	def up_move(self,scene):
		if self.x-self.speed>2:
			self.Set_pos(self.x-self.speed,self.y,scene)
	def gravity(self,scene,t):
		g=1
		jump=round(g*t*t)
		'''if(self.x<8):
			jump=1
		elif(self.x<17):
			jump=2
		elif(self.x+3<=32):
			jump=3
		elif(self.x+2<=32):
			jump=2
		else:
			jump=1'''
		if self.x+jump>32:
			jump=32-self.x
		self.Set_pos(self.x+jump,self.y,scene)
	def boss_shoot(self,x,y,scene):
		self.gun='>'
		self.Set_pos_gun(x,y,scene)
	def Set_pos_gun(self,x,y,background):
		Fit_in_shoot(self,x,y,background)
	def get_lives(self):
		return self.__lives
	def set_lives(self,x):
		self.__lives=x
		
class hero_mando(person):
	def __init__(self):
		person.__init__(self)
		self.__length=4
		self.__width=9
		self.x=32
		self.y=2
		self.__lives=3
		self.__coin_collect=0
		self.__enemy_killed=0
		self.__obs_killed=0
		self.speed=2
		self.__is_shield=0
		self.__is_power=0
		#self.power_time=0
		#9*4 matrix
		#print("enter")
		if self.__is_shield==0:
			self._matrix=[[' ',' ',' ',' ','(',')',' ',' ',' '],
							[ ' ', '/','/','|',' ',' ', '|','_','_'],
							['/','/',' ', '|','_','_','|',' ',' '],
							[' ',' ',' ','/',' ',' ','\\',' ',' ']]
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width
	def get_is_shield(self):
		return self.__is_shield
	def set_is_shield(self,x):
		self.__is_shield=x
	def get_is_power(self):
		return self.__is_power
	def set_is_power(self,x):
		self.__is_power=x
	
	def get_obs_killed(self):
		return self.__obs_killed
	def set_obs_killed(self,x):
		self.__obs_killed=x
	def get_enemy_killed(self):
		return self.__enemy_killed
	def set_enemy_killed(self,x):
		self.__enemy_killed=x
	def get_coin(self):
		return self.__coin_collect
	def set_coin(self,x):
		self.__coin_collect=x

	def shoot(self,scene):
		#self.fire_len=49
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
		self._matrix=[[' ',' ',' ',' ',q,w,' ',' ',' '],
					[ ' ', r,r,e,' ',' ', e,y,y],
					[r,r,' ', e,y,y,e,' ',' '],
					[' ',' ',' ',r,' ',' ',t,' ',' ']]

	def remove_shield(self):
		self._matrix=[[' ',' ',' ',' ','(',')',' ',' ',' '],
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
		self.__length=2
		self.__width=2
		self.x=x
		self.y=y
		self._matrix=[['^','^'],
					['/','\\']]

		'''
		 ^^
		 /\
		 '''
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width
class dragon(person):
	def __init__(self,x,y):
		person.__init__(self)
		self.__length=14
		self.__width=46
		self.x=x
		self.y=y
		self.speed=2
		self.__lives=5
		self.gun='O'
		self._matrix=[[] for i in range(0,50)]
		self._matrix[0]  = ("              ______________                  ")
		self._matrix[1]  = ("        ,===:'.,            `-._              ")
		self._matrix[2]  = ("             `:.`---.__         `-._          ")
		self._matrix[3]  = ("               `:.     `--.         `.        ")        
		self._matrix[4]  = ("                 \.        `.         `.      ")
		self._matrix[5]  = ("         (,,(,    \.         `.   ____,-`.,   ")
		self._matrix[6]  = ("      (,'     `/   \.   ,--.___`.'            ")
		self._matrix[7]  = ("  ,  ,'  ,--.  `,   \.;'         `            ")
		self._matrix[8]  = ("   `{D, {    \  :    \;                       ") 
		self._matrix[9]  = ("     V,,'    /  /    //                       ")
		self._matrix[10] = ("     j;;    /  ,' ,-//.    ,---.              ") 
		self._matrix[11] = ("     \;'   /  ,' /  _  \  /  _  \   ,'/       ")
		self._matrix[12] = ("           \   `'  / \  `'  / \  `.' /        ")
		self._matrix[13] = ("            `.___,'   `.__,'   `.__,'         ")
	
	def boss_shoot(self,scene,hero_pos):
		self.gun='O'
		self.Set_pos_gun(hero_pos,self.y-26,scene)
		self.Set_pos_gun(hero_pos+2,self.y-26,scene)
		#self.Set_pos_gun(self.x+10,self.y-26,scene)
	def remove(self,x,y,background):
		remove_boss_gun(self,x,y,background)

	def gravity(self,scene):
		self.Set_pos(self.x+2,self.y,scene)
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width
