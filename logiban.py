def lojban(lojban_string):
    lojban_number = {
        "pa": 1,
        "re": 2,
        "ci": 3,
        "vo": 4,
        "mu": 5,
        "xa": 6,
        "ze": 7,
        "bi": 8,
        "so": 9,
        "no": 0
    }
    lookup = ""
    counter = 0
    value = ''
    for letter in lojban_string:
        counter += 1
        lookup += letter
        if counter == 2:
            counter = 0
            value += str(lojban_number.get(lookup))
            lookup = ""
    print(value)

lojban("civozeno")