n = int(input())
marks = list(map(int, input().split()))
if any(mark<40 for mark in marks):
	print("Fail")
else:
	aggr= sum(marks) / n
	print(f"Aggregate Percentage: {aggr:.2f}")

	if aggr>75:
		print("Grade: Distinction")
	elif aggr>=60:
		print("Grade: First Division")
	elif aggr>=50:
		print("Grade: Second Division")
	elif aggr>=40:
		print("Grade: Third Division")