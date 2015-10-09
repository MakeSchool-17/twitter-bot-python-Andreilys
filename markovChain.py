import text_tokenizer
from text_tokenizer import *


class SentenceGenerator(object):

    def __init__(self, size):
        self.size = size

    def build_dict(self, tokenized_text):
        tokenized_text.remove('')
        length = len(tokenized_text) - 1
        i = 0
        dictionary = [dict() * self.size]
        for word in tokenized_text:
            if i != length:
                dictionary[word] = tokenized_text[i + 1]
                i = i + 1
        return dictionary


    def generate_sentences(self, dictionary):
        sentence = ""
        for key in dictionary:
            sentence = sentence + ' ' + key
            sentence = sentence + ' ' + dictionary[key]
        print(sentence)

if __name__ == '__main__':
    # tokenize the text
    words = "text.txt"
    tokenized_text = text_Parser(words)
    sentence_generator = SentenceGenerator(10)
    dictionary = SentenceGenerator.build_dict(tokenized_text)
    print(sentenceGenerator.generate_sentences(dictionary))
