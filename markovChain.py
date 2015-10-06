import text_tokenizer
from text_tokenizer import *


def build_dict(tokenized_text):
    tokenized_text.remove('')
    dictionary = {}
    for i, word in enumerate(tokenized_text):
        print(word)
    return dictionary

def generate_sentences(dict):
    return None

if __name__ == '__main__':
    # keep this function call here
    # to see how to enter arguments in Python scroll down
    words = "text.txt"
    tokenized_text = text_Parser(words)
    build_dict(tokenized_text)
