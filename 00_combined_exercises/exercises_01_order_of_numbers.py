while True:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))

    if n1 < n2 and n2 < n3:
        print("numbers are ascending")
    if n3 < n2 and n2 < n1:
        print("numbers are descending")
    if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
        print("no specific order, but all even")
    if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
        print("no specific order, but all odd")
    else:
        print("no specific order")