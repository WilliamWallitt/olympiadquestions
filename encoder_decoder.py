def encoder_decoder():
    dict = {}
    dict_reverse = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,.'
    key = []
    counter = 0
    while True:
        user_input = input("""
    1) Enter an encoding key string.
    2) Encode a section of text using the current key.
    3) Decode a section of text using the current key.
    4) Exit the program.
    Enter Number Here : """)

        if user_input == '4':
            print('Exiting Now!')
            return

        elif user_input == '1':
            counter += 1
            if counter > 1:
                key = []
            user_input = input("Enter encoding key string : ")
            user_input.upper().strip()
            for char in user_input:
                if char not in key:
                    key.append(char)

            key = "".join(key).upper()
            for i in alphabet:
                if i not in key:
                    key += i
            print('Encoded Key : ' + key)

        elif user_input == '2':
            index = 0
            output = ''
            value = 0
            user_input = input("Enter string to encode : ")
            user_input.strip()
            values = [x + 1 for x in range(29)]
            dict[' '] = 29
            dict_reverse[29] = ' '
            for char in alphabet:

                dict[char] = values[index]
                dict_reverse[values[index]] = char
                index += 1
            # Check lim < 250 chars
            # # - character = break

            for char in user_input:
                if char == '#':
                    break
                value += dict[char.upper()]
                if value >= 29:
                    value = value - 29
                output += key[value]

            if ' ' not in user_input:
                    output += ' '
            print('Encoded string : ' + output)

        elif user_input == '3':

            counter = 0
            index = 0
            output = ''
            condition = False
            user_input = input("Enter string to decode : ")
            user_input.strip().upper()

            if len(key) == 0:

                print('Please enter an encoding key')
                encoder_decoder()
                return

            else:

                while not condition:

                    for value in key:

                        if counter > 29:
                            counter = 1

                        else:
                            counter += 1

                        if index >= len(user_input):
                            index = 0

                        if value == user_input[index].upper():

                            index += 1

                            output += str(dict_reverse[counter - 1])
                            counter = 1

                            if len(output) == len(user_input):

                                condition = True
                                break

            print('Decoded Key : ' + output)


encoder_decoder()
