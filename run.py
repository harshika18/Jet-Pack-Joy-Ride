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
Dragon=dragon(22,452)
Dragon.Set_pos(22,452,scene)
getinp = Get()
back=scene.displayScene()
Lives=[[] for i in range(0,10)]
# Lives[0]=("LIVES:")
# for i in range(5,5+len(Lives)):
# 	back[0][i]=Lives[0][i-5]
print("lives:%d coin:%d dragon lives:%d" %(Hero.lives,Hero.coin_collect,Dragon.lives))
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
	print("lives:%d coin:%d dragon lives:%d" %(Hero.lives,Hero.coin_collect,Dragon.lives))

	#timer_plus()
	recent=time.time()
	if(recent - original_time >=0.2) and scene.start<360:
		#print(recent - original_time)
		scene.start+=1
		original_time=time.time()
	if scene.start>=360:
		break
	if Hero.y<scene.start:
		Hero.right_move(scene)
	if is_shoot==0:
		#print("check")
		Hero.remove(shoot_pos_x+2,shoot_pos_y,scene)
	else:
		is_shoot=0
	input=input_to(getinp)
	os.system('clear')
	back=scene.displayScene()
	# #Lives=list("LIVES:")
	# for i in range(5,5+len(Lives)):
	# 	back[0][i]=Lives[i-5]
	#make_back(scene)
	# for i in range(scene.start+5,scene.start+5+len(Lives)):
	# 	back[0][i]=Lives[i-5]
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
			#Hero.boss_shoot(Hero.x+2,Hero.y+15, scene)
			#Dragon.boss_shoot(scene)


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

is_shoot_dragon=1
original_time=time.time()
shoot_pos_x=0
shoot_pos_y=0

while True:
	if is_shoot_dragon==0:
		#print("check")
		Dragon.remove(shoot_pos_x+2,shoot_pos_y,scene)
		if Hero.x+4>=Dragon.x and Hero.x<=Dragon.x+11 and Hero.y<=426:
			Fit_in_shoot(Dragon,shoot_pos_x,Dragon.y-51,scene)
			Fit_in_shoot(Dragon,shoot_pos_x+2,Dragon.y-51,scene)
			#Fit_in_shoot(Dragon,Dragon.x+9,Dragon.y-51,scene)
			#check_hero(Dragon.x+3,Dragon.x+10,300,Hero)
			check_hero(shoot_pos_x,shoot_pos_x+2,300,Hero)
			is_shoot_dragon=2
	elif is_shoot_dragon==2:
		Dragon.remove(shoot_pos_x+2,shoot_pos_y,scene)

	else:
		is_shoot_dragon=0
	
	

	recent=time.time()
	if recent - original_time >=4:
		#print(recent - original_time)
		Dragon.boss_shoot(scene,Hero.x)
		shoot_pos_x=Hero.x
		check_hero(Dragon.x+3,Dragon.x+10,426,Hero)
		original_time=time.time()
		is_shoot_dragon=1

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
		if input=='d':
			if Hero.y<440:
				ch=check_clash(Hero,Hero.x,Hero.y+2,scene)
				Hero.right_move(scene)
				print("lives:%d coin:%d dragon lives:%d" %(Hero.lives,Hero.coin_collect,Dragon.lives))
		elif input=='a':
			if Hero.y>360:
				ch=check_clash(Hero,Hero.x,Hero.y-2,scene)
				Hero.left_move(scene)
				print("lives:%d coin:%d dragon lives:%d" %(Hero.lives,Hero.coin_collect,Dragon.lives))
		elif input=='w':
			if Hero.x+2<=Dragon.x:
				Dragon.up_move(scene)
			ch=check_clash(Hero,Hero.x-2,Hero.y,scene)
			Hero.up_move(scene)
			print("lives:%d coin:%d dragon lives:%d" %(Hero.lives,Hero.coin_collect,Dragon.lives))
		elif input==' ':
			is_shoot=1
			shoot_pos_y=Hero.y
			shoot_pos_x=Hero.x+2
			#obstacle_detect(Hero,Hero.x+2,Hero.y,scene)
			Hero.boss_shoot(Hero.x+2,Hero.y+10, scene)
			dragon_check(Dragon,Hero.x+2)
			
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
		if Hero.x+4>=Dragon.x+14 and Dragon.x<22:
			Dragon.gravity(scene)
	if Hero.x==32 and Dragon.x<22:
		Dragon.gravity(scene)
