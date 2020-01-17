from back import *
from globalfunc import *

class pattern:
	def __init__(self,x,y):
		self.matrix=[]
		self.length=26
		self.width=26
		self.x=x
		self.y=y
		for i in range(0,26):
			self.matrix.append([])
			for j in range(0,26):
				self.matrix[i].append(' ')
	def Set_pos(self,x,y,background):
		Fit_in(self,x,y,background)
	def return_matr(self):
		return self.matrix
	def design(self):
		st=0
		i=10
		while i>=0:
			for j in range(st,st+6):
				self.matrix[i][j]='.'
				self.matrix[j][i]='.'
			i-=5
			st+=5
		i=15
		st=0
		while i<=25:
			for j in range(st,st+6):
				self.matrix[i][j]='.'
				self.matrix[j][i]='.'
			i+=5
			st+=5
		i=10
		st=20
		while i>=0:
			for j in range(st,st+6):
				self.matrix[i][j]='.'
				self.matrix[j][i]='.'
			i-=5
			st-=5
		i=20
		st=15
		while i>=15:
			for j in range(st,st+6):
				self.matrix[i][j]='.'
				self.matrix[j][i]='.'
			i-=5
			st+=5

	def print_design(self):
		sceneprint = ""
		for i in range(0, 28):
			for j in range(28):
				sceneprint += matrix[i][j]+ " "
			sceneprint += '\n'

#print(sceneprint)