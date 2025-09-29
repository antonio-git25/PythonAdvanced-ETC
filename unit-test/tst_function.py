def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1

#print(linear_search(['b','d','e'],'a'))


def is_sorted_ascending(lst: list) -> bool:
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))


def is_sorted_descending(lst: list) -> bool:
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


result = is_sorted_ascending([1,5,3,2,8])
print(result)
result = is_sorted_ascending([1,2,3,8])
print(result)