#!/usr/bin/python

#####couchpir8######
########2016########

import platform
import os
import subprocess
import socket
import curses
import curses.textpad
import time

from os import system
from subprocess import call
from curses import wrapper

#Begin Curses Screen.
myscreen = curses.initscr()

myscreen.border(0)
myscreen.addstr(1,1, "Sminer")

host = socket.gethostname()
os = platform.system()
release = platform.release()
distro = platform.linux_distribution(distname="")
#cpu = subprocess.run("uname -m", shell=True)


#Just for Spacing
#print ("\n\n")

#class style:
#	BOLD = "\033[1m"
#	END = "\033[0m"

#print ("Host: {}" .format(host))
#print ("Operating System: {}" .format(os)) 
#print ("Operating System: {}" .format(release))
#print ("Distro: {}" .format(distro))
#print ("CPU: {}" .format(cpu))



myscreen.addstr(3,2, "Host: {}" .format(host))
myscreen.addstr(4,2, "Operating System: {}" .format(release))
myscreen.addstr(5,2, "Distro: {}" .format(distro))
myscreen.refresh()
x = myscreen.getch()
#if x = "x":
#curses.endwin()




#Spacing
#print ("\n\n")

