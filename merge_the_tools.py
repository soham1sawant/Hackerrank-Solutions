# merge_the_tools.py

def merge_the_tools(str , k):
    str = str.upper()

    for i in range(0 , len(str) , k):
        substr = ''
        for i in str[i:i+k]:
            if i not in substr:
                substr += i
        print(substr)
        


if __name__ == '__main__':
    print()
    print("Hackerrank : Merge The Tools")
    print()

    string , k = input('Enter string : ') , int(input('Enter k : '))
    merge_the_tools(string , k)
