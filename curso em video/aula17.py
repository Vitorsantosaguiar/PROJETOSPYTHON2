num = (1, 2, 3, 4, 5)
num[2] = 10  # This will raise a TypeError because tuples are immutable
print(num)
# Output:
# TypeError: 'tuple' object does not support item assignment
# Tuples are immutable, meaning their elements cannot be changed after they are created.
# If you need a mutable sequence, consider using a list instead:
num = [1, 2, 3, 4, 5]
num[2] = 10  # This will work because lists are mutable
print(num)
# Output:
# [1, 2, 10, 4, 5]
num.append(6)  # Adding an element to the list
print(num)
num.sort()  # Sorting the list
num.sort(reverse=True)  # Sorting the list in descending order
print(num)