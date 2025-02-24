import requests # library to download book from web link

# Links for the two books
link_1 = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt" # Pride & Prejudice by Jane Austen
link_2 = "https://www.gutenberg.org/cache/epub/11/pg11.txt" # Alice's Adventures in Wonderland by Lewis Carroll

# Extract books, set up empty lists for unique words and set up punctuations to be filtered out
result_1 = requests.get(link_1)
result_2 = requests.get(link_2)
# print(result.text)
unique_words_1 = {}
unique_words_2 = {}
punctuations = ";:,.'!?-=()[]/|{}"

# Process for Book #1 (Pride & Prejudice)
# Loop to iterate over each line and replace punctuations
for line in result_1.text.splitlines():
    for p in punctuations:
        line = line.replace(p, " ")
    words = line.split()
# Loop to iterate over each word to count occurrences of unique words & add them to empty list
    for word in words:
        word = word.lower()
        unique_words_1[word] = unique_words_1.get(word, 0) + 1

# Process for Book #2 (Alice's Adventures in Wonderland)
# Loop to iterate over each line and replace punctuations
for line in result_2.text.splitlines():
    for p in punctuations:
        line = line.replace(p, " ")
    words = line.split()
# Loop to iterate over each word to count occurrences of unique words & add them to empty list
    for word in words:
        word = word.lower()
        unique_words_2[word] = unique_words_2.get(word, 0) + 1

# Saving values of unique word frequencies in a list for each book
freq_1 = list(unique_words_1.items())
freq_2 = list(unique_words_2.items())

# Printing out results to see which book has more unique words
print(f"Pride and Prejudice has {len(freq_1)} unique words while Alice's Adventures in Wonderland has {len(freq_2)} unique words")
# Pride and Prejudice has more words (7762 vs 3647 unique words)