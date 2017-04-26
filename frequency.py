""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import re


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    book = open(file_name, 'rb')
    text = str(book.read())
    book.close
    rxHeader = re.compile("\*\*\* START OF THIS PROJECT GUTENBERG EBOOK.*?\*\*\*")
    rxFooter = re.compile("\*\*\* END OF THIS PROJECT GUTENBERG EBOOK.*?\*\*\*")
    header = rxHeader.search(text)
    footer = rxFooter.search(text)
    text = text[header.end():footer.start()]
    # Remove everything added by Project Gutenberg. (Leaves Table of Contents and other information in original printing)
    text = text.replace('\\n', ' ')  # Get rid of newline characters
    punc = string.punctuation.replace("'", '')
    for char in punc:
        text = text.replace(char, '')  # get rid of all punctuation except apostrophes
    text = text.lower()  # make everything lowercase
    wordList = text.split()  # Break text into a list of words
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
    frequencyList = []
    for key, value in hist.items():
        frequencyList.append((value, key))
    frequencyList.sort(reverse=True)

    if len(frequencyList) <= n:
        return frequencyList

    lowFreq = frequencyList[n-1][0]
    topWords = []
    for word in frequencyList:
        if word[0] >= lowFreq:
            topWords.append(word)
    return topWords


if __name__ == "__main__":
    numWords = 100
    print("Running WordFrequency Toolbox")
    word_list = get_word_list('Dracula.txt')
    topNWords = get_top_n_words(word_list, numWords)
    print('Words with top ' + str(numWords) + ' rankings:\n(Found ' + str(len(topNWords)) + ' words)')
    for word in topNWords:
        print (word[1] + '\t' + str(word[0]))
