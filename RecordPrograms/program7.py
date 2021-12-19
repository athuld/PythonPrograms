def pattern1():
    print()
    for i in range(0, 4):
        for _ in range(0, i + 1):
            print("* ", end="")
        print("\r")


def pattern2():
    print()
    sp = 2 * 6 - 2

    for i in range(0, 6):
        for _ in range(0, sp):
            print(end=" ")
        sp -= 2
        for _ in range(0, i + 1):
            print("* ", end="")
        print("\r")


def pattern3():
    print()
    sp = 6 - 1

    for i in range(0, 6):
        for _ in range(0, sp):
            print(end=" ")
        sp -= 1
        for _ in range(0, i + 1):
            print("* ", end="")
        print("\r")


def pattern4():
    print()
    num = 1
    for i in range(0, 7):
        for _ in range(0, i + 1):
            print(num, end=" ")
            num += 1
        print("\r")


pattern1()
pattern2()
pattern3()
pattern4()
