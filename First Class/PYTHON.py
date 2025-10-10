def calculate_grade():
  #step 1 : Input the number of subjects
 n = int(input("Enter number of subjects:"))
 #step 2 : Input marks for each subjects
 total_marks = 0
 maximum_marks = 100 # Assuming each subject is out of 100 marks
 for i in range(n):
  marks = int(input(f"Enter marks for subject { i + 1 }:"))
 total_marks += marks
 # step 3 : calculate percentage
 percentage = ( total_marks / (n * maximum_marks))*100
 # step 4 : Determine grade
 if percentage >= 90:
  grade = "A"
 elif percentage >= 80:
  grade = "B"
 elif percentage >=70:
  grade = "C"
 else:
   grade = "F"

 # step 5 : OUTPUT THE RESULTS
   print(f"Total Marks: {total_marks}/{n * maximum_marks}")
   print(f"Percentage: {percentage}")
   print(f"Grade:{grade}")

# call the function
calculate_grade()  
