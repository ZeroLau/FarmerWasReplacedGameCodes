clear()
for i in range(get_world_size()):
	for j in range(get_world_size()):
		if num_items(Items.Sunflower_Seed)==0:
			trade(Items.Sunflower_Seed)
		till()
		plant(Entities.Sunflower)
		move(North)
	move(East)
while True:
	max = 0
	movto(0,0)
	cord = []
	temp = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() != Entities.Sunflower:
				if num_items(Items.Sunflower_Seed)==0:
					trade(Items.Sunflower_Seed)
				plant(Entities.Sunflower)
			temp = measure()
			while not can_harvest():
				if num_items(Items.Fertilizer)==0:
					trade(Items.Fertilizer)
				use_item(Items.Fertilizer)

			if temp >max:
				max = temp
				cord = []
				#print(max)
			if temp == max:
				cord.append([get_pos_x(),get_pos_y()])
			move(North)
		move(East)

	for i in cord:
		go(i[0],i[1])
		harvest()
	go(0,0)
	#for i in range(get_world_size()):
		#for j in range(get_world_size()):	
			#if get_entity_type() != Entities.Sunflower:
				#if num_items(Items.Sunflower_Seed)==0:
					#trade(Items.Sunflower_Seed)
				#plant(Entities.Sunflower)
			#move(North)
		#move(East)
		