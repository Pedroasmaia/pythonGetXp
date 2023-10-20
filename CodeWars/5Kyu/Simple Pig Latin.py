'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
def pig_it(text):
    words = text.split(' ')
    response = ''
    for word in words:
        if word.isalpha():
            c = word[0] + 'ay'
            remaining = word[1:]
            response += remaining+c+" " 
        else:
            response += word
    return response.strip()
'''
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
