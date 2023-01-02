def print_upper_words(words):
    '''Makes word upper case'''
    
    for word in words:
        print(word.upper())

def print_e_word(words):
    '''prints words that start with 'e' and uppercases them'''
    
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper(words, must_start_with):
    '''prints out first letter of word if that letter in plugged in. Also uppercased'''

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break