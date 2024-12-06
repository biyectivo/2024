import re
import math
import numpy as np


lab_array = []
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_6.txt") as file:
    for line in file:
        lab_array.append([x for x in line.strip()])

lab = np.array(lab_array)
print(lab)
rows,cols = lab.shape
print(rows,cols)

original_lab = lab.copy()

current_dir = 90

def check_valid(row, col):
    global rows, cols
    return row >= 0 and row < rows and col >= 0 and col < cols
    
def new_pos(row, col, direction):        
    if direction == 0:
        newrow = row
        newcol = col+1
    elif direction == 90:
        newrow = row-1
        newcol = col
    elif direction == 180:
        newrow = row
        newcol = col-1
    elif direction == 270:
        newrow = row+1
        newcol = col
    
    return [newrow, newcol]
    
    
def check_obstacle(row, col, direction):
    global lab
    
    if direction == 0:
        newrow = row
        newcol = col+1
    elif direction == 90:
        newrow = row-1
        newcol = col
    elif direction == 180:
        newrow = row
        newcol = col-1
    elif direction == 270:
        newrow = row+1
        newcol = col
    
    if not check_valid(newrow, newcol):
        return False
    else:
        return lab[newrow][newcol] == "#"

def check_exit(row, col, direction):
    global lab
    
    if direction == 0:
        newrow = row
        newcol = col+1
    elif direction == 90:
        newrow = row-1
        newcol = col
    elif direction == 180:
        newrow = row
        newcol = col-1
    elif direction == 270:
        newrow = row+1
        newcol = col
        
    return not check_valid(newrow, newcol)

def rotate_right():
    global current_dir
    if current_dir == 0:
        new_dir = 270
    elif current_dir == 90:
        new_dir = 0
    elif current_dir == 180:
        new_dir = 90
    elif current_dir == 270:
        new_dir = 180
    return new_dir

 
# =============================================================================
# [current_row,current_col] = np.where(lab == "^")
# current_row = current_row[0]
# current_col = current_col[0]
# 
# n = 1
# lab[current_row, current_col] = "X"
# 
# while not check_exit(current_row, current_col, current_dir):
#     #print(f"At {current_row},{current_col}")
#     while check_obstacle(current_row, current_col, current_dir):
#         current_dir = rotate_right()
#     [current_row, current_col] = new_pos(current_row, current_col, current_dir)
#     #n+=1
#     lab[current_row, current_col] = "X"  
#     
# 
#     
# print(lab)
# print(np.count_nonzero(lab=="X"))
# =============================================================================



# Part 2

n = 1


possible_obstacles = []

start_row,start_col = np.where(lab == "^")
start_row=start_row[0]
start_col=start_col[0]
print(start_row, start_col)
for row in range(0,rows):
    for col in range(0,cols):
        lab = np.array(lab_array)
        
        if lab[row][col] == "#" or lab[row][col] == "^":
            continue
        
        lab[row][col] = "#"
        
        #[current_row,current_col] = np.where(lab == "^")
        #current_row = current_row[0]
        #current_col = current_col[0]
        current_row = start_row
        current_col = start_col
        current_dir = 90
        
        loop = False
        #visited=[]
        visited = set()
        
        #print(f"For {row},{col}")
            
        while not check_exit(current_row, current_col, current_dir) and not loop:
            #print(current_row, current_col)
            while check_obstacle(current_row, current_col, current_dir):                
                current_dir = rotate_right()
            [current_row, current_col] = new_pos(current_row, current_col, current_dir)
            
            #if lab[current_row][current_col] != "X":
            #    lab[current_row][current_col] = "X"                
            
            #if [current_row, current_col, current_dir] not in visited:
            if (current_row, current_col, current_dir) not in visited:
                #visited.append([current_row, current_col, current_dir])
                #visited.append((current_row, current_col, current_dir))
                visited.add((current_row, current_col, current_dir))
            else:
                loop = True
        
        if loop:
            possible_obstacles.append([row, col])
            #print("loops")
            #print(lab)
        #else:
            #print("didnt loop")
                  
        #print("~")
    
print(len(possible_obstacles))

