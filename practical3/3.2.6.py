import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
ind = []
for i in range(0, len(array1)):
	if array1[i] == search_value :
		ind.append(i)
	else:
		pass
print("[", end='')
print(*ind, end='')
print("]")
# Count occurrences in array1
count = 0 
for i in range(0,len(array1)):
	if array1[i] == count_value :
		count += 1
	else:
		pass
print(count)
# Broadcasting addition
array2 = np.copy(array1)
array2 = array2 + broadcast_value
print(array2)
# Sort the first array
print(np.sort(array1))