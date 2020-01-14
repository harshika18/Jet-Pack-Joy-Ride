from config import *
import numpy as np
from mypattern import *
from globalfunc import *


class background:
	def __init__(self):
		
		self.score = 0
		self.dis_cover = 0
		self.start = 0
		self.length = SCREEN_LEN
		self.width = SCREEN_WIDTH
		self.map_size= MAP_SIZE
		#print("enter")
		self.screen=[]
		for x in range(0, self.map_size):
			self.screen.append([])
			for y in range(0, self.map_size):
				self.screen[x].append(' ')
	#def ground(self):
		for x in range(36, self.length):
			for y in range(0, self.map_size):
				self.screen[x][y] = colors['Brown'] + 'I' + RESET 

	def return_matr(self):
		return self.screen
	def update_matrix(self, up_mat):
		self.screen = up_mat
	def displayScene(self):
		poss=2
		while poss<MAP_SIZE-50:
	#for tt in range(10):
			# v_pat=pattern(2,poss)
			# v_pat.design()
			# v_pat.Set_pos(2,poss,scene)
			design(2,poss,self)
			poss+=60		
		sceneprint = ""
		original=self.start + self.width
		#if(self.screen[0][0]==' '):
		#	self.screen[0][0]='\x1b[0;45m'
		if self.start >= self.map_size - self.width:
			self.start = self.map_size - self.width
		for i in range(0, self.length):
			for j in range(self.start, self.start + self.width):
				sceneprint += str(self.screen[i][j])
			sceneprint += '\n'
				#sceneprint += colors['Cyan'] + "Press Q to exit\n" 
		return sceneprint

