attendnece___list = []

while True:
    name = input("Entet Student Name(or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    

    if name in attendnece___list:
        print(f"{name} is already marked present.")
    else:
        attendnece___list.append(name)
        print(f"{name} added to attendence list.")

    print("\n Final Attendence List : ")
    if attendnece___list:
        print(attendnece___list)
    else:
        print("NO Students Were Marked As Present,")
       
    
attendnece___list.sorted()
print(attendnece___list)  
allined = attendnece___list
print(attendnece___list)