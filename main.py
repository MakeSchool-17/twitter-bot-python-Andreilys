import re
import parsing
import histogram
import hashtable
import Heap
from parsing import *
from hashtable import *
from histogram import *
from Heap import MaxHeap

# If we subtract the Unix dictionary's keys from our word count dict's keys,
#  we can find specialized/jargon words in our corpus or words
# we didn't normalize. We can even use this to refine our regular expressions
# and normalization techniques!

if __name__ == '__main__':
    user_input = "humannature.txt"
    tokenized_text = text_Parser(user_input)
    histogram = histogram(tokenized_text)
    max_heap = MaxHeap()
    for i in histogram:
        max_heap.insert((i, histogram[i]))
    print(max_heap.peek(20)[0])
