from config import *
from make_background import *
import os
import sys
import termios
from input import *
from globalfunc import *


scene = background()
Hero = Hero()
Hero.Set_pos(32,2,scene)
make_back(scene)
getinp = Get()
back=scene.displayScene()
print(back)

while True:
	input=input_to(getinp)
	os.system('clear')
	#make_back(scene)
	back=scene.displayScene()
	print(back)
	if input is not None:
		#print(input)
		if input=='d':
			ch=check_clash(Hero,Hero.x,Hero.y+2,scene)
			Hero.right_move(scene)
			print("lives:%d coin:%d" %(Hero.lives,Hero.coin_collect))
		elif input=='a':
			ch=check_clash(Hero,Hero.x,Hero.y-2,scene)
			Hero.left_move(scene)
			print("lives:%d coin:%d" %(Hero.lives,Hero.coin_collect))
		elif input=='w':
			ch=check_clash(Hero,Hero.x-2,Hero.y,scene)
			Hero.up_move(scene)
			print("lives:%d coin:%d" %(Hero.lives,Hero.coin_collect))
		elif input == 'q':
			os.system('clear')
			sys.exit()
		elif Hero.x!=32:
			print("Enter1")
			Hero.gravity(scene)

	elif Hero.x!=32:
		print("Enter2")
		Hero.gravity(scene)
