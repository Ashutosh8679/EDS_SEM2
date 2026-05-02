import numpy as np

def array_operations(A, B):

	# Convert A and B to NumPy arrays
	X = np.array(A)
	Y = np.array(B)

	# Arithmetic Operations
	sum_result = X + Y
	diff_result = X - Y
	prod_result = X * Y

	# Statistical Operations
	mean_A = np.mean(X)
	median_A = np.median(X)
	std_dev_A = np.std(X)

	# Bitwise Operations
	and_result = X & Y
	or_result =  X | Y
	xor_result = X ^ Y

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
B = list(map(int, input().split()))  # Elements of array B
array_operations(A, B)
