def ISBN(number, missing_value_index=0):

    # Missing allowing the 10th digit to be an X = 10
    # As sometime the last one = 10 is needed

    # Convert number to string
    numbers = str(number)
    # Variables for the total number and the multiplication of each number
    total = 0
    times = 10

    # Variables for finding missing value
    starting_thingy = 0
    list = []

    # Variable for length of input
    number_length = 10

    if missing_value_index != 0:
        # So if user using the second argument (missing_value_index)
        number_length = 9
        # iterate over numbers and add them to a list
        for item in numbers:
            # item is a string, convert to int
            item = int(item)
            list.append(item)
        # Insert 0 into the list at the index specified
        list.insert(missing_value_index - 1, starting_thingy)
        # Go through list
        for i in list:
            # add each number * value to total
            total += times * i
            times -= 1

            # turns each item in list to a string
            s = map(str, list)
            # Joins all the items together to form one number
            s = ''.join(s)
            # Calls the function on the number to check if its right
            s = ISBN(s)

            # Check if the first index (first return item) returns valid
            if s[0] == 'Valid ISBN':
                print(s)
                print(starting_thingy)
                print(list)
                # If valid break out of the function, after printing the info
                return
            # Check if the current value inserted into said index is divisible by 11
            if total % 11 != 0:
                if starting_thingy >= 11:
                    return
                # Remove value inserted
                list.pop(missing_value_index - 1)
                # Add one to that value and then append it back into the list same index
                starting_thingy += 1
                list.insert(missing_value_index - 1, starting_thingy)
                # And then try again

    # Check if number len is valid
    if len(numbers) != number_length:
        print("Invalid ISBN number")
        return
    # Add up the numbers to get total
    for number in numbers:
        number = int(number)
        total += times * number
        times -= 1
    # See if total is divisible by 11, return if valid or not
    if total % 11 == 0:
        return "Valid ISBN", total
    else:
        return "Invalid ISBN", total




def using_X(number, index=10):
    number = str(number)
    


if __name__ == "__main__":

    print(ISBN(3540678654))
    ISBN(354067865, 10)




