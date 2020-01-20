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

def Fit_in_shoot(obj,x,y,back):
	Myobj=obj.gun
	k=45
	backmatrix=back.return_matr()
	if Myobj=='O':
		k=25
	for i in range(y,y+k,5):
	#for i in range(y,y+len(Myobj)):
		if backmatrix[x][i]==' ':
			backmatrix[x][i]=Myobj
	back.update_matrix(backmatrix)

def remove_gun(obj,x,y,back):
	backmatrix=back.return_matr()
	for j in range(0,36):
		for i in range(y,MAP_SIZE-1):
		#print(backmatrix[x][i])
			if backmatrix[j][i]=='>':
				backmatrix[j][i]=' '
	back.update_matrix(backmatrix)

def remove_boss_gun(obj,x,y,back):
	backmatrix=back.return_matr()
	for j in range(0,36):
		for i in range(350,455):
			#print(backmatrix[x][i])
			if backmatrix[j][i]=='O':
				backmatrix[j][i]=' '
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

	#check enemy
	for i in range (x,x+obj.length):
		for j in range(y,y+obj.width):
			if backmatrix[i][j]=='^':
				obj.lives-=1
				for c in range(34,36):
					for d in range(j,j+5):
						backmatrix[c][d]=' '

	#check power
	for i in range (x,x+obj.length):
		for j in range(y,y+obj.width):
			v= Style.BRIGHT + colors['Purple'] + 'S' + RESET
			h=Style.BRIGHT + colors['Purple'] + '#' + RESET
			if backmatrix[i][j]==h or backmatrix[i][j]==v:
				obj.speed+=1
				break

	#check magnet

	
def obstacle_detect(obj,x,y,back):
	backmatrix=back.return_matr()
	for i in range(y,back.start+SCREEN_WIDTH):
		v=Style.BRIGHT + colors['Red'] + '*' + RESET
		#print(backmatrix[x][i])
		if(backmatrix[x][i]==v):
			obj.obs_killed+=1
			for c in range(3,32):
				for j in range(i-10,i+20):
					if(backmatrix[c][j]==v):
						backmatrix[c][j]=' '
			break
		elif(backmatrix[x][i]=='^'):
			obj.enemy_killed+=1
			for c in range(34,36):
				for j in range(i,i+5):
					backmatrix[c][j]=' '
			break

def check_hero(x,x1,y,obj):
	if obj.x+4>=x and obj.x<=x1 and obj.y>=y:
		obj.lives-=1

def dragon_check(obj,x):
	if x>=obj.x and x<=obj.x+14:
		obj.lives-=1