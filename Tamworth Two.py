# Pair of pigs let loose in a 10 x 10 grid
# Their movement depends on the walls of the container and the trees
# Normally they move one square in the direction they are facing
# If their move is blocked - turn 90 clockwise
# If farmer and pigs meet pass through each other if they meet during the move
# Farmers movements mirror that of the pigs

# Program itself:
# Reads two lines of user input:
# 1: two numbers = co-ordinates of pigs
# 2: co-ordinates of farmer
# direction of both - facing upwards (0 degrees)
# Terminates when both farmer and pigs have some co-ordinates - after turn ends

# generate grid
grid = [['.'] * 10 for x in range(10)]
# initialize coordinates
pig_coords, farmer_coords = 0, 0
# input strings
pig_input, farmer_input = 'Enter Pigs Starting Coords : ', 'Enter Farmer Starting Coords : '
# getting user input for farmer and pig coordinates


# turns coords into their correct index's
def real_coords(number):

    x, y = int(number[0]) - 1, 9 - (int(number[1]) - 1)
    return x, y

# user input for pig and farmer coordinates
for i in range(2):
    if i == 0:
        pig_coords = input(pig_input)
        x, y = real_coords(pig_coords)
        grid[y][x] = 'P'

    else:
        farmer_coords = input(farmer_input)
        x, y = real_coords(farmer_coords)
        grid[y][x] = 'F'


# simulating the moves
def simulate_moves(pig, farmer, grid, moves):

    number_of_moves = 0
    pig_dir, farmer_dir = 0, 0
    pig_x, pig_y = real_coords(pig)
    farmer_x, farmer_y = real_coords(farmer)

    for i in range(moves):

        print(print_grid(grid))

        if pig_dir or farmer_dir == 360:
            pig_dir, farmer_dir = 0, 0

        if pig_x == farmer_x and pig_y == farmer_y:
            print(print_grid(grid))
            return 'Farmer and pigs meet on move ' + str(number_of_moves) + ' at ' + str(pig_x) + str(pig_y)

        number_of_moves += 1

        



# Printing the grid
def print_grid(grid):
    for i in grid:
        print(''.join(i))


condition = True

while condition is True:
    options = """
    T int (n): Read in n more lines to put trees in
    M int (n): Simulate next n moves
    X: Program will terminate
    """
    options_char = ['T', 'M', 'X']
    user_input = input(options)

    if user_input.upper()[0] not in options_char:
        print('Please enter a valid char')
        continue

    elif user_input[0] == 'T':
        number = int(user_input[1])
        prompt_user = 'Please enter Tree coordinates : '

        for i in range(number):
            user_input = input(prompt_user)
            x, y = real_coords(user_input)
            grid[y][x] = '*'
        print_grid(grid)

    elif user_input[0] == 'M':
        number = int(user_input[1:])
        print(simulate_moves(farmer_coords, pig_coords, grid, number))

    else:
        print('Terminating Program!')
        condition = False
        break


