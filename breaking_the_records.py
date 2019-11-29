# breaking_the_records.py

def breakingRecords(scores):
    print(scores)

    highscores = [scores[0]]
    for i in range(1 , len(scores)):
        if highscores[i-1] > scores[i]:
            highscores.append(highscores[i-1])
        else:
            highscores.append(scores[i])

    print(highscores)


if __name__ == '__main__':
    n = int(input("Enter the number of games Maria played : "))
    scores = list(map(int , input("Enter her scores : ").rstrip().split()))

    print(breakingRecords(scores))