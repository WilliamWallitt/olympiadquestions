def word_counter(file):
    # Open file and iterate through
    name = file
    file = open(file, 'r')
    counter = 0

    for line in file:
        # Using the line.split() method to count each word
        for word in line.split():
            counter += 1
    print("Number of words for", name, 'is', counter)


word_counter("words.txt")