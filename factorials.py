# function factorials(m) calculates m factorial and prints last non zero number
# also prints the number of zeroes after the last non zero number


def factorials(m):
    factorial = 1

    if m < 1 or m > 1000000:
        return "Please enter a valid number"

    else:
        for i in range(1, m + 1):
            factorial = factorial * i

    factorial = str(factorial)
    counter = 0
    # Iterating backwards through number
    for i in factorial[::-1]:

        if i != '0':
            print(int(factorial[-counter - 1]), counter)
            return

        else:
            counter += 1

factorials(100)
