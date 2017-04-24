""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    book = open(file_name, 'rb')
    text = str(book.read())
    book.close
    text = text.replace('\\n', ' ')
    punc = string.punctuation.replace("'", '')
    for char in punc:
        text = text.replace(char, '')
    text = text.lower()
    wordList = text.split()
    return wordList


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    hist = {}
    for word in word_list:
        if word not in hist:
            hist[word] = 1
        else:
            hist[word] += 1
    frequencies = []
    for item in hist:
        frequencies.append(hist[item])
    frequencies.sort()
    for i in range(n,len(frequencies)):
        if frequencies[i] != frequencies[i+1]:
            frequencies = frequencies[:i]
            break
    # Get the n words with the highest frequency, and the rest of the words with the same frequency as the last one.
    topWords = []
    for item in hist:
        if hist[item] in frequencies:
            topWords.append(item)
    return topWords


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('Dracula.txt')
    print(get_top_n_words(word_list, 100))
    # print(string.punctuation)
