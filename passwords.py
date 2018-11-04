def password(input):
    repeated = ''
    counter = 0
    input = str(input)
    if len(input) > 10:
        print("invalid characters")
        return
    elif input.isupper() is False:
        print("invalid character")
        return
    else:
        for character in input:
            repeated += character
            counter += 1
            if len(repeated) > 1:
                if character == repeated[counter - 2]:
                    print("Rejected", character, 'is repeated')
                    return
                if len(repeated) >= 4:
                    if repeated[counter - 4:counter - 3] == repeated[counter -2:counter - 1]:
                        print("Rejected",repeated[counter - 4: counter - 2], 'is repeated')
                        return

                    elif len(repeated) == len(input):
                        print('Accepted')
                        return

list = ['A', 'LONDON', 'BIOGRAPHY','APRICOT', 'AA', 'QUININE','HELLO','COMMITTEE']
counter = 0
for i in range(len(list)):
    password(list[counter])
    counter += 1