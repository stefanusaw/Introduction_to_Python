def menu():
    n = int(input("Welcome to the Recursive Artistry Program! Choose an option:\n1. Calculate Factorial\n2. Find Fibonacci\n3. Exit\n"))
    if n == 1:
        callFactorial()
    elif n == 2:
        callFibonacci()
    else:
        exit()
        
def callFactorial():
    n = int(input("Enter a number to find its factorial: "))
    def factorial(n):
        if n == 1:
            return n
        return n * factorial(n-1)
    fac = factorial(n)
    print(f"The factorial of {n} is {fac}.")

def callFibonacci():
    n = int(input("Enter the position of the Fibonacci number: "))    
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    fib = fibonacci(n)
    print(f"The {n}th Fibonacci number is {fib}.")
    

menu()