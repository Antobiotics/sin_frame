import sys
import pygame
import math
import time
import subprocess

pygame.init()

#Create the screen
height = 630
width = 480
size = (height,width)
window = pygame.display.set_mode(size)

#PARAMETERS
amp = 30
phase = 6.3

def linear_map(x,(x1,x2),(y1,y2)):
	return((y2-y1)/(x2-x1)*(x-x1)+y1)

def drawHor(sp):
	for i in range(0,width):
	#	b=amp*math.sin(2*(1/phase)*i+sp)
		u = math.sin((1/phase)*i+sp)
		b_p=linear_map(u,(-1,1),(0,255))
		grey=(b_p,b_p,b_p)	
		pygame.draw.line(window,grey,(0,i),(height,i))

pi_2= math.pi
sp = pi_2/4

#CLEAN USB LSOF

#SHOOTING
n_sh = 3
for i in range(0,n_sh):
	drawHor(sp)
	pygame.display.flip()
	cad = "--capture-image-and-download"
	folder = "--folder=."
	name = "--filename"
	p = "%Y%m%d%H%M%S.jpg"
#	subprocess.call(["gphoto2","--auto-detect"])
	subprocess.call(["gphoto2",cad,name,p])
	sp= sp+ pi_2/4

print("SHOOTING IS OVER")
sys.exit(0)

#LISTENING
while True:
	#drawHor(sp)

	#pygame.display.flip()
	#sp = sp + pi_2/4
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
	#	else:
	#		print event


