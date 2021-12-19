text = input("Enter a string: ")
i = int(input("Enter the position of character to remove: "))

for pos in range(len(text)):
    if pos == i:
        text = text.replace(text[i], "", 1)

print("\nNew String:")
print(text)
