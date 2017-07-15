from nltk.corpus import words

usa_states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey", "new mexico", "new york", "north carolina", "north dakota", "ohio", "oklahoma", "oregon", "pennsylvania" , "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming"]

def GetWordIntersection(first, second):
    return ''.join(set(first).intersection(set(second)))

word_list = words.words()
word_list_lower = [x.lower() for x in word_list]

for state in usa_states:
    for word in word_list_lower:
        if GetWordIntersection(state, word) == '':
            every_other_state_shares = True
            for other_state in usa_states:
                if other_state == state:
                    continue
                if GetWordIntersection(other_state, word) == '':
                    every_other_state_shares = False
            if every_other_state_shares:
                print state + " : " + word
                break;
