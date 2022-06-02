def get_tank_volume(width, depth, height):
    volume = int((width*depth*height)/1000)      # use int to 'throw away' all decimal places of the number
    return volume


#print(get_tank_volume(30, 45, 40))
#print(get_tank_volume(36, 45, 124))