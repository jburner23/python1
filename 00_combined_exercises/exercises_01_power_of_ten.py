while True:
    number = int(input("Enter a max 3 digit number:"))
    if number < 0:
        print("number cannot be negative")
    if number > 999:
        print("number has more than 3 digits")
    else:
        two_digits = number % 100
        one_digit = number % 10
        hundred = number // 100
        ten = two_digits // 10
        print(f"{number} = {hundred} * 100 + {ten} * 10 + {one_digit} * 1")
        #print(two_digits)
        #print(one_digit)
        #print(hundred)
        #print(ten)