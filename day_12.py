import re
import math
import numpy as np
import itertools as it
import time
from functools import cmp_to_key

grid = []
total = 0
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_12_sample_3.txt") as file:
    for line in file:
        grid.append([x for x in line.strip()])

grid = np.array(grid)
rows, cols = grid.shape

visited = np.zeros([rows,cols])

print(grid)


t = time.time()

regions = []

def valid(row, col):
    global rows, cols
    return row >= 0 and row < rows and col >= 0 and col < cols

def create_region(row,col,region):
    global grid, visited
    visited[row][col] = 1
    neighbors = 0
    if valid(row+1, col) and grid[row+1][col] == grid[row][col] and visited[row+1][col] == 0:
        neighbors += 1
        region.add((row+1,col))
        create_region(row+1,col, region)
    if valid(row-1, col) and grid[row-1][col] == grid[row][col] and visited[row-1][col] == 0:
        neighbors += 1
        region.add((row-1,col))
        create_region(row-1,col, region)
    if valid(row, col+1) and grid[row][col+1] == grid[row][col] and visited[row][col+1] == 0:
        neighbors += 1
        region.add((row,col+1))
        create_region(row,col+1, region)
    if valid(row, col-1) and grid[row][col-1] == grid[row][col] and visited[row][col-1] == 0:
        neighbors += 1
        region.add((row,col-1))
        create_region(row,col-1, region)
    
    if neighbors == 0:
        regions.append(region)
        return
    
for row in range(0,rows):
    for col in range(0, cols):
        region = set()
        found = False
        for r in regions:
            if (row,col) in r:
                found = True
                
        if not found:
            region.add((row,col))
            create_region(row, col, region)


final_regions = set()
for r in regions:
    final_regions.add(frozenset(r))

    
def num_neighbors(row,col):
    global grid
    neighbors = 0
    if valid(row+1, col) and grid[row+1][col] == grid[row][col]:
        neighbors += 1
    if valid(row-1, col) and grid[row-1][col] == grid[row][col]:
        neighbors += 1
    if valid(row, col+1) and grid[row][col+1] == grid[row][col]:
        neighbors += 1
    if valid(row, col-1) and grid[row][col-1] == grid[row][col]:
        neighbors += 1
    return neighbors

total = 0
for r in final_regions:
    area = len(r)
    perimeter = len(r) * 4
    for coord in r:
        #print(" ", coord, num_neighbors(coord[0], coord[1]))
        perimeter -= num_neighbors(coord[0], coord[1])
    #print(r, area, perimeter)

    total += area * perimeter
    
print(total)

def compare(item1, item2):
    r1 = item1[0]**2 + item1[1]**2
    r2 = item2[0]**2 + item2[1]**2
   
    func = r1 - r2
    if func < 0:
        return -1
    elif func > 0:
        return 1
    else:
        return 0

# part 2
total = 0
for r in final_regions:
    area = len(r)
    l = [x for x in r]
    l = sorted(l, key = cmp_to_key(compare))
    
    sides = 4
    top_left = (min([x[0] for x in l]), min([x[1] for x in l]))
    bottom_right = (max([x[0] for x in l]), max([x[1] for x in l]))
    letter = grid[l[0][0]][l[0][1]]
    
    for row in range(top_left[0], bottom_right[0]+1):
        for col in range(top_left[1], bottom_right[1]+1):
            if grid[row][col] != letter:
                n = 0
                n += 1 if valid(row-1,col) and grid[row-1][col]==letter else 0
                n += 1 if valid(row+1,col) and grid[row+1][col]==letter else 0
                n += 1 if valid(row,col-1) and grid[row][col-1]==letter else 0
                n += 1 if valid(row,col+1) and grid[row][col+1]==letter else 0
                sides += 4 if n == 4 else 2
    
    #print(letter, area, sides)
    total += area * sides
    
    #print(r,letter,sides," ", top_left,bottom_right)

print(total)
print(f"Time: {time.time()-t} s")