import sys
import termios
import tty
import signal
from globalfunc import *


class Get:
    """Class to get input from user in real time"""

    def __call__(self):
        """ Defining the call for class objects """

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def input_to(getch):
    """Taking input from user."""
    text = getch()
    return text