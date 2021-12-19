text = input("Enter a string:")
print("\nEven length words:")
for word in text.split():
    if len(word) % 2 == 0:
        print(word)
