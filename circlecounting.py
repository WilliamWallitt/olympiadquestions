def circle_counting(num_friends, words):
    # Create a empty list and populate
    list = []
    # Keeping track of index of list
    # Starting before the first element (-1)
    index = -1
    # Keeping track of the rhyme
    words_left = words
    for i in range(num_friends):
        list.append(i + 1)
    # While loop until only one item in the list
    while len(list) > 1:
        # Add one to index
        index += 1
        # Decrement the counter
        words_left -= 1
        # Check if index is going beyond list index
        if index == len(list):
            index = 0
        # Check if end of rhyme occurs
        if words_left == 0:
            # Reset the rhyme
            words_left = words
            # Remove the value that is at the end of the rhyme
            list.pop(index)
            # Move index left 1 to account for value being removed
            index -= 1

    return list[0]

list = [6,40,20,37,200,230,555,999,82]
list1 = [4,1,8,19,200,173,444,82,999]
answers = [5,40,1,27,149,230,31,9,49]

counter = 0
for item in range(len(list)):
    test = circle_counting(list[counter], list1[counter])
    if test == answers[counter]:
        print("Correct", test)
    counter += 1
