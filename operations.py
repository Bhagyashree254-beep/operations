import sys

def operations(a, b):
    return a + b, a - b, a * b, a / b

if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except IndexError:
        a = int(input("Enter first num1: "))
        b = int(input("Enter second num2: "))
    except ValueError:
        print("Please enter valid integers.")
        sys.exit(1)

    print(operations(a, b))



