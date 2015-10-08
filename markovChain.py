import text_tokenizer
from text_tokenizer import *


def build_dict(tokenized_text):
    tokenized_text.remove('')
    length = len(tokenized_text)
    dictionary = dict()
    for i, word in enumerate(tokenized_text):
        dictionary[(word, tokenized_text[i + 1 - length])] = 0
    return dictionary

def generate_sentences(dict):
    return None

if __name__ == '__main__':
    # keep this function call here
    # to see how to enter arguments in Python scroll down
    words = "text.txt"
    tokenized_text = text_Parser(words)
    print(build_dict(tokenized_text))
