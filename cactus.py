def cactussort(list):
	data=[]
	for i in range(10):
		for j in list:
			if j[1]==i:
				data.append(j)
	return data

def cacindex(list, x):
	for i in range(len(list)):
		if x == list[i][0]:
			return i
	return None

def cacswap(x, y,list):
	ox = get_pos_x()
	oy = get_pos_y()
	#print(ox,oy)
	if (x - ox) >0:
		for i in range(ox, x):
			swap(East)
			itemswap(East,list)
	elif (x - ox) <0:
		for i in range(ox, x, -1):
			swap(West)
			itemswap(West,list)
	
	if (y - oy) >0:
		for i in range(oy, y):
			swap(North)
			itemswap(North,list)
	elif (y - oy) <0:
		for i in range(oy, y, -1):
			swap(South)
			itemswap(South,list)
	#print(x,y)

def itemswap(dir,list):
	a=get_pos_x()
	b=get_pos_y()
	move(dir)
	c=get_pos_x()
	d=get_pos_y()
	
	cord1 = [a,b]
	cord2 = [c,d]
	i = cacindex(list, cord1)
	j = cacindex(list, cord2)
	list[i].pop(0)
	list[i].insert(0,cord2)
	list[j].pop(0)
	list[j].insert(0,cord1)
	
clear()

for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			if num_items(Items.Cactus_Seed)<1:
				trade(Items.Cactus_Seed)
			plant(Entities.Cactus)
			move(North)
		move(East)
		
while True:
	x=0
	y=0
	list=[]
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			list.append([[get_pos_x(),get_pos_y()],measure()])
			move(North)
		move(East)
	
	new = cactussort(list)
	
	for i in new:
		go(i[0][0],i[0][1])
		cacswap(x,y,new)
		x +=1
		if x == 10:
			x=0
			y+=1
	harvest()
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if num_items(Items.Cactus_Seed)<1:
				trade(Items.Cactus_Seed)
			plant(Entities.Cactus)
			move(North)
		move(East)