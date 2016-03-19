#!/usr/bin/python

#####couchpir8######
########2016########

import platform
import os

os = platform.system()
release = platform.release()
distro = platform.linux_distribution(distname="")
#cpu = os.popen("uname -r")

#Just for Spacing
print ("\n\n")

#print ("Operating System: {}" .format(os)) 
print ("Operating System: {}" .format(release))
print ("Distro: {}" .format(distro))
#print ("CPU: {}" .format(cpu))

#Spacing
print ("\n\n")
