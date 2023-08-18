def get_count(sentence):
    total = 0
    for vowel in sentence:
        if vowel == 'a' or vowel == 'e'  or vowel == 'i' or vowel == 'o' or vowel == 'u':
            total+=1
    return total