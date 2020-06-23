def compute():
    name = input("Enter the name of the company : ").strip()
    letters = {}
    for letter in name:
        if letter is ' ':
            continue
        else:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    
    sortedLetters = sorted(letters.items(), key = lambda x : x[1], reverse = True)
    ctr = 0
    for i in sortedLetters:
        if ctr == 3:
            break
        print(i[0] + ' ' + str(i[1]))
        ctr += 1

if __name__ == "__main__":
    compute()