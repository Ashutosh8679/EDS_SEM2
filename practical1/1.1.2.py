import math

x = int(input())
if x<10:
	print(x*x)
elif 9<x<100:
	y = math.sqrt(x)
	print(f"{y:.2f}")
elif 99<x<1000:
	print(f"{x**(1/3):.2f}")
else:
	print("Invalid")