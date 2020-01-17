'''import colorama
from colorama import Back as bg

colorama.init()
print(bg.LIGHT GREEN)
print(colorama.ansi.clear_screen())'''

#print '\033[1m \033[91m \033[4m' +  "SELECTED OPTION IS FOR INSERTING\n" + '\033[0m'
#print "Please enter valid input\n" 

# Python program to print 
# red text with green background 

from colorama import Fore, Back, Style 
print(Fore.RED + 'some red text') 
for x in range(1,10):
	print(Back.GREEN ) 
print(Style.RESET_ALL) 
