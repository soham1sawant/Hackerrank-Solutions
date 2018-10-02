# string_formatting.py

def print_formatted(number):
    results = []

    for i in range(1 , number + 1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hexa = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal , octal , hexa , binary])

    width = len(results[-1][3])                             # largest binary number

    for i in results:
        print(*(rep.rjust(width) for rep in i))

if __name__ == '__main__':
    n = int(input("Enter the number : "))
    print_formatted(n)
