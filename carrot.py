def carrot():	
	
	for i in range(get_world_size()):
			if can_harvest():
				harvest()
			else:
				move(North)
				continue
			#trade(Items.Carrot_Seed)
			if get_ground_type() !=  Grounds.Soil:
				till()
			if num_items(Items.Carrot_Seed)==0:
						trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			move(North)
	move(East)