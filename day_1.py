import re

left = []
right=[]
with open(r"C:\Users\biyec\Downloads\day_1.txt") as file:
    for line in file:
        left.append( line.split(r",")[0].strip("\n"))
        right.append(line.split(r",")[1].strip("\n"))

distance = 0
left.sort()
right.sort()
for i in range(0, len(left)):
    distance += abs(int(left[i])-int(right[i]))
print(distance)

similarity = 0
for i in range(0, len(left)):
    similarity += int(left[i]) * right.count(left[i])
    
print(similarity)