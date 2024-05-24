#exercise 1
def count_a_number(numbers, number):
    counter = 0
    for i in numbers:
        if i == number:
            counter = counter + 1
    return counter
print(count_a_number([1, 2, 3, 3, 4, 5], 3))

#exercise 2
def play_with_lists(numbers, number):
    temp = numbers.copy()
    print(numbers[::-1])
    if number != 1:
        number = 1
        print(number)
    else:
        print(number)
    temp.sort(reverse=True)
    #for some reason the sorted function did not "reverse" my list
    print(temp)

play_with_lists([1,2,3,4,5], 2)

#exercise 3
def compare_lists(list1, list2):
    same_list = []
    for i in list1:
        if i in list2:
            same_list.append(i)
    return same_list
print(compare_lists([1,2,3,4,5],[2,3,4]))

#exercise 4
def remove_duplicates(items):
    print(list(set(items)))
remove_duplicates([1,1,2,3,4,4])

def remove_duplicates_my_way(items):
    duplicates_list = []
    for i in items:
        if i not in duplicates_list:
            duplicates_list.append(i)
    return duplicates_list
print(remove_duplicates_my_way([1,1,2,3,4,4]))

#exercise 5
def describe_computer(computer):
    ctype = computer.get('Type', 'type unknown')
    brand = computer.get('Brand', 'brand unknown')
    price = computer.get('Price', 'price unknown')
    print(f"You have a {ctype} from {brand} that costs {price}€.")
    computer['OS'] = 'Linux'
    print(computer)
my_computer = {'Type': 'Notebook', 'Brand': 'Dell', 'Price': 2000}
describe_computer(my_computer)