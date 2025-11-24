students_list = []

def Add_New_Student():
    name = str(input("Enter The Students Name = "))
    roll_number = int(input("Enter The Roll Number = "))
    marks = int(input("Enter The Marks = "))
    grade = input("Enter The grade")
    
    students_list.append({"Name" : name , "Roll No" : roll_number , "Marks" : marks , "Grade" : grade})
    print("Students Add Successfully.\n")

def view_student():
    if not students_list:
        print("Student Record Is Not Found.\n ")
    else:
       for s in students_list:
         print(f"Roll : {s['roll_Number']} | Name : {s['name']} | Marks : {s['marks']} | Grade : {s['grade']}")


def search_student():
    roll_number = int(input("Enter The Roll Number To Search : "))
    for s in list:
        if s['roll_Number'] == roll_number:
            print(f"Roll : {s['roll_Number']} | Name : {s['name']} | Marks : {s['marks']} | Grade : {s['grade']}")
            return
    print("Student Not Found")    
   
def updated_student():
    roll_number = int(input("Enter The Roll Number To Update : "))
    for s in students_list:
        if s['roll_Number'] == roll_number:
            print(f"Current Details - Roll : {s['roll_Number']} | Name : {s['name']} | Marks : {s['marks']} | Grade : {s['grade']}")
            s['name'] = input("Enter New Name : ")
            s['marks'] = int(input("Enter New Marks : "))
            s['grade'] = input("Enter New Grade : ")
            print("Student Details Updated Successfully")
            return
    print("Student Not Found")

def delete_student():
    Roll_Number = int(input("Enter The Roll Number To Delete = "))
    for s in students_list:
        if s['roll number'] == Roll_Number:
            students_list.remove(s)
            print("Student Deleted Successfully")
            return
    print("Student Not Found")

def main():
    while True:
        print("\n Student Manegement System")
        print("1. Add_New_Student ")
        print("2. View_Student ")
        print("3. Search_Student ")
        print("4. Updated_Student ")
        print("5. Delete_Student")
        choice = input("Enter Your Choice (1-6): ")

        if choice == "1":
            print(Add_New_Student)
        elif choice == "2":
            print(view_student)
        elif choice == "3":
            print(search_student)
        elif choice == "4":
            print(updated_student)
        elif choice == "5":
            print(delete_student)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid Choice. Please Try Again.")

main()
        








