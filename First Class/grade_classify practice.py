
def grade(socre: int) -> str:
    if socre >= 90:
        return "A"
    elif socre >= 80:
        return "B"
    elif socre >= 70:
        return "C"
    elif socre >= 60:
        return "D"
    elif socre >= 50:
        return "E"
    else:
        return "Fail"
n = int(input("Enter The Students Number : "))
result = []
for i in range (1 , n + 1 ):
    name = input("Name Of The Student : ")
    print(f"The Name Of The Student Is {name}")

    socre = int(input("Socre : "))
    print(f"The Socre Of The Student Is {socre}")
    result.append((name , socre , grade(socre)))
 
print(result)