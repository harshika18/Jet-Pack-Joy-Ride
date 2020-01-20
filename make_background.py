from obstacle import *
from person import *
from mypattern import *
from globalfunc import *

def make_back(scene):
	y=0
	x=0
	poss=2
	j=20
	while j<MAP_SIZE-50:	
		Enemy=enemy(34,j)
		Enemy.Set_pos(34,j,scene)
		j+=70
	j=23
	while j<MAP_SIZE-50:
		Enemy=enemy(34,j)
		Enemy.Set_pos(34,j,scene)
		j+=70
		#Enemy.Set_pos(34,j,scene)
		#j+=30
	while y<MAP_SIZE-50 and poss<MAP_SIZE-50:
	#for tt in range(10):
		# v_pat=pattern(2,poss)
		# v_pat.design()
		# v_pat.Set_pos(2,poss,scene)
		
		poss+=60		
		type=random.choice([0,1,2,3])
		x=random.randrange(4,19)
		y+=random.randrange(10,30)
		if type==0:
			v_beam=vertical_beam(x,y)
			v_beam.Set_pos(x,y,scene)
			y+=20
		elif type==1:
			h_beam=horizontal_beam(x,y)
			h_beam.Set_pos(x,y,scene)
			y+=20
		elif type==2:
			f_beam=fourty_beam(x,y)
			f_beam.Set_pos(x,y,scene)
			y+=20
		elif type==3:
			Coin=coin(x,y)
			Coin.Set_pos(x,y,scene)
			y+=20
	y=random.randrange(50,100)
	magnet=up_magnet(3,y)
	magnet.Set_pos(3,y,scene)
	y=random.randrange(300,400)
	magnet=up_magnet(3,y)
	magnet.Set_pos(3,y,scene)

	y=random.randrange(170,220)
	magnet=down_magnet(33,y)
	magnet.Set_pos(33,y,scene)

	y=random.randrange(110,160)
	power=power_up(3,y)
	power.Set_pos(3,y,scene)

	y=random.randrange(230,280)
	power=power_up(32,y)
	power.Set_pos(32,y,scene)

