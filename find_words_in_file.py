punctuation = ",.?!"

def find_words(filename):
    """
    print the letter words starting with "b"
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        for line in f:
            # sanitize line
            for p in punctuation:
                line = line.replace(punctuation, " ")
            # need to break down line into words
            words = line.split() # by default splits by space
            # check each word
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B":
                    print(word)

find_words("input.txt")