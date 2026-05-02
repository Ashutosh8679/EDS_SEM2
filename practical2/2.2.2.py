x = input().split()
h = []
for item in x:
	n = int(item)
	h.append(n)

cap = 0

for i in range(len(h)):
	if cap<h[i]:
		cap=h[i]
	else:
		continue
print(cap)
