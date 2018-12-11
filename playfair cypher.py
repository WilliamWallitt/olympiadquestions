# 2 = 5x5 grid, each containing jumbled alphabet
# 1) split word into pairs - each char in pair encode using L then R grid
# 2) if len(word) != even, X is added to the end of word before encoding
# 3) if two letters are on the same row, each one is replaced by the one on its right
# - wrapped around the same row if necessary.
# 4) if not, treat the two positions on the grid as two corners of a triangle
# 5) encrypt each grid (top / bot) with keyword


def playfair_cypher():
    alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    grid1, grid2 = [], []
    for i in range(2):
        if i == 0:
            grid = grid1
        else:
            grid = grid2
        user_input = input("Enter word to encrypt grids : ").upper()
        if grid == grid1:
            for char in user_input:
                if char not in grid:
                    grid.append(char)
            for a in alphabet:
                if a not in grid:
                    grid.append(a)
        else:
            for a in alphabet[::-1]:
                if a not in user_input:
                    grid2.append(a)
            for char in user_input[::-1]:
                grid2.append(char)

    def printing_grid(grid1, grid2):
        print("")
        printing = ""
        printing1 = ""
        counter = 0

        for char, char1 in zip(grid1, grid2):
            counter += 1
            printing += char
            printing1 += char1
            if len(printing) >= 5:
                print(" ".join(printing), "  ", " ".join(printing1))
                printing, printing1 = "", ""
        print("")
    printing_grid(grid1, grid2)

    def encode(input_user):
        str(input_user).upper()
        # if user_input an uneven number, add X to end
        if len(input_user) % 2 != 0:
            input_user += 'X'
        pairs = [input_user[i:i+2] for i in range(0, len(input_user), 2)]
        output = ''
        row_end = {4: 1, 9: 2, 14: 3, 19: 4, 24: 5}
        for pair in pairs:
            x, y = pair[0], pair[1]
            index_x, index_y, row_x, row_y = 0, 0, 1, 1
            row_end_x, row_end_y = 0, 0
            for i in grid1:
                if i == x:
                    break
                else:
                    index_x += 1
            for j in grid2:
                if j == y:
                    break
                else:
                    index_y += 1
            for key in row_end:
                if index_x <= key:
                    row_x = row_end[key]
                    row_end_x = key
                    break
            for key in row_end:
                if index_y <= key:
                    row_y = row_end[key]
                    row_end_y = key
                    break

            if row_x == row_y:
                if index_x + 1 > row_end_x:
                    output += grid1[index_x - 4]
                else:
                    output += grid1[index_x + 1]
                if index_y + 1 > row_end_y:
                    output += grid2[index_y - 4]
                else:
                    output += grid2[index_y + 1]
            else:
                diff = 5 * abs(row_x - row_y)
                if row_x > row_y:
                    output += grid1[index_x - diff]
                    output += grid2[index_y + diff]
                else:
                    output += grid1[index_x + diff]
                    output += grid2[index_y - diff]

        print(output)

    def decode(input_user):
        str(input_user).upper()
        # if user_input an uneven number, add X to end
        if len(input_user) % 2 != 0:
            input_user += 'X'
        pairs = [input_user[i:i + 2] for i in range(0, len(input_user), 2)]
        output = ''
        row_end = {4: 1, 9: 2, 14: 3, 19: 4, 24: 5}
        for pair in pairs:
            x, y = pair[0], pair[1]
            index_x, index_y, row_x, row_y = 0, 0, 1, 1
            row_end_x, row_end_y = 0, 0
            for i in grid1:
                if i == x:
                    break
                else:
                    index_x += 1
            for j in grid2:
                if j == y:
                    break
                else:
                    index_y += 1
            for key in row_end:
                if index_x <= key:
                    row_x = row_end[key]
                    row_end_x = key
                    break
            for key in row_end:
                if index_y <= key:
                    row_y = row_end[key]
                    row_end_y = key
                    break

            if row_x == row_y:
                if index_x - 1 < row_end_x - 5:
                    output += grid1[index_x + 4]
                else:
                    output += grid1[index_x - 1]
                if index_y - 1 < row_end_y - 5:
                    output += grid2[index_y + 4]
                else:
                    output += grid2[index_y - 1]
            else:
                diff = 5 * abs(row_x - row_y)
                if row_x > row_y:
                    output += grid1[index_x - diff]
                    output += grid2[index_y + diff]
                else:
                    output += grid1[index_x + diff]
                    output += grid2[index_y - diff]
        output_check = ''
        for i in output:
            if i == 'X':
                continue
            else:
                output_check += i

        print(output_check)

    while len(grid1) != 0:

        user_input = input("Please enter a E/D/Q to Encode / Decode / Quit : ")

        if user_input == "E":
            user_input = input().upper()
            encode(user_input)

        elif user_input == "D":
            user_input = input().upper()
            decode(user_input)

        elif user_input == "Q":
            break


playfair_cypher()
