
def make_anagram_dict(words):

    file = open('words.txt', 'r').readlines()
    list_of_words = []

    for word in file:
        list_of_words.append(word.strip().lower())

    dictionary = {}

    words = list_of_words

    for word in words:
        word = "".join(sorted(word))
        dictionary[word] = []

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in dictionary:
            dictionary.setdefault(sorted_word, []).append(word)
    return dictionary


if __name__ == "__main__":

    dict = make_anagram_dict("words.txt")

    longest_value = 0
    longest_pair = 0
    list = []
    x = ""
    y = ""

    for key in dict:
        value = dict[key]
        if len(value) > longest_value:
            longest_value = len(value)
            list = value
            x = key
        if len(value) == 2:
            if len(value[0]) > longest_pair:
                longest_pair = len(value[0])
                y = value

    print(x + " : " + str(list), y, longest_pair)
