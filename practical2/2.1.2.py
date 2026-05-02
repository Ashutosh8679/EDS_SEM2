# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

print("Original Dictionary:",student)
key=int(input())
val=input()
student[key]=val
print("After Insertion:",student)

key=int(input())
val=input()
student[key]=val
print("After Update:",student)

key=int(input())
if key in student: 
	del student[key]
print("After Deletion:",student)

print("Traversing Dictionary:")
for key,val in student.items():
	print(key,":",val)
