def compute():
    for _ in range(int(input("Enter the number of test cases : "))):
        try:
            num = float(input("Enter the number : "))
            if num == 0:
                print("False")
            else:
                print("True")
        except:
            print("False")

if __name__ == "__main__":
    compute()