# drawing_book.py

def pageCount(n , p):
    print(min(p//2 , n//2 - p//2))

def main():
    print()
    print("Hackerrank : Drawing Book")
    print()

    n = int(input("Enter the number of pages in the book : "))
    p = int(input("Enter the page that Brie's teacher wants her to turn : "))

    pageCount(n , p)

main()
