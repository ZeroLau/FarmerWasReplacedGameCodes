def noncycle():	
	b4 = [get_pos_x(),get_pos_y()]
	if move(North) == True:
		do_a_flip()
	elif move(East) == True:
		do_a_flip()
	elif move(West) == True:
		do_a_flip()
	elif move(South) == True:
		do_a_flip()
	
	
	now = [get_pos_x(),get_pos_y()]
	olddiff = []
	while get_entity_type() != Entities.Treasure:
		diff = [now[0]-b4[0],now[1]-b4[1]]
		b4 = now
		while diff == [0,1]:
			if move(West)==True:
				break
			move(North)
			break
	
		while diff == [1,0]:
			if move(North)==True:
				break
			move(East)
			break
		
		while diff == [0,-1]:
			if move(East)==True:
				break
			move(South)
			break
		
		while diff == [-1,0]:
			if move(South)==True:
				break
			move(West)
			break
		
		if diff == [0,0]:
			while olddiff == [0,1]:
				if move(East)==True:
					break
				move(South)
				break
	
			while olddiff == [1,0]:
				if move(South)==True:
					break
				move(West)
				break
	
			while olddiff == [0,-1]:
				if move(West)==True:
					break
				move(North)
				break

			while olddiff == [-1,0]:
				if move(North)==True:
					break
				move(East)
				break

		now = [get_pos_x(),get_pos_y()]
		olddiff = diff
		
def mapping():
	b4 = [get_pos_x(),get_pos_y()]
	if move(North) == True:
		do_a_flip()
	elif move(East) == True:
		do_a_flip()
	elif move(West) == True:
		do_a_flip()
	elif move(South) == True:
		do_a_flip()
	
	map = []
	now = [get_pos_x(),get_pos_y()]
	olddiff = []
	diff = [now[0]-b4[0],now[1]-b4[1]]
	map.append([diff, b4])
	while True:
		
		
		while diff == [0,1]:
			if move(West)==True:
				break
			move(North)
			break
	
		while diff == [1,0]:
			if move(North)==True:
				break
			move(East)
			break
		
		while diff == [0,-1]:
			if move(East)==True:
				break
			move(South)
			break
		
		while diff == [-1,0]:
			if move(South)==True:
				break
			move(West)
			break
		
		if diff == [0,0]:
			while olddiff == [0,1]:
				if move(East)==True:
					break
				move(South)
				break
	
			while olddiff == [1,0]:
				if move(South)==True:
					break
				move(West)
				break
	
			while olddiff == [0,-1]:
				if move(West)==True:
					break
				move(North)
				break

			while olddiff == [-1,0]:
				if move(North)==True:
					break
				move(East)
				break
				
		b4 = now
		now = [get_pos_x(),get_pos_y()]
		olddiff = diff
		diff = [now[0]-b4[0],now[1]-b4[1]]
		if map[0] == [diff, b4]:
			break
		map.append([diff, b4])
	return map

def ascindex(list, x):
	for i in range(len(list)):
		if x == list[i][1]:
			return i
	return None

def dungo(list,x,y):
	target = [x,y]
	ox = get_pos_x()
	oy = get_pos_y()
	
	original = [ox,oy]
	
	tdex = ascindex(list, target)
	odex = ascindex(list, original)
	
	if tdex>odex:
		for i in list[odex:tdex]:
			
			if i[0]==[0,1]:
				move(North)
			elif i[0] == [1,0]:
				move(East)
			elif i[0] == [0,-1]:
				move(South)
			elif i[0] == [-1,0]:
				move(West)
	else:
		
		for i in range(odex,tdex,-1):
			
			if list[i-1][0]==[0,1]:
				move(South)
			elif list[i-1][0] == [1,0]:
				move(West)
			elif list[i-1][0] == [0,-1]:
				move(North)
			elif list[i-1][0] == [-1,0]:
				move(East)
	

clear()

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant(Entities.Bush)
			move(North)
		move(East)

	while get_entity_type()!=Entities.Hedge:
		if num_items(Items.Fertilizer)==0:
			trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
	map = mapping()
	noncycle()
	newx, newy = measure()
	for i in range(150):
		while get_entity_type() == Entities.Treasure:
			if num_items(Items.Fertilizer)==0:
				trade(Items.Fertilizer)
			use_item(Items.Fertilizer)
		dungo(map, newx,newy)
		newx, newy = measure()
		
	
	harvest()