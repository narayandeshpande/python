#Q.1) Write a program which prints Fibonacci series of a number. 
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Input number
num = int(input("Enter a number: "))

# Print Fibonacci series up to the input number
print("Fibonacci series up to", num, ":")
print(fibonacci_series(num))
