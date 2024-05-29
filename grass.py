def grass():	
	for i in range(get_world_size()):
			if not can_harvest():
				move(North)
				continue
			harvest()
			
				
			if get_ground_type() ==  Grounds.Soil:
				till()
			
			move(North)
	move(East)