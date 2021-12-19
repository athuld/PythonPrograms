n = int(input("Enter the quantity of product: "))

print()
if n < 50:
    print("Time to place new order")
elif n >= 50 and n < 100:
    print("Sufficient")
else:
    print("Improve sales and marketing")
