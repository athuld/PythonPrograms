n = int(input("Enter the value for n: "))

sum = 0

for i in range(1, n + 1):
    sum += i * i

print("\nSum of squares of first", n, "natural numbers is: ", sum)
