from copy import *

def blackbox():
    # initialize grid
    grid = [['.'] * 10 for i in range(10)]
    # user - add atom positions on grid
    for i in range(5):
        atom = input("Enter atom's position here : ").replace(" ", '')
        x, y = int(atom[0]) - 1, 9 - (int(atom[1]) - 1)
        grid[y][x] = 'A'

    # function - to print grid
    def print_grid(input_grid):
        for i in range(10):
            x = ''.join(input_grid[i])
            print(x)
    # print grid with atoms
    print_grid(grid)

    # function - move ray across grid

    def move(x, y, direction, gridz):
        grid_new = gridz.copy()
        dr = direction
        # takes in x_coord, y_coord, direction and grid
        condition = True
        while condition:
            if dr == 'T':
                if y > 9 or y < 0 or y + 1 > 9:
                    print_grid(grid_new)
                    print(dr, y)
                    return
                # checking next position
                if grid_new[y + 1][x] == '.':
                    grid_new[y + 1][x] = '+'
                    y += 1
                if grid_new[y + 1][x] == 'A':
                    grid_new[y + 1][x] = 'A*'
                    y += 1
                    print_grid(grid_new)
                    print('Absorbed')
                    return
                if grid_new[y + 1][x + 1] == 'A' and grid_new[y + 1][x - 1] == 'A':
                    print_grid(grid_new)
                    print('Reflected')
                    return
                if grid_new[y + 1][x + 1] == 'A':
                    dr = 'R'
                if grid_new[y + 1][x - 1] == 'A':
                    dr = 'L'
                if grid_new[y + 1][x] == '+':
                    y += 1

            if dr == 'B':
                if y > 9 or y < 0 or y - 1 < 0:
                    print_grid(grid_new)
                    print(dr, y)
                    return
                if grid_new[y - 1][x] == '.':
                    grid_new[y - 1][x] = '+'
                    y -= 1
                if grid_new[y - 1][x] == 'A':
                    grid_new[y - 1][x] = 'A*'
                    y -= 1
                    print_grid(grid_new)
                    print('Absorbed')
                    return
                if grid_new[y - 1][x + 1] == 'A' and grid_new[y + 1][x - 1] == 'A':
                    print_grid(grid_new)
                    print('Reflected')
                    return
                if grid_new[y - 1][x + 1] == 'A':
                    dr = 'R'
                if grid_new[y - 1][x - 1] == 'A':
                    dr = 'L'
                if grid_new[y - 1][x] == '+':
                    y -= 1

            if dr == 'L':
                if x > 9 or x < 0 or x + 1 > 9:
                    print_grid(grid_new)
                    print(dr, x)
                    return
                if grid_new[y][x + 1] == '.':
                    grid_new[y][x + 1] = '+'
                    x += 1
                if grid_new[y][x + 1] == 'A':
                    grid_new[y][x + 1] = 'A*'
                    print_grid(grid_new)
                    print('Absorbed')
                    return
                if grid_new[y + 1][x + 1] == 'A' and grid_new[y - 1][x + 1] == 'A':
                    print_grid(grid_new)
                    print('Reflected')
                    return
                if grid_new[y + 1][x + 1] == 'A':
                    dr = 'B'
                if grid_new[y - 1][x + 1] == 'A':
                    dr = 'T'
                if grid_new[y][x + 1] == '+':
                    x += 1

            if dr == 'R':
                if x > 9 or x < 0 or x - 1 < 0:
                    print_grid(grid_new)
                    print(dr, x)
                    return
                if grid_new[y][x - 1] == '.':
                    grid_new[y][x - 1] = '+'
                    x -= 1
                if grid_new[y][x - 1] == 'A':
                    grid_new[y][x - 1] = 'A*'
                    print_grid(grid_new)
                    print('Absorbed')
                if grid_new[y + 1][x - 1] == 'A' and grid_new[y - 1][x - 1] == 'A':
                    print_grid(grid_new)
                    print('Reflected')
                    return
                if grid_new[y + 1][x - 1] == 'A':
                    dr = 'B'
                if grid_new[y - 1][x - 1] == 'A':
                    dr = 'T'
                if grid_new[y][x - 1] == '+':
                    x += 1

    while True:
        ray = input("Enter ray path : ").replace(" ", '').upper()
        ray_dir = ray[0]
        ray_pos = int(ray[1]) - 1
        if ray == "X0":
            return
        else:

            if ray_dir == 'T':
                y_coord = 0
                x_coord = ray_pos
                grid[y_coord][x_coord] = '+'
                move(x_coord, y_coord, ray_dir, grid)

            elif ray_dir == 'B':
                y_coord = 9
                x_coord = ray_pos
                grid[y_coord][x_coord] = '+'
                move(x_coord, y_coord, ray_dir, grid)

            elif ray_dir == 'L':
                y_coord = 9 - ray_pos
                x_coord = 0
                grid[y_coord][x_coord] = '+'
                move(x_coord, y_coord, ray_dir, grid)

            elif ray_dir == 'R':
                y_coord = 9 - ray_pos
                x_coord = 9
                grid[y_coord][x_coord] = '+'
                move(x_coord, y_coord, ray_dir, grid)

            else:
                print("Ray path parameters not met : ")


blackbox()