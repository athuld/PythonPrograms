def checkPrime(n):
    flag = False

    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break

    if flag:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")


def checkAmstrong(n):
    sum = 0
    temp = n

    while temp > 0:
        rem = temp % 10
        sum += rem ** 3
        temp //= 10

    if n == sum:
        print(n, "is an amstrong number")
    else:
        print(n, "is not an amstrong number")


def checkPerfect(n):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i
    if n == sum:
        print(n, "is a perfect number")
    else:
        print(n, "is not a perfect number")


def checkFibonacci(n):
    f1 = 1
    f2 = 1
    f3 = 0

    if n == 0 or n == 1:
        print(n, "is a fibonacci number")

    while f3 < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    if f3 == n:
        print(n, "is a fibonacci number")
    else:
        print(n, "is not a fibonacci number")


n = int(input("Enter a number: "))
print("\n")

checkPrime(n)
checkAmstrong(n)
checkPerfect(n)
checkFibonacci(n)
