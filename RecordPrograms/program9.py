def startsWithT(text):
    count = 0
    for word in text.split():
        if word.startswith("t"):
            count += 1
    print("\nNo: of words starting with 't' :", count)


def endsWithS(text):
    count = 0
    for word in text.split():
        if word.endswith("s"):
            count += 1
    print("No: of words ending with 's' :", count)


def sixLetterWords(text):
    count = 0
    for word in text.split():
        if len(word) == 6:
            count += 1
    print("No: of 6 letter words in the string:", count)


def countWords(text):
    words = text.split()
    count = len(words)
    print("No: of words in the string:", count)


text = input("Enter a string: ").lower()
startsWithT(text)
endsWithS(text)
sixLetterWords(text)
countWords(text)
