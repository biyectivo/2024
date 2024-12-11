import re
import time
import numpy as np
 
t = time.time()
 
grid = []
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_10.txt") as file:
    for line in file:
        grid.append([int(x) if x!="." else -1 for x in line.strip()])
 
grid = np.array(grid)
rows, cols = grid.shape
peaks = set()
trailheads = np.where(grid == 0)
 
#print(grid)
#print(rows,cols)
#print(trailheads)

 
def valid(row, col):
    global rows, cols
    return row >= 0 and row < rows and col >= 0 and col < cols
 
def is_climbable(row,col):
    global grid, peaks
    if grid[row][col] == 9:
        if (row,col) not in peaks:
            peaks.add((row,col))
            return 1
        else:
            return 0
    else:
        cond = 0
        if valid(row, col+1) and grid[row, col+1] == grid[row, col] + 1:
            cond += is_climbable(row, col+1)
        if valid(row, col-1) and grid[row, col-1] == grid[row, col] + 1:
            cond += is_climbable(row, col-1)
        if valid(row+1, col) and grid[row+1, col] == grid[row, col] + 1:
            cond += is_climbable(row+1, col)
        if valid(row-1, col) and grid[row-1, col] == grid[row, col] + 1:
            cond += is_climbable(row-1, col)
       
        return cond
 
paths = []
def is_climbable_p2(row,col, path):
    global grid, peaks, paths
    if grid[row][col] == 9:
        paths.append(path)
        if (row,col) not in peaks:
            peaks.add((row,col))
            return 1
        else:
            return 0
    else:
        cond = 0
        if valid(row, col+1) and grid[row, col+1] == grid[row, col] + 1:
            cond += is_climbable_p2(row, col+1,path+">")
        if valid(row, col-1) and grid[row, col-1] == grid[row, col] + 1:
            cond += is_climbable_p2(row, col-1,path+"<")
        if valid(row+1, col) and grid[row+1, col] == grid[row, col] + 1:
            cond += is_climbable_p2(row+1, col,path+"v")
        if valid(row-1, col) and grid[row-1, col] == grid[row, col] + 1:
            cond += is_climbable_p2(row-1, col,path+"^")
       
        return cond
 
score = 0
score2 = 0
all_peaks = set()
for i in range(0, len(trailheads[0])):
    peaks = set()
    paths = []
    this_score = is_climbable_p2(trailheads[0][i], trailheads[1][i],"")
    this_score2 = len(paths)
    #print(f" {trailheads[0][i]},{ trailheads[1][i]}: {this_score} {this_score2}")
    score += this_score
    score2 += this_score2
# =============================================================================
#     score2 += this_score2
# =============================================================================
    all_peaks.union(peaks)
 
print(f"Total score: {score}")
print(f"Total score: {score2}")
#print(paths)
print(f"Total time: {time.time()-t} s")