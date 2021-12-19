n = int(input("Enter a number: "))
rev = 0
sum = 0
temp = n
while temp != 0:
    rem = temp % 10
    rev = rev * 10 + rem
    sum += rem
    temp //= 10

print("\nReverse of ", n, "is", rev)
print("Sum of digits is", sum)
