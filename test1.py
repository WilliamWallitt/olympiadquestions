from test import make_anagram_dict


def anaquery(file):

    while input != "":

        word = input("Please enter a word to find its anagram : ")
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) == 0:
            print("Exiting now!")
            return
        else:
            search = make_anagram_dict(file)
            try:
                if len(search[sorted_word]) == 1:
                    print("No Anagram Found!")
                else:
                    for i in search[sorted_word]:
                        if i != word:
                            print("Anagrams are :", i)
            except KeyError:
                print("No Anagram Found! - Key Error")
            print("")


anaquery("words.txt")