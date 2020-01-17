from config import *
from make_background import *
import os
import sys
import termios
from input import *
from globalfunc import *
import threading, time

scene = background()
Hero = Hero()
Hero.Set_pos(32,2,scene)
make_back(scene)
getinp = Get()
back=scene.displayScene()
print(back)
original_time=time.time()
# ticker = threading.Event()
# while not ticker.wait(1):
# 	timer_plus(scene)
#timer_plus(scene)
is_shoot=0
shoot_pos_x=0
shoot_pos_y=0

while True:
	#timer_plus()
	recent=time.time()
	if(recent - original_time >=0.05):
		scene.start+=1
		original_time=recent
	if Hero.y<scene.start:
		Hero.right_move(scene)
	if is_shoot==0:
		#print("check")
		Hero.remove(shoot_pos_x+2,shoot_pos_y,scene)
	else:
		is_shoot=0
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
		elif input==' ':
			is_shoot=1
			shoot_pos_y=Hero.y
			shoot_pos_x=Hero.x+2
			obstacle_detect(Hero,Hero.x+2,Hero.y,scene)
			Hero.shoot(scene)
		if input == 'q':
			os.system('clear')
			sys.exit()
		# elif Hero.x!=32:
		# 	#print("Enter1")
		# 	Hero.gravity(scene)

	elif Hero.x<32:
		#print("Enter2")
		Hero.gravity(scene)
		ch=check_clash(Hero,Hero.x+2,Hero.y,scene)
