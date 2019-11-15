# the_minion_game.py

def minion_game(string):
    string = string.upper()
    stuart = 0
    kevin = 0
    vowels = 'AEOIU'

    for i in range(len(string)):
        if string[i] in vowels:     # checks whether the letter is a vowel
            kevin += len(string) - i    # subtracts the index position of the vowel from length of string
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print('Stuart',stuart)
    elif kevin > stuart:
        print('Kevin',kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)