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
    text = str(book.read()).replace('\\n', ' ')
    book.close
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
    frequently to least frequentlyoccurring
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
    top_n_freq = frequencies[len(frequencies)-n:]
    topWords = []
    for item in hist:
        if hist[item] in top_n_freq:
            topWords.append(item)
    return topWords


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('Dracula.txt')
    print(get_top_n_words(word_list, 100))
    # print(string.punctuation)
