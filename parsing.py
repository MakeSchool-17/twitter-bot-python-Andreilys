import re


def text_Parser(text):
    new_text = text.read()
    no_punc_text = remove_punctuation(new_text)
    tokens = split_on_whitespace(no_punc_text)
    return tokens


def split_on_whitespace(text):
    return re.split('\s+', text)


def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('-', ' ', no_punc_text)
    return no_punc_text


if __name__ == '__main__':
    user_input = raw_input("Which file would you like to parse? ")
    file = open(user_input)
    print(text_Parser(file))
