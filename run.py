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
Dragon=dragon(22,952)
Dragon.Set_pos(22,952,scene)
getinp = Get()
back=scene.displayScene()
temp_scene=scene.displayScene()
print(back)
original_time=time.time()
shield_time=time.time()
#power_time=time.time()
first_time_shield=0
gravity_time=0
is_shoot=0
shoot_pos_x=0
shoot_pos_y=0

#0.2
while True:
	#print(is_shield)
	recent=time.time()
	#print(recent-shield_time)
	if Hero.is_shield==1 and recent-shield_time>=10:
		Hero.is_shield=0
		Hero.remove_shield()
	#Hero.magnet(scene)
	if(recent - original_time >=0.2) and scene.start<860:
		#print(recent - original_time)
		scene.start+=2
		original_time=time.time()
	if scene.start>=860:
		break
	if Hero.y<=scene.start:
		Hero.y=scene.start
		Hero.Set_pos(Hero.x,Hero.y,scene)
		#Hero.right_move(scene)
	if is_shoot==0:
		#print("check")
		Hero.remove(shoot_pos_x+2,shoot_pos_y,scene)
	else:
		is_shoot=0
	input=input_to(getinp)
	os.system('clear')
	back=scene.displayScene()
	temp_scene=scene.displayScene()
	put_info(scene,Hero,Dragon)
	print(back)
	if input is not None:
		#print(input)
		if input=='d':
			if(Hero.y>200 and Hero.y<250) or (Hero.y>500 and Hero.y<550):
				Hero.speed=1
			elif (Hero.y>150 and Hero.y<200) or (Hero.y>450 and Hero.y<500):
				Hero.speed=3
			elif Hero.is_power==0:
				Hero.speed=2
			elif Hero.is_power==1 and recent-Hero.power_time<=10:
				Hero.speed=3
			ch=check_clash(Hero,Hero.x,Hero.y+2,scene)
			if (ch==1 or ch==2) and Hero.is_shield==1:
				obstacle_detect(Hero,Hero.x,Hero.y,scene)
				Hero.is_shield=0
				Hero.remove_shield()
			Hero.right_move(scene)
		elif input=='a':
			if(Hero.y>150 and Hero.y<=200) or (Hero.y>450 and Hero.y<500):
				Hero.speed=1
			elif (Hero.y>200 and Hero.y<250) or (Hero.y>500 and Hero.y<550):
				Hero.speed=3
			elif Hero.is_power==0:
				Hero.speed=2
			elif Hero.is_power==1 and recent-Hero.power_time<=10:
				Hero.speed=3
			ch=check_clash(Hero,Hero.x,Hero.y-2,scene)
			if ch==1 or ch==2 and Hero.is_shield==1:
				obstacle_detect(Hero,Hero.x,Hero.y,scene)
				Hero.is_shield=0
				Hero.remove_shield()
			Hero.left_move(scene)
		elif input=='w':
			ch=check_clash(Hero,Hero.x-2,Hero.y,scene)
			if ch==1 or ch==2 and Hero.is_shield==1:
				obstacle_detect(Hero,Hero.x,Hero.y,scene)
				Hero.is_shield=0
				Hero.remove_shield()
			Hero.up_move(scene)
		elif input==' ':
			is_shoot=1
			shoot_pos_y=Hero.y
			shoot_pos_x=Hero.x+2
			obstacle_detect(Hero,Hero.x+2,Hero.y,scene)
			Hero.shoot(scene)
		elif input=='s' and (recent-shield_time>=50 or first_time_shield==0):
			Hero.shield()
			first_time_shield=1
			shield_time=time.time()
			Hero.is_shield=1
		if input == 'q':
			os.system('clear')
			sys.exit()
		gravity_time=0
	elif Hero.x<32:
		#print("Enter2")
		gravity_time+=0.3
		Hero.gravity(scene,gravity_time)
		ch=check_clash(Hero,Hero.x+2,Hero.y,scene)
		if ch==1 or ch==2 and Hero.is_shield==1:
			obstacle_detect(Hero,Hero.x,Hero.y,scene)
			Hero.is_shield=0
			Hero.remove_shield()
	if input is None:
		if(Hero.y>200 and Hero.y<250) or (Hero.y>500 and Hero.y<550):
			Hero.speed=2
			Hero.left_move(scene)
		if (Hero.y>150 and Hero.y<200) or (Hero.y>450 and Hero.y<500):
			Hero.speed=2
			Hero.right_move(scene)

is_shoot_dragon=1
original_time=time.time()
shoot_pos_x=0
shoot_pos_y=0

while True:
	if is_shoot_dragon==0:
		#print("check")
		Dragon.remove(shoot_pos_x+2,shoot_pos_y,scene)
		if Hero.x+4>=Dragon.x and Hero.x<=Dragon.x+11 and Hero.y<=926:
			Fit_in_shoot(Dragon,shoot_pos_x,Dragon.y-51,scene)
			Fit_in_shoot(Dragon,shoot_pos_x+2,Dragon.y-51,scene)
			check_hero(shoot_pos_x,shoot_pos_x+2,800,Hero)
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
		check_hero(Dragon.x+3,Dragon.x+10,926,Hero)
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
	temp_scene=scene.displayScene()
	put_info(scene,Hero,Dragon)
	print(back)
	if input is not None:
		if input=='d':
			if Hero.y<940:
				ch=check_clash(Hero,Hero.x,Hero.y+2,scene)
				Hero.right_move(scene)
		elif input=='a':
			if Hero.y>860:
				ch=check_clash(Hero,Hero.x,Hero.y-2,scene)
				Hero.left_move(scene)
		elif input=='w':
			if Hero.x+2<=Dragon.x:
				Dragon.up_move(scene)
			ch=check_clash(Hero,Hero.x-2,Hero.y,scene)
			Hero.up_move(scene)
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
		
	elif Hero.x<32:
		#print("Enter2")
		Hero.gravity(scene)
		ch=check_clash(Hero,Hero.x+2,Hero.y,scene)
		if Hero.x+4>=Dragon.x+14 and Dragon.x<22:
			Dragon.gravity(scene)
	if Hero.x==32 and Dragon.x<22:
		Dragon.gravity(scene)
