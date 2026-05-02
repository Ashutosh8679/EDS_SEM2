import numpy as np

# write your code here...
r,c = map(int, input().split())

data = []
for i in range(r):
	data.extend(map(int,input().split()))

arr = np.array(data).reshape(r,c)

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)