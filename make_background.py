from obstacle import *
from person import *
from mypattern import *
scene = background()
def make_back(scene):
	y=0
	x=0
	#v_pat=pattern(2,2)
	#v_pat.Set_pos(2,2,scene)
	while y<MAP_SIZE-50:
	#for tt in range(10):
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

Hero = Hero()
Hero.Set_pos(32,2,scene)
make_back(scene)
back=scene.displayScene()
print(back)
	

	