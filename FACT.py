A = int(input("Enter a number: "))

if A < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, A + 1):
        factorial *= i

    print(f"The factorial of {A} is {factorial}")