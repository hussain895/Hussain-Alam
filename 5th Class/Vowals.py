string = str(input("Enter Your Name : "))

vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        print(char)