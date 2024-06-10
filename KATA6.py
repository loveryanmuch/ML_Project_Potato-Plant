def whereCanIPark(spots, vehicle):
    valid_spots = {
        'regular': ['R'],
        'small': ['R', 'S'],
        'motorcycle': ['R', 'S', 'M']
    }
    for y in range(len(spots)):
        for x in range(len(spots[y])):
            if spots[y][x] in valid_spots[vehicle]:
                return [x, y]
                
    return False
