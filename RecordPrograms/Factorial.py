def factWithRecursion(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factWithRecursion(n - 1)


def factWithoutRecursion(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


n = int(input("Enter a number: "))
print("Factorial of", n, "with recursion:", factWithRecursion(n))
print("Factorial of", n, "without recursion:", factWithoutRecursion(n))
