text = input("Enter a sentence: ").lower()
D = dict()
for word in text.split():
    if word in D:
        D[word] += 1
    else:
        D[word] = 1

currHigh = 0
currKey = ""
for key in D.keys():
    if D[key] > currHigh:
        currHigh = D[key]
        currKey = key

print("\nMost repeated word is:", currKey, "\nCount:", D[currKey])
