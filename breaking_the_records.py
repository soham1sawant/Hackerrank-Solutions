# breaking_the_records.py

def breakingRecords(scores):
    # For high scores
    highscores = [scores[0]]            # list to score all the highest scores
    for i in range(1 , len(scores)):        # iterates through the second element of scores till the last
        if highscores[i-1] > scores[i]:     # checks if the previous element is greater than the current element
            highscores.append(highscores[i-1])      # if true then appends the previous element to highscores
        else:
            highscores.append(scores[i])        # else appends the current element to highscores
    
    highs = 0                               # counter varaible to count the number of times the score reaches a new high
    for i in range(1 , len(highscores)):        # iterates through highscores
        if highscores[i] > highscores[i-1]:     # checks if the current highscore is greater than the previous
            highs += 1                      # if true then in increases the counter variable by 1

    # For low scores
    lowscores = [scores[0]]         # list to score all the lowest scores
    for i in range(1 , len(scores)):            # iterates through the second element of scores till the last
        if lowscores[i-1] < scores[i]:      # checks if the previous element is smaller than the current element
            lowscores.append(lowscores[i-1])    # if true then appends the previous element to lowscores
        else:
            lowscores.append(scores[i])     # else appends the current element to lowscores
    
    lows = 0                                # counter varaible to count the number of times the score reaches a new low
    for i in range(1 , len(lowscores)):  # iterates through lowscores
        if lowscores[i] < lowscores[i-1]:       # checks if the current lowscore is greater than the previous
            lows += 1                   # if true then in increases the counter variable by 1

    return [highs , lows]           # retruns the 2 values of the counters

if __name__ == '__main__':
    n = int(input("Enter the number of games Maria played : "))
    scores = list(map(int , input("Enter her scores : ").rstrip().split()))

    result = breakingRecords(scores)
    print(' '.join(map(str , result)))