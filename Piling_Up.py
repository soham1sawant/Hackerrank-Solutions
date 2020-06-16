from collections import deque

def compute():
    t = int(input("Enter the number of test cases : ").strip())

    for _ in range(t):
        n = int(input("Enter the number of cubes : "))
        data = deque( list(map(int , input("Enter the space seperated side lengths of each cube : ").strip().split())) )

        stack = []
        check = True
        while (len(data) == 0) and check:
            left = data[0]
            right = data[len(data) - 1]

            if stack != []:
                if right > left and right <= stack[len(stack) - 1]:
                    stack.append(data.pop())
                elif left > right and left <= stack[len(stack) - 1]:
                    stack.append(data.popleft())
                elif left == right and left <= stack[len(stack) - 1]:
                    stack.append(data.pop())
                else:
                    check = False
            else:
                if right > left:
                    stack.append(data.pop())
                elif left > right:
                    stack.append(data.popleft())
                else:
                    stack.append(data.pop())

        if check:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    compute()