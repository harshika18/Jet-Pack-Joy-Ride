import colorama
import numpy as np

'''def color_sign(x):
    c = colorama.Fore.GREEN if x > 0 else colorama.Fore.RED
    return f'{c}{x}'''
color_ascii= '\x1b[0;34m' + '#' + '\x1b[0m'

np.set_printoptions(formatter={'float': color_ascii})