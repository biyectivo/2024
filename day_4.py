import re
import math
import numpy as np

matrix = []
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_4.txt") as file:
    for line in file:
        matrix.append([n for n in line.strip()])
    

word_search = np.matrix(matrix)

[rows,cols] = word_search.shape

#direction: 0 = up, 1 = up-right, ...
def searchable(row, col, direction):
    if direction == 0:
        return row >= 3
    elif direction == 1:
        return row >= 3 and col <= cols - 4
    elif direction == 2:
        return col <= cols - 4
    elif direction == 3:
        return row <= rows - 4 and col <= cols - 4
    elif direction == 4:
        return row <= rows - 4
    elif direction == 5:
        return row <= rows - 4 and col >= 3
    elif direction == 6:
        return col >= 3
    elif direction == 7:
        return row >= 3 and col >= 3

def search_string(row, col, direction):
    global word_search
    if direction == 0:
       return word_search[row, col]+word_search[row-1, col]+word_search[row-2, col]+word_search[row-3, col]
    elif direction == 1:
        return word_search[row, col]+word_search[row-1, col+1]+word_search[row-2, col+2]+word_search[row-3, col+3]
    elif direction == 2:
        return word_search[row, col]+word_search[row, col+1]+word_search[row, col+2]+word_search[row, col+3]
    elif direction == 3:
        return word_search[row, col]+word_search[row+1, col+1]+word_search[row+2, col+2]+word_search[row+3, col+3]
    elif direction == 4:
        return word_search[row, col]+word_search[row+1, col]+word_search[row+2, col]+word_search[row+3, col]
    elif direction == 5:
        return word_search[row, col]+word_search[row+1, col-1]+word_search[row+2, col-2]+word_search[row+3, col-3]
    elif direction == 6:
        return word_search[row, col]+word_search[row, col-1]+word_search[row, col-2]+word_search[row, col-3]
    elif direction == 7:
        return word_search[row, col]+word_search[row-1, col-1]+word_search[row-2, col-2]+word_search[row-3, col-3]

def searchable_2(row, col, direction):
    if direction == 0:
        return row >= 1
    elif direction == 1:
        return row >= 1 and col <= cols - 2
    elif direction == 2:
        return col <= cols - 2
    elif direction == 3:
        return row <= rows - 2 and col <= cols - 2
    elif direction == 4:
        return row <= rows - 2
    elif direction == 5:
        return row <= rows - 2 and col >= 1
    elif direction == 6:
        return col >= 1
    elif direction == 7:
        return row >= 1 and col >= 1
    
# 15 is /, 37 is \
def search_string_2(row, col, direction):
    global word_search
    if direction == 15:
       return word_search[row-1, col+1]+word_search[row, col]+word_search[row+1, col-1]
    elif direction == 37:
        return word_search[row-1, col-1]+word_search[row, col]+word_search[row+1, col+1]
    
xmas = 0

for direction in range(0,9):
    for r in range(0,rows):
        for c in range(0,cols):
            if searchable(r,c,direction):
                if search_string(r,c,direction) == "XMAS":
                    xmas += 1

print(xmas)

xmas = 0

#part 2

for r in range(0,rows):
    for c in range(0,cols):
        if searchable_2(r,c,1) and searchable_2(r,c,3) and searchable_2(r,c,5) and searchable_2(r,c,7) and word_search[r,c] == "A":
            #print(r,c,search_string_2(r,c,15),search_string_2(r,c,37))
            if (search_string_2(r,c,15) in ["MAS","SAM"] and search_string_2(r,c,37) in ["MAS","SAM"]):
                xmas += 1

print(xmas)