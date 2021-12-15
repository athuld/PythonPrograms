n = int(input("Enter a number: "))
rev = 0
temp = n
while temp != 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp //= 10

if rev == n:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
