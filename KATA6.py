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


print(whereCanIPark(
  [
    ['s', 's', 's', 'S', 'R', 'M'],
    ['s', 'M', 's', 'S', 'r', 'M'],
    ['s', 'M', 's', 'S', 'r', 'm'],
    ['S', 'r', 's', 'm', 'r', 'M'],
    ['S', 'r', 's', 'm', 'r', 'M'],
    ['S', 'r', 'S', 'M', 'M', 'S']
  ],
  'regular'
))

print(whereCanIPark(
  [
    ['M', 'M', 'M', 'M'],
    ['M', 's', 'M', 'M'],
    ['M', 'M', 'M', 'M'],
    ['M', 'M', 'r', 'M']
  ],
  'small'
)) 

print(whereCanIPark(
  [
    ['s', 's', 's', 's', 's', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['S', 'r', 's', 'm', 'r', 's'],
    ['S', 'r', 's', 'm', 'R', 's'],
    ['S', 'r', 'S', 'M', 'm', 'S']
  ],
  'motorcycle'
))