def binary_search(list, item):
    low = 0
    high = len(list) - 1

    count = 0
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid, f'Попыток: {count}'
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        count += 1

    return None, f'Попыток: {count}'


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # log(2)9 = 3
print(binary_search(my_list, -1))
