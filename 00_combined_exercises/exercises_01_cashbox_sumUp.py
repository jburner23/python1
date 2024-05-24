"""
while True:
    to_pay = input("To pay:")
    to_pay = int(to_pay)
    #to_pay = int(input("To pay: "))
    if to_pay <= 0:
        print("Negative input is invalid")
        continue

    amount_received = int(input("Amount received: "))
    if amount_received <= 0:
        print("Negative input is invalid")
        continue

    if amount_received < to_pay:
        print("You did not pay enough!")
        continue

    #if amount_received >= to_pay:
        #print("Your change is: "+str(amount_received-to_pay))
    #print("Your change is: ",amount_received-to_pay)
    print(f'Your change is: {amount_received-to_pay}')
"""
while True:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    if n1 < 0 or n2 < 0:
        print("n1 and n2 need to be > 0")
        continue
    #n2 = int(input("n2: "))
    #if n2 < 0:
    #    print("n2 needs to be > 0")
    #    continue
    if n2 <= n1:
        print("n2 needs to be > n1")
        continue
    for i in range(n1,n2+1):
        print(i,end=" ")
    print()