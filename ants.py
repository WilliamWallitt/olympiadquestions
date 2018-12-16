def ants():
    # starting postion = (x, y) - coords then T/B/L/R on grid
    ant1 = input("Enter starting position of ant1 : ")
    ant2 = input("Enter starting position of ant2 : ")
    # create 11x11 grid of '*'
    grid = [['.'] * 11 for _ in range(11)]
    # remove spaces from string input
    ant1 = ant1.replace(" ", "")
    ant2 = ant2.replace(" ", "")

    def moving(x, y, dr):
        """

        :param x: x - coordinate
        :param y: y - coordinate
        :param dr: direction (0, 360)
        :return: x, y, dr - updated
        """
        if dr == 0:
            y -= 1
            if y > 10 or y < 0:
                return x, y, dr
            if grid[y][x] == '*':
                dr -= 90
                grid[y][x] = '.'
            else:
                grid[y][x] = '*'
                dr += 90
        elif dr == 90:
            x += 1
            if x > 10 or x < 0:
                return x, y, dr
            if grid[y][x] == '*':
                grid[y][x] = '.'
                dr -= 90
            else:
                grid[y][x] = '*'
                dr += 90
        elif dr == 180:
            y += 1
            if y > 10 or y < 0:
                return x, y, dr
            if grid[y][x] == '*':
                grid[y][x] = '.'
                dr -= 90
            else:
                grid[y][x] = '*'
                dr += 90
        else:
            x -= 1
            if x > 10 or x < 0:
                return x, y, dr
            if grid[y][x] == '*':
                grid[y][x] = '.'
                dr -= 90
            else:
                grid[y][x] = '*'
                dr += 90

        if dr < 0:
            dr += 360
        if dr > 360:
            dr -= 360
        if dr == 360:
            dr = 0

        return x, y, dr

    # holds starting degree's of ant
    dict = {'T': 0, 'B': 180, 'L': 270, 'R': 90}

    # if false, ant removed from grid
    ant1_true = True
    ant2_true = True

    # if user enters a two digit number
    if len(ant1) > 3:
        x = 3
    else:
        x = 2
    if len(ant2) > 3:
        y = 3
    else:
        y = 2

    # initialise ant1/ant2 starting position and dir on the grid
    x1, y1, dr1, x2, y2, dr2 = int(ant1[0]) - 1, 10 - (int(ant1[1]) - 1), dict[ant1[x].upper()], \
                               int(ant2[0]) - 1, 10 - (int(ant2[1]) - 1), dict[ant2[y].upper()]

    # prints grid and ant's coordinates and heading
    def printing(grid_list):
        for row in grid_list:
            # join list elements, with no whitespace/comma between
            row = ''.join(row)
            print(row)
        for key in dict:
            if dict[key] == dr1:
                if not ant1_true:
                    print("Removed ant")
                else:
                    print(x1 + 1, 11 - y1, key)
        for key in dict:
            if dict[key] == dr2:
                if not ant2_true:
                    print("Removed ant")
                else:
                    print(x2 + 1, 11 - y2, key)

    # keep inputting moves until user exits programme
    while True:

        move = input("Enter number of moves : ")
        move = int(move)

        if move == -1:
            return "Exiting now!"
        else:

            counter_x = 0
            counter_y = 0
            # Actual index in list
            for i in range(move):

                # skip first move
                if x1 and ant1[0] and y1 == ant1[1] and counter_x == 0:
                    counter_x += 1
                    continue
                if x2 == ant2[0] and y2 == ant2[1] and counter_y == 0:
                    counter_y += 1
                    continue

                # set the returned values = updated x,y,dr values
                x1, y1, dr1 = moving(x1, y1, dr1)
                x2, y2, dr2 = moving(x2, y2, dr2)
                # check if ant still on grid, if not remove ant
                if x1 > 10 or x1 < 0 or y1 < 0 or y1 > 10:
                    ant1_true = False
                    continue
                if x2 > 10 or x2 < 0 or y2 < 0 or y2 > 10:
                    ant2_true = False
                    continue

            # if both ants are off the board then exit the programme (as game over)
            if ant1_true is False and ant2_true is False:
                return
            # call function - printing()
            printing(grid)

ants()
