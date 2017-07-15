import sys
from nltk.corpus import words

def GetWordIntersection(first, second):
    return ''.join(set(first).intersection(set(second)))

word_list = []
if sys.argv[1] == 'nltk':
    word_list = words.words()
    word_list = [x.lower() for x in word_list]
elif sys.argv[1] == 'top5000':
    with open("top5000.txt") as f:
        word_list = [word for line in f for word in line.split()]
else:
    print "insert a valid mode"

usa_states = [line.rstrip('\n') for line in open('states.txt')]

for state in usa_states:
    found_match = False
    for word in word_list:
        if GetWordIntersection(state, word) == '':
            every_other_state_shares = True
            for other_state in usa_states:
                if other_state == state:
                    continue
                if GetWordIntersection(other_state, word) == '':
                    every_other_state_shares = False
            if every_other_state_shares:
                found_match = True
                print state + " : " + word
                break;
    if not found_match:
        print "    No match for: " + state
