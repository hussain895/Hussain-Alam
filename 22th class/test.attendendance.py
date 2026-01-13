name = input("Enter Your Name = ")
print("\n")
english = int(input("Enter The Marks Of English = 100/"))
math = int(input("Enter The Marks Of Math = 100/"))
phy = int(input("Enter The Marks Of Physics = 100/"))
com = int(input("Enter The Marks Of Computer = 100/"))
chem = int(input("Enter The Marks Of Chemistry = 100/"))
print('\n')

attendance = input("Attendance Of The Student = ")
print("\n")

total_marks = english+math+phy+com+chem
print(f"Total Marks = 500/{total_marks}") 
print("\n")

marks=int(total_marks)
per = (marks/500)*100
print(f"Percentage = {per}")
print('\n')

per = str(per)
if per >= "85":
    print("Grade A")
elif per < "84" and per > "70":
    print("Grade B")
else:
    print("Fail")

print("\n")

if per > "85" and attendance > "80":
    print("Pass")
else:
    print("Fail")


list["Hussain": "Pass" , "ALi" : "Fail" , "Baqar" : "Pass"]



print(list.sort)



