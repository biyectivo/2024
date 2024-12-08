import re
import math
import numpy as np
import itertools as it
import time

t = time.time()

total = 0
grid = []
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_8.txt") as file:
    for line in file:
       grid.append([x for x in line.strip()])
grid = np.array(grid)
#print(grid)
rows,cols = grid.shape

antennas = {}
antinodes = np.zeros(shape=(rows,cols))

def valid(row,col):
    global rows, cols
    return row >= 0 and row < rows and col >= 0 and col < cols

for row in range(0,rows):
    for col in range(0,cols):
        if grid[row][col] != ".":
            if grid[row][col] in antennas.keys():
                antennas[grid[row][col]].append((row,col))
            else:
                antennas[grid[row][col]] = []
                antennas[grid[row][col]].append((row,col))

#part 1
def resonate_p1(antenna, start_row, start_col, delta_row, delta_col):
    global grid, antinodes
    row = start_row + delta_row
    col = start_col + delta_col
    
    if valid(row,col) and grid[row][col] != antenna:
        antinodes[row][col] = 1
        
for antenna in antennas.keys():
    for i in range(0,len(antennas[antenna])):
        for j in range(i+1, len(antennas[antenna])):
            #print(f"antenna {antennas[antenna][i]} vs {antennas[antenna][j]}")
            dist_v = antennas[antenna][i][0] - antennas[antenna][j][0]
            dist_h = antennas[antenna][i][1] - antennas[antenna][j][1]
            
            # try all four - only 2 at most will be valid but oh well
            resonate_p1(antenna, antennas[antenna][i][0], antennas[antenna][i][1], -dist_v, -dist_h)
            resonate_p1(antenna, antennas[antenna][i][0], antennas[antenna][i][1], dist_v, dist_h)
            resonate_p1(antenna, antennas[antenna][j][0], antennas[antenna][j][1], -dist_v, -dist_h)
            resonate_p1(antenna, antennas[antenna][j][0], antennas[antenna][j][1], dist_v, dist_h)
            
print(sum(sum(antinodes)))

#part 2
def resonate_p2(antenna, start_row, start_col, delta_row, delta_col):
    global grid, antinodes
    row = start_row + delta_row
    col = start_col + delta_col
    while valid(row,col):
        antinodes[row][col] = 1
        row += delta_row
        col += delta_col

for antenna in antennas.keys():
    for i in range(0,len(antennas[antenna])):
        for j in range(i+1, len(antennas[antenna])):
            dist_v = antennas[antenna][i][0] - antennas[antenna][j][0]
            dist_h = antennas[antenna][i][1] - antennas[antenna][j][1]
            
            # try all four - only 2 at most will be valid but oh well
            resonate_p2(antenna, antennas[antenna][i][0], antennas[antenna][i][1], -dist_v, -dist_h)
            resonate_p2(antenna, antennas[antenna][i][0], antennas[antenna][i][1], dist_v, dist_h)
            resonate_p2(antenna, antennas[antenna][j][0], antennas[antenna][j][1], -dist_v, -dist_h)
            resonate_p2(antenna, antennas[antenna][j][0], antennas[antenna][j][1], dist_v, dist_h)


print(antinodes)
print(sum(sum(antinodes)))
print(f"Time: {time.time()-t} seconds")