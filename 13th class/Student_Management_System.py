list = []

def new_student( ):
    name = input("Enter The Students Name = ")
    roll_number = int(input("Enter The Roll Number = "))
    marks = int(input("Enter The Marks = "))
    grade = input("Enter The Grade = ")
    list.append({"name": name , "roll_Number" :roll_number , "marks" : marks , "grade": grade })
    print("Students Add Successfully")


def view_students():
    if not list:
        print("No student records found.\n")
    else:
        for s in list:
            print(f"Roll : {s['roll_Number']} | Name : {s['name']} | Marks : {s['marks']} | Grade : {s['grade']}")


def search_student():
    roll_number = int(input("Enter The Roll Number To Search : "))
    for s in list:
        if s['roll_Number'] == roll_number:
            print(f"Roll : {s['roll_Number']} | Name : {s['name']} | Marks : {s['marks']} | Grade : {s['grade']}")
            return
    print("Student Not Found")      


def update_student():
    roll_number = int(input("Enter The Roll Number To Update : "))
    for s in list:
        if s['roll_Number'] == roll_number:
            print(f"Current Details - Roll : {s['roll_Number']} | Name : {s['name']} | Marks : {s['marks']} | Grade : {s['grade']}")
            s['name'] = input("Enter New Name : ")
            s['marks'] = int(input("Enter New Marks : "))
            s['grade'] = input("Enter New Grade : ")
            print("Student Details Updated Successfully")
            return
    print("Student Not Found")


def delete_student():
    roll_number = int(input("Enter The Roll Number To Delete : "))
    for s in list:
        if s['roll_Number'] == roll_number:
            list.remove(s)
            print("Student Deleted Successfully")
            return
    print("Student Not Found")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Your Choice (1-6): ")

        if choice == '1':
            new_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid Choice. Please Try Again.")


main()

