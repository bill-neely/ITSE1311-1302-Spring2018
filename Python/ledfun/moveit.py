#!/usr/bin/env python

import time
import os
import unicornhat as unicorn


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

x = 0
y = 0
r = 255
b = 20
g = 147
keepGoing = True


while keepGoing:
	print('x: ' + str(x) + ' y: ' + str(y))
	unicorn.clear()
	unicorn.set_pixel(x,y, r, g, b)
	unicorn.show()
	direction = getchar()
	if direction == '8':
		if y < height - 1:
			y += 1
	if direction == '2':
		if y > 0:
			y -= 1
	if direction == '4':
		if x < width - 1:
			x += 1
	if direction == '6':
		if x > 0:
			x -= 1
	if direction == 'q':
		keepGoing = False
