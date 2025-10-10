attendence_list=[]
while True:
   name = input("Enter The Students Name(or 'done' to stop) = ")
   if name.lower() == 'done':
       break
   
   
   attendence_list = name.split()
   
print(attendence_list)
attendence_list.sorted
