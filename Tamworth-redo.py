# make grid
grid = [['.'] * 10 for x in range(10)]
farmer, pigs = 0, 0


# pig and farmer coordinates from user input
for i in range(2):
    if i == 0:
        pigs = input('Please enter Pigs Coordinates : ').replace(" ", '')
    else:
        farmer = input('Please enter Farmer Coordinates : ').replace(" ", '')


# converting coordinates
def grid_index(x_coord, y_coord):
    x_coord, y_coord = int(x_coord), int(y_coord)
    x, y = x_coord - 1, 9 - (y_coord - 1)
    return x, y


# converting to coordinates
def coordinates(x_coord, y_coord):
    x_coord, y_coord = int(x_coord), int(y_coord)
    x, y = x_coord + 1, y_coord
    return x, y


# taking in user_input and adding it to grid
def user_input_to_coordinates(user_input, replace_with):

    p_or_f = ['P', 'F']

    if len(user_input) == 2:
        x, y = grid_index(user_input[0], user_input[1])
        if grid[y][x] not in p_or_f:
            grid[y][x] = replace_with

    elif len(user_input) == 3:
        if user_input[1] == '0':
            x, y = grid_index(user_input[0:2], user_input[2:])
            if grid[y][x] not in p_or_f:
                grid[y][x] = replace_with
        elif user_input[2] == '0':
            x, y = grid_index(user_input[0], user_input[1:])
            if grid[y][x] not in p_or_f:
                grid[y][x] = replace_with

    elif len(user_input) == 4:
        x, y = grid_index(user_input[0:2], user_input[2:])
        if grid[y][x] not in p_or_f:
            grid[y][x] = replace_with

user_input_to_coordinates(pigs, 'P')
user_input_to_coordinates(farmer, 'F')


# moving the pigs and farmer around the map
def simulating_moves(pigs_location, farmer_location, moves):

    # getting pig index coordinates

    pig_x, pig_y = 0, 0
    farmer_x, farmer_y = 0, 0

    if len(pigs_location) == 2:
        pig_x, pig_y = grid_index(pigs_location[0], pigs_location[1])

    elif len(pigs_location) == 3:
        counter = 0
        for i in pigs_location:
            if i == 0:
                if counter <= 1:
                    pig_x, pig_y = grid_index(pigs_location[0:2], pigs_location[2:])
                else:
                    pig_x, pig_y = grid_index(pigs_location[0], pigs_location[1:])
            counter += 1
    elif len(pigs_location) == 4:
        pig_x, pig_y = grid_index(pigs_location[0:2], pigs_location[2:])

    # getting farmer index coordinates
    if len(farmer_location) == 2:
        farmer_x, farmer_y = grid_index(farmer_location[0], farmer_location[1])
    elif len(farmer_location) == 3:
        counter = 0
        for i in farmer_location:
            if i == 0:
                if counter <= 1:
                    farmer_x, farmer_y = grid_index(farmer_location[0:2], farmer_location[2:])
                else:
                    farmer_x, farmer_y = grid_index(farmer_location[0], farmer_location[1:])
            counter += 1
    elif len(farmer_location) == 4:
        farmer_x, farmer_y = grid_index(farmer_location[0:2], farmer_location[2:])

    # now we have the coordinates, moving them
    # setting initial direction to 0

    pig_direction, farmer_direction = 0, 0

    # where the pig/farmer should be moving
    def where_to_move(x, y, direction):

        if direction >= 360:
            direction = direction - 360

        if direction == 0:
            if y - 1 <= 0:
                direction += 90
            elif grid[y - 1][x] == '*':
                direction += 90
            else:
                y -= 1

        elif direction == 90:
            if x + 1 >= 9:
                direction += 90
            elif grid[y][x + 1] == '*':
                direction += 90
            else:
                x += 1

        elif direction == 180:
            if y + 1 >= 9:
                direction += 90
            elif grid[y + 1][x] == '*':
                direction += 90
            else:
                y += 1

        elif direction == 270:
            if x - 1 <= 0:
                direction += 90
            elif grid[y][x - 1] == '*':
                direction += 90
            else:
                x -= 1

        return x, y, direction

    counter = 0
    for turns in range(int(moves) + 1):

        print_grid(grid)

        grid[pig_y][pig_x] = '.'
        grid[farmer_y][farmer_x] = '.'

        px, py = (coordinates(pig_x, pig_y))
        fx, fy = (coordinates(farmer_x, farmer_y))

        if px == fx and py == fy:
            print('Farmer and pigs meet on move ' + str(counter + 1) + ' at (' + str(px) + ',' + str(py + 1) + ')')
            break
        else:
            print('Farmer: ', fx, fy)
            print('Pigs : ', px, py)

        pig_x, pig_y, pig_direction = where_to_move(pig_x, pig_y, pig_direction)
        farmer_x, farmer_y, farmer_direction = where_to_move(farmer_x, farmer_y, farmer_direction)

        grid[pig_y][pig_x] = 'P'
        grid[farmer_y][farmer_x] = 'F'

        counter += 1


# printing the grid
def print_grid(grid_to_print):

    for _ in grid_to_print:

        print(''.join(_))

print_grid(grid)

# making moves and planting trees
condition = False
while not condition:
    print("""
    Tn : Add Trees To Grid (n = int)
    Mn : Simulate Next n Moves (n = int)
    X  : Terminate Program
    """)
    user_input = input('Enter Here : ').upper().replace(' ', '')

    if user_input[0] == 'T':
        for i in range(int(user_input[1:])):
                tree_planting = input('Enter Tree Coordinates Here : ').replace(' ', '')
                user_input_to_coordinates(tree_planting, '*')
        print_grid(grid)

    # simulating moves
    elif user_input[0] == 'M':
        simulating_moves(pigs, farmer, user_input[1:])

    elif user_input[0] == 'X':
        condition = True
        print("Exiting Now!")
        break



