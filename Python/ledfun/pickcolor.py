#!/usr/bin/env python

import time
import unicornhat as unicorn


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

def toggle(height, width, r, g, b):
	print("Setting: " + str(r) + ", " + str(g) + ", " + str(b))
	for y in range(height):
		for x in range(width):
			unicorn.set_pixel(x,y, r, g, b)
			unicorn.show()
			time.sleep(0.05)


while True:
	r = int(input("r = (0..255): "))
	g = int(input("g = (0..255): "))
	b = int(input("b = (0..255): "))
	unicorn.off()
	toggle(height, width, r, g, b)
