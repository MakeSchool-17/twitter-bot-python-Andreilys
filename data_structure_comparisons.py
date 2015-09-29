import sys
import re
import random


# Takes the source text input from user, and tokenizes the text
def tokenizer(source_text):
    file = open(source_text)
    open_file = str(file.read().splitlines())
    tokenized_text = re.split(r'[,;!? ]', open_file)
    return tokenized_text

#
# # histogram that takes a source text as input, and returns histogram data structure (dictionary)
# def histogram_dic(tokenized_text):
#     length = len(source_text)
#     i = 0
#     histogram_Dictionary = dict()
#     for i in xrange(length):
#         # check to see if the dictionary key exists already
#         if source_text[i] in histogram_Dictionary:
#             histogram_Dictionary[source_text[i]] += 1
#         else:
#             histogram_Dictionary[source_text[i]] = 1
#     # removing some unnecssary words
#     histogram_Dictionary.pop('', 0)
#     return histogram_Dictionary
#
# # takes user inputted word, as well as the histogram and returns whether the word exists
# # Big-O complexity is:
# def frequency_dict(word, histogram):
#     length = len(histogram)
#     if histogram.has_key(word):
#         return histogram[word]
# # Key does not exist
#     else:
#         print("Key does not exist")


def histogram_tuples(tokenized_text):
    hgram = []                           # create a new list called hgram
    for word in tokenized_text:                   # for each word in the list of words
        index = find(word, hgram)        # check if word is in hgram already
        if index == None:                # if word is not in histogram
            hgram.append((word, 1))      # add a new word-count pair to hgram
        else:                            # if word is already in hgram
            count = hgram[index][1]      # find its current count
            new_pair = (word, count + 1) # make a new word-count pair
            hgram[index] = new_pair      # replace word-count pair
    return hgram


# Big-O complexity is:
def frequency_tuples(word, histogram):
    return None


def histogram_singlyLinkedList(tokenized_text):
    return None


# Big-O complexity is:
def frequency_singlyLinkedList(word, histogram):
    return None

# def random_word(histogram):
#     list = []
#     for key in histogram:
#         if histogram[key] == 1:
#             list.append(key)
#         else:
#             i = 0
#             while i < histogram[key]:
#                 list.append(key)
#                 i = i + 1
#     length = len(list) - 1
#     random_word = list[random.randint(0, length)]
#     return random_word
#
#
# def weighted_word(histogram):
#     # place holder for number of words
#     number_of_words = 0
#     for key in histogram:
#         number_of_words = number_of_words + histogram[key]
#     # assign the histogram[key] for a new probability
#     for key in histogram:
#         histogram[key] = histogram[key] / float(number_of_words)
#     # select random number between 0 and 1
#     random_Number = random.randint(0, 1)
#     # walk the list, subtracting weight of each number as you go, as you get to 0, choose the item
#     for key in histogram:
#         random_Number = random_Number - histogram[key]
#         if random_Number <= 0:
#             return key



if __name__ == '__main__':
    source_text = raw_input('Enter Source text you would like to create a histogram data structure with: ')
    # histogram that takes a source text as input, and returns histogram data structure (dictionarty)
    tokenized_text = tokenizer(source_text)
    print(histogram_tuples(tokenized_text))

    # returns number of unique words in the histogram
    # number_of_unique_words = unique_words(histogram)
    # print("There are %s unique words" % number_of_unique_words)
    # word = raw_input("Which word would you like to check the frequency of? ")
    # print("The word: %s, appears %d number of times" % (word, frequency(word, histogram)))
