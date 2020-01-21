from colorama import Fore, Back, init, Style

#init(autoreset=True)
#MAP CONTRAIT
SCREEN_LEN = 40
SCREEN_WIDTH = 140
MAP_SIZE = 1000
SCREEN_DELETE=70

#HERO CONTRAINT
HERO_INIT_X = 32
HERO_INIT_Y = 1
HERO_LENGTH = 4
HERO_WIDTH = 3


#w=fly, a=left, d=right, l=fire, space=shield
INPUT = ['w', 'a', 'd', 'l', ' ']

SPEED = {1: 0.25,
         2: 0.15}

SCORE_DIST = 10
SCORE_KILL = 200
SCORE_COIN = 100
 
# coin_collect=0
# lives=3

colors = {
	'Blue': '\x1b[0;34m',
	'Green': '\x1b[0;32m',
	'Cyan': '\x1b[0;36m',
	'Red': '\x1b[0;31m',
	'Purple': '\x1b[0;35m',
	'Brown': '\x1b[0;33m',
	'Gray': '\x1b[0;37m',
	'Light Green': '\x1b[1;32m',
	'Light Cyan': '\x1b[1;36m',
	'Yellow': '\x1b[1;33m',
	'White': '\x1b[1;37m'
}
RESET = '\x1b[0m'