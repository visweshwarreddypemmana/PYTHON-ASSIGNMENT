def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
number = int(input("Enter a number: "))
print("The factorial of",number,"is",factorial(number))