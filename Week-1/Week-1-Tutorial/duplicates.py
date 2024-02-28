def duplicates(array):
    n = len(array)
    seen = []
    for i in range(0, n):
        if array[i] in seen:
            return True
        seen.append(array[i])
    return False


ISDUP = [1, 2, 3, 4, 5, 4]
NOTDUP = [3, 34, 1, 2, 33]
DUPYES = [2, 2]
print(duplicates(ISDUP))
print(duplicates(NOTDUP))
print(duplicates(DUPYES))


