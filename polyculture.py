clear()
while True:
	for i in range(get_world_size()):
		if not can_harvest():
			move(North)
			continue
		lis = get_companion()
		x = get_pos_x()
		y = get_pos_y()
		go(lis[1],lis[2])
		if lis[0] == Entities.Grass:
			if get_ground_type() == Grounds.Soil:
				till()
		else:
			if get_ground_type() != Grounds.Soil:
				till()

		if lis[0] == Entities.Carrots:
			if num_items(Items.Carrot_Seed)==0:
				trade(Items.Carrot_Seed)
			
		plant(lis[0])
		
		go(x,y)
		harvest()
		if get_ground_type() == Grounds.Soil:
				till()
	move(East)
