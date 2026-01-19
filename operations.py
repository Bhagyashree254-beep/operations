import sys

def addition(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except IndexError:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter valid integers.")
        sys.exit(1)
        
    print("\n.....Result...\n") 
    print("sum", addition(a,b))
    print("sub", substraction(a,b))
    print("multi", multiplication(a,b))
    print("div", division(a,b))
    
    
   


