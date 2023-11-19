# write the function is_anagram
def is_anagram(test, original):
    anagram = False
    if len(test) == len(original):
        for c in test:
            original = original.lower()
            test = test.lower()
            c = c.lower()
            if c in original and test.count(c) == original.count(c):
                anagram = True
            else:
                anagram = False
                return anagram
        return anagram
    else:
        return anagram
    
"""
Eu Podia apenas ter feito isso:
"""
def is_the_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())