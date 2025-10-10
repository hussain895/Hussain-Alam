d = "ABCDEFG"

print(d[0:3])
print(d[::2])

print(r"\\")

g = "My Name Is Hussain Alam"

b = g.find("My")
print(b)

age = 18

if age > 19:
    print("You Can Access")
else:
    print("You Cannot Access")    


if age > 19:
    print("You Can Enter")
elif age == 18:
    print("Go See Pink Floyd") 
else: 
    print("Go See Meat Loaf")

print("Move On")  


album = int(input("album-year = "))

if(album > 1979) and (album < 1990):
    print('Album year was in between 1980 and 1989')

print("")
print("Do Stuff ..")


player_name = "Lionel Messi"
sport = "Soccer"
achievements = 7

if achievements > 10:
    print(f"{player_name} play {sport} and has {achievements} achievements")
else:
    print(f"{player_name} does not have more than 10 achievements. ")



player_name = "Roger Federer"
sport = "Tennis"
achievements = 20

if (achievements == 20 and sport == "Tennis"):
    print(f"{player_name} play {sport} and has {achievements} achievements")
else:
    print(f"{player_name} does not have 20 achievements. ") 




dates = [1982 , 1980 , 1973]
n = len(dates)

for i in range(n):
    print(dates[i]) 


i = 0
year = dates[0]
while (year != 1973):
    print(year)
    i = i + 1
    year = dates[i] 


for i in range (-5 , 6):
    print(i)


Genres = ['rock' , 'R&B' , 'soundtrack' , 'Soul' , 'Pop']
n = len(Genres)

for i in range(n):
    print(Genres[i]) 


Genres = ['rock' , 'R&B' , 'soundtrack' , 'Soul' , 'Pop']

for i in Genres:
    print(i) 


PlaylistRatings = [10 , 9.5 , 10 , 8 ,7.5 , 5 , 10 ,10 ]
i=0
score = PlaylistRatings[0]
while (score > 6):
     print(PlaylistRatings[i])
     i = i+1


squares = ['orange' , 'orange' , 'purple' , 'blue' , 'orange']
new_squares =[]
i = 0

while(i<len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
    print(new_squares)