text = input("Enter the sentence: ")
digit = alpha = special = 0

for i in range(len(text)):
    if text[i].isdigit():
        digit += 1
    elif text[i].isalpha():
        alpha += 1
    else:
        special += 1

print("\nNo: of digits:", digit)
print("No: of alphabets:", alpha)
print("No: of special characters:", special)
