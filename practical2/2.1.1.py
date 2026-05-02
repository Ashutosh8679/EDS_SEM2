x = 0
l = []
while x!=4:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	x = int(input("Enter choice: "))
	if x==1:
		val = int(input("Integer: "))
		l.append(val)
		print("List after adding:", l)
	if x==2 and l!=[]:
		val = int(input("Integer: "))
		try: 
			l.remove(val)
			print("List after removing:", l)
		except ValueError:
			print("Element not found")
	elif x==2 and l==[]:
		print("List is empty")
	if x==3:
		if l==[]:
			print("List is empty")
		else:
			print(l)
	if x>4:
		print("Invalid choice")
	