raw  = " Age: 21 yrs  ,  Height: 5.8ft   ,   Weight= 65kg "
clean = raw.replace(" ","").lower()

age = int(clean[clean.index("age:")+4 : clean.index("yrs")])
height = float(clean[clean.index("height:")+7 : clean.index("ft")])
weight = int(clean[clean.index("weight=")+7 : clean.index("kg")])

print("Age:", age," Height:", height, "Weight:", weight)

a = int(input("Enter The Temp In Celvin = "))
b = int(input("Enter The Humidity = "))

raws = f"Temp= {a}C , Humidity= {b}% "
cleans = raws.replace(" ","").lower()

temp = int(cleans[cleans.index("temp=")+5 : cleans.index("C")])
humidity = int(cleans[cleans.index("humidity=")+9 : cleans.index("%")])

print( temp , humidity)