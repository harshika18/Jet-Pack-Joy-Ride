from colorama import Fore, Back, init, Style
from config import *
from back import *


def Fit_in(obj,x,y,back):
	Myobj=obj.return_matr()
	backmatrix=back.return_matr()
	#print(Myobj)
	#print(backmatrix)
	#back.ground()
	for i in range(obj.x,obj.x+obj.length):
		for j in range(obj.y,obj.y+obj.width):
			if backmatrix[i][j] !=Style.BRIGHT + colors['Red'] + '*' + RESET:
				backmatrix[i][j]=' '
	for i in range(x,x+obj.length):
		for j in range(y,y+obj.width):
			#print(i,j,i-x,j-y)
			if backmatrix[i][j] != Style.BRIGHT + colors['Red'] + '*' + RESET:
				backmatrix[i][j]=Myobj[i-x][j-y]

	back.update_matrix(backmatrix)

def check_clash(obj,x,y,back):
	#check from right
	Myobj=obj.return_matr()
	backmatrix=back.return_matr()
	#print(backmatrix)
	#check for beam
	for i in range(x,x+obj.length):
		for j in range(y,y+obj.width):
			if backmatrix[i][j]==Style.BRIGHT + colors['Red'] + '*' + RESET:
				#print(backmatrix[i][j])
				obj.lives-=1
				obj.Set_pos(32,y,back)
				return 1
	#ceck for coin
	for i in range (x,x+obj.length):
		for j in range(y,y+obj.width):
			if backmatrix[i][j]==Style.BRIGHT + colors['Yellow'] + '$' + RESET:
				obj.coin_collect+=1

	
