found = False
l = input().split()
val = input()
for i in range(len(l)):
	if l[i]==val:
		print(i)
		found = True
		break
if found==False:
	print("Not found")