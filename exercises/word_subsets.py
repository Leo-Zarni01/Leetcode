from collections import Counter 
def wordSubsets(wordA, wordB):
    counter = Counter()
    for each_letter in wordB:
        print(each_letter)
        counter |= Counter(each_letter)

    return [a for a in wordA if not counter - Counter(a)]
