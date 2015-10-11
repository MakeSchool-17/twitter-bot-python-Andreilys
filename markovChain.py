import text_tokenizer
from text_tokenizer import *
import random


class SentenceGenerator(object):
    def __init__(self, size):
        self.size = size

    def build_dict(self, tokenized_text):
        tokenized_text.remove('')
        length = len(tokenized_text) - 1
        i = 0
        List = []
        for word in tokenized_text:
            if i != length:
                dictionary = dict()
                dictionary[word] = tokenized_text[i + 1]
                List.append(dictionary)
                i = i + 1
        return List

    def generate_sentences(self, List):
        sentence = ""
        length = len(List)
        for i in range(5):
            random_Number = random.randrange(0, length, 1)
            sentence = sentence + " " + List[random_Number].values()[0] + " " + List[random_Number].keys()[0]
        return sentence

if __name__ == '__main__':
    # tokenize the text
    words = "text.txt"
    tokenized_text = text_Parser(words)
    sentence_generator = SentenceGenerator(10)
    List = sentence_generator.build_dict(tokenized_text)
    print(sentence_generator.generate_sentences(List))
