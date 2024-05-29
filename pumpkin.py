clear()

while True:
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			while (not can_harvest()) and (get_entity_type()!= None):
				if num_items(Items.Fertilizer)==0:
					trade(Items.Fertilizer)
				use_item(Items.Fertilizer)
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Pumpkin:
				if num_items(Items.Pumpkin_Seed)==0:
					trade(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)
			move(North)
		move(East)
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			while get_entity_type() != Entities.Pumpkin:
				if num_items(Items.Pumpkin_Seed)==0:
					trade(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)
				while not can_harvest():
					if num_items(Items.Fertilizer)==0:
						trade(Items.Fertilizer)
					use_item(Items.Fertilizer)
					if get_entity_type() == None:
						break
				
			move(North)
		move(East)
	harvest()
				