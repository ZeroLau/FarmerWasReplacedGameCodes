def movto(x, y):
	ox = get_pos_x()
	oy = get_pos_y()
	#print(ox,oy)
	if (x - ox) >0:
		for i in range(ox, x):
			move(East)
	elif (x - ox) <0:
		for i in range(ox, x, -1):
			move(West)
	
	if (y - oy) >0:
		for i in range(oy, y):
			move(North)
	elif (y - oy) <0:
		for i in range(oy, y, -1):
			move(South)
	#print(x,y)
	
def go(x,y):
	o1 = get_pos_x()
	o2 = get_pos_y()
	
	ox = abs(o1-x)
	oy = abs(o2-y)
	#print(ox,oy)
	xo = get_world_size() - ox
	yo = get_world_size() - oy
	#print(xo,yo)
	if x-o1 > 0:
		if ox > xo:
			for i in range(xo):
				move(West)
		else:
			for i in range(ox):
				move(East)
	elif x-o1 < 0:
		if ox > xo:
			for i in range(xo):
				move(East)
		else:
			for i in range(ox):
				move(West)
			
	if y-o2 >0:	
		if oy > yo:
			for i in range(yo):
				move(South)
		else:
			for i in range(oy):
				move(North)
	elif y-o2 <0:
		if oy > yo:
			for i in range(yo):
				move(North)
		else:
			for i in range(oy):
				move(South)
	