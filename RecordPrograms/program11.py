vowels = ["a", "e", "i", "o", "u"]

text = input("Enter a string: ").lower()

v_count = 0
c_count = 0

for char in text:
    if char in vowels:
        v_count += 1
    else:
        c_count += 1

print("\nNo: of vowels:", v_count)
print("No: of consonants:", c_count)
