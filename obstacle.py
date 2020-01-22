from back import *
import random
from globalfunc import *


class obstacle:
	def __init__(self):
		self._matrix=[]
		self.__length=0
		self.__width=0
		for i in range(21):
			self._matrix.append([])
			for j in range(21):
				#print(i)
				self._matrix[i].append(' ')
	def return_matr(self):
		return self._matrix
	def Set_pos(self,x,y,background):
		Fit_in(self,x,y,background)
	
class vertical_beam(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=10
		self.__width=6
		self.x=x
		self.y=y
		v= Style.BRIGHT + colors['Red'] + '*' + RESET
		s= Style.BRIGHT + colors['Red'] + ' ' + RESET
		#10*7 matrix
		for i in range(2):
			for j in range(6):				
				self._matrix[i][j]=v
		for i in range(2,8):
			for j in range(2,4):
				self._matrix[i][j]=v
		for i in range(8,10):
			for j in range(6):				
				self._matrix[i][j]=v
		'''self._matrix=[[' ','_' ,'_' ,'_' ,'_',' '],
					['|','_',' ',' ','_','|'],
					[' ',' ','|','|',' ',' '],
					[' ',' ','|','|',' ',' '],
					[' ',' ','|','|',' ',' '],
					[' ',' ','|','|',' ',' '],
					[' ',' ','|','|',' ',' '],
					[' ',' ','|','|',' ',' '],
					[' ','_','|','|','_',' '],
					['|','_','_','_','_','|']]


		
		              ____            ******
		             |_  _|           ******  
		               ||               **   
		               ||               **
		               ||               **
		               ||             ****** 
		               ||             ******
		               ||
		              _||_   
                     |____| 
		'''
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width

class horizontal_beam(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=4
		self.__width=19
		self.x=x
		self.y=y
		v= Style.BRIGHT + colors['Red'] + '*' + RESET
		#v= Style.BRIGHT + colors['Red'] + '|' + RESET
		#s= Style.BRIGHT + colors['Red'] + ' ' + RESET
		#4*19
		for j in range(3):			
			self._matrix[0][j]=v
		for j in range(16,19):			
			self._matrix[0][j]=v
		for i in range(1,3):
			for j in range(19):
				self._matrix[i][j]=v
		for j in range(3):			
			self._matrix[3][j]=v
		for j in range(16,19):			
			self._matrix[3][j]=v
		'''self._matrix=[[s,h,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,h,s],
					[v,s,v,h,s,h,s,h,s,h,s,h,s,h,s,h,v,s,v],
					[v,s,s,h,s,h,s,h,s,h,s,h,s,h,s,h,s,s,v],
					[v,h,v,s,s,s,s,s,s,s,s,s,s,s,s,s,v,h,v]]


   _               _
	 | |_ _ _ _ _ _ _| |           /\
	 | 	_ _ _ _ _ _ _  |          / /
	 |_|             |_|         /  \
	                             \/\ \
	                                \ \
	                                 \ \/\
	                                  \  /
	                                  / /
	                                  \/
		                                  '''
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width

class fourty_beam(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=11
		self.__width=13
		self.x=x
		self.y=y
		#9*9 matrix
		v= Style.BRIGHT + colors['Red'] + '*' + RESET
		#v= Style.BRIGHT + colors['Red'] + '/' + RESET
		#s= Style.BRIGHT + colors['Red'] + ' ' + RESET
		for j in range(4,6):			
			self._matrix[0][j]=v
		for j in range(3,7):			
			self._matrix[1][j]=v
		for j in range(2,6):			
			self._matrix[2][j]=v
		for j in range(1,6):			
			self._matrix[3][j]=v
		for j in range(0,3):			
			self._matrix[4][j]=v
		for j in range(4,7):			
			self._matrix[4][j]=v
		for j in range(1,2):			
			self._matrix[5][j]=v
		for j in range(5,8):			
			self._matrix[5][j]=v
		self._matrix[5][11]=v
		for j in range(6,9):			
			self._matrix[6][j]=v
		for j in range(10,13):			
			self._matrix[6][j]=v
		for j in range(7,12):			
			self._matrix[7][j]=v
		for j in range(6,11):			
			self._matrix[8][j]=v
		for j in range(5,9):			
			self._matrix[9][j]=v
		for j in range(6,8):			
			self._matrix[10][j]=v
		

		'''self._matrix=[[s,s,v,h,s,s,s,s,s],
					[s,v,s,v,s,s,s,s,s],
					[v,s,s,h,s,s,s,s,s],
					[h,v,h,s,h,s,s,s,s],
					[s,s,s,h,s,h,s,s,s],
					[s,s,s,s,h,s,h,v,h],
					[s,s,s,s,s,h,s,s,v],
					[s,s,s,s,s,v,s,v,s],
					[s,s,s,s,s,h,v,s,s]]	                                  



  1        
     2         **
     3        ****
     4       ****
     5      ***** 
     6     *** ***
     7      *   ***   *
     8           *** ***
     9            *****
    10           *****
    11          ****
    12           **
    13             

          ***          ***  
          ****************   
          ****************
          ***          *** 
          '''
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width

class coin(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=8
		self.__width=18
		self.x=x
		self.y=y
		v= Style.BRIGHT + colors['Yellow'] + '$' + RESET
		for i in range(random.randrange(1,7)):
			for j in range(random.randrange(4,17)):
				self._matrix[i][j]=v
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width

class up_magnet(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=3
		self.__width=8
		self.x=x
		self.y=y
		v= Style.BRIGHT + colors['Cyan'] + '=' + RESET
		h=Style.BRIGHT + colors['Cyan'] + '|' + RESET
				
		self._matrix=[[' ',' ',v,v,v,v,' ',' '],
							[h,h,' ',' ',' ',' ',h,h],
							[h,h,' ',' ',' ',' ',h,h]]

	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width


	'''  ____
	|    |       ====
	|    |     ||    ||
	           ||    ||
	'''
	
class down_magnet(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=3
		self.__width=8
		self.x=x
		self.y=y
		v= Style.BRIGHT + colors['Cyan'] + '=' + RESET
		h=Style.BRIGHT + colors['Cyan'] + '|' + RESET
				
		self._matrix=[[h,h,' ',' ',' ',' ',h,h],
							[h,h,' ',' ',' ',' ',h,h],
							[' ',' ',v,v,v,v,' ',' ']]
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width

class power_up(obstacle):
	def __init__(self,x,y):
		obstacle.__init__(self)
		self.__length=4
		self.__width=3
		self.x=x
		self.y=y
		v= Style.BRIGHT + colors['Purple'] + 'S' + RESET
		h=Style.BRIGHT + colors['Purple'] + '#' + RESET
				
		self._matrix=[[' ',v,' ',],
					[h,h,h],
					[h,h,h],
					[h,h,h]]


	'''
         S
        ###
        ###
        ###

      '''
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width
