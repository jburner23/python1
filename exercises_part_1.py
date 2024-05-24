"""
#exercise 1
#def famous_quote(name, quote):
def famous_quote():
    name = "Socrates"
    quote = "All I know is that I know nothing."
    print(f'{name} once said, "{quote}"')
famous_quote()

#exercise 2
def number_eight():
    print(5+3)
    print(9-1)
    print(2*4)
    print(16//2)
    print(2**3)
number_eight()
#exercise 3
def name_age():
    name = input("Please enter name: ")
    age = input("Please enter age: ")
    print("Hello,",name+". You are",age,"years old.")
    print(f"Hello, {name}. You are {age} years old.")
    print("Hello, {fname}. You are {fage} years old.".format(fname=name, fage=age))
name_age()

#exercise 4
def swap_integers():
    x = int(input("Please enter x: "))
    y = int(input("Please enter y: "))
    print("x =",x)
    print("y =",y)
    print("After swap: ")
    temp = x
    x = y
    y = temp
    print("x =",x)
    print("y =",y)
swap_integers()

#exercise 5 alt
#def check_numbers(number1, number2):
#    number1 = int(input("Number 1: "))
#    number2 = int(input("Number 2: "))
#    if number1 % 6 == 0 or number2 % 6 == 0:
#        print("One number is divisible by 6")
#    else:
#        print("Error: Neither number is divisible by 6!")
#    if number1 % 10 == 0 and number2 % 10 == 0:
#        print("Both numbers are divisible by 10")
#    else:
#        print("Both numbers are not divisible by 10")
#number1=0
#number2=0
#check_numbers(number1, number2)

#exercise 5
def check_numbers(number1, number2):
    print("Number 1:", number1)
    print("Number 2:", number2)
    if number1 % 6 == 0 or number2 % 6 == 0:
        print("One number is divisible by 6")
        if number1 % 10 == 0 and number2 % 10 == 0:
            print("Both numbers are divisible by 10")
            return True
        else:
            print("Both numbers are not divisible by 10")
            return False
number1 = 6
number2 = 10
check_numbers(number1, number2)

#exercise 6 alt
#def sum_up(number1, number2):
#    number1 = int(input("Number 1: "))
#    number2 = int(input("Number 2: "))
#    if number2 > number1:
#        sum1 = sum(range(number1, number2 + 1))
#        print(sum1,type(sum1))
#    else:
#        print("The second number is not greater than the first!")
#number1=0
#number2=0
#sum_up(number1,number2)

#exercise 6
def sum_up(number1, number2):
    if number2 > number1:
        sum1 = sum(range(number1, number2 + 1))
        print(sum1)
    else:
        print("The second number is not greater than the first!")
sum_up(3,9)

#exercise 7
def sequence(number):
    if number >= 0 and number <= 9:
        for i in range(10):
            if i != number:
                print(i,end=' ')
    else:
        print("Error: number is not an integer between 0 and 9")
sequence(5)

#exercise 8
def check_string(text):

    if text.startswith("a") or text.endswith("a") or text.startswith("A") or text.endswith("A"):
        return True
    else:
        return False

text = "www"
text1 = "Aji"
text2 = "ay"
text3 = "Sa"
text4 = "werA"
print("\n")
print(check_string(text))
print(check_string(text1))
print(check_string(text2))
print(check_string(text3))
print(check_string(text4))
"""
#exercise 9
def triangle(rows):
    for i in range(1, rows+1):
        print("* "*i)

triangle(4)
