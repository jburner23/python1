def remove_duplicates_my_way(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

print(remove_duplicates_my_way((1,1,2,3,4,5,5,)))