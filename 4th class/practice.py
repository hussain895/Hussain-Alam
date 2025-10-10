print("Hello , World!")

# Print the traditional hello world


z = 15+2
print(z)

print(type(z))

n = int(input("Enter a Number : "))

print(float(n))

print(type(False))
print(int(False))
print(int(True))
print(bool(0))
print(bool(1))


n = 6/2
print(n)
print(type(n))

n = 6//2
print(n)
print(type(n))

print(type("hello" == "world"))



n = "1001"
print(type(n))
print(int(n))



x = 43 + 60 + 16 + 41
print(x)
y = x/60
print(y)




name = "Hussain ALam"
print(name[0])
print(len(name))
print(name[0:7])
print(name[::2])
print(name[0:7:2])
print(name.find("Hussain"))


a = input("Enter The Name : ")

state = a.upper() + " is a good student".upper()
print(state)
b = state.replace('good'.upper(),'bad').upper()
print(b)


import re
a = "The BodyGuard is the best "
b = r"the"

result = re.search(b , a)

if result:
    print("Match Found!")
else:
    print("Match Not Found!")