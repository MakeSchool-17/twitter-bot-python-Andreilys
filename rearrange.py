import sys
from random import shuffle

total = len(sys.argv)

command_Args = sys.argv[1:]
shuffle(command_Args)

print("The total number of args passed: %d" % total)
print("Shuffled list: %s " % command_Args)
