text = input("Enter a sentence: ").lower()
D = dict()
for word in text.split():
    if word in D:
        D[word] += 1
    else:
        D[word] = 1
print("\nWords counts:")
for key in D.keys():
    print(key, ":", D[key])
