# designer_PDF_viewer.py

def designerPdfViewer(h , word):

    heights = []            # list to store the heights of the letters of the word
    for letter in word:         # iterates through word
        heights.append( h[ord(letter) - 97] )  # adds to the list the height of the letter by finding its position

    return max(heights) * len(word)     # return the product of the maximum height and the length of the string word
    

if __name__ == '__main__':
    h = list(map(int, input("Enter the height of each letter : ").rstrip().split()))
    word = input("Enter the word : ")

    result = designerPdfViewer(h, word)
    print(result)