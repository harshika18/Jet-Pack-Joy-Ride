from back import *
from globalfunc import *

# class pattern:
# 	def __init__(self,x,y):
# 		matrix=[]
# 		length=26
# 		width=26
# 		x=x
# 		y=y
# 		for i in range(0,26):
# 			matrix.append([])
# 			for j in range(0,26):
# 				matrix[i].append(' ')
# 	def Set_pos(self,x,y,background):
# 		Fit_in(self,x,y,background)
# 	def return_matr(self):
# 		return matrix
def design(x,y,back):
	matrix=[]
	for i in range(0,26):
		matrix.append([])
		for j in range(0,26):
			matrix[i].append(' ')
	st=0
	i=10
	while i>=0:
		for j in range(st,st+6):
			matrix[i][j]='.'
			matrix[j][i]='.'
		i-=5
		st+=5
	i=15
	st=0
	while i<=25:
		for j in range(st,st+6):
			matrix[i][j]='.'
			matrix[j][i]='.'
		i+=5
		st+=5
	i=10
	st=20
	while i>=0:
		for j in range(st,st+6):
			matrix[i][j]='.'
			matrix[j][i]='.'
		i-=5
		st-=5
	i=20
	st=15
	while i>=15:
		for j in range(st,st+6):
			matrix[i][j]='.'
			matrix[j][i]='.'
		i-=5
		st+=5
	backmatrix=back.return_matr()
	for i in range(x,x+26):
		for j in range(y,y+26):
			#print(i,j,i-x,j-y)
			if backmatrix[i][j]==' ':
				backmatrix[i][j]=matrix[i-x][j-y]
	
	back.update_matrix(backmatrix)

	# def print_design(self):
	# 	sceneprint = ""
	# 	for i in range(0, 28):
	# 		for j in range(28):
	# 			sceneprint += matrix[i][j]+ " "
	# 		sceneprint += '\n'


# def Fit_in(mat,x,y,back):
# 	backmatrix=back.return_matr()
# 	for i in range(x,x+26):
# 		for j in range(y,y+26):
# 			#print(i,j,i-x,j-y)
# 			backmatrix[i][j]=mat[i-x][j-y]

# 	back.update_matrix(backmatrix)
