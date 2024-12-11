
import re
import math
import numpy as np
import itertools as it
import time

grid = []
total = 0
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_9.txt") as file:
    line = file.readlines()[0]


t = time.time()

disk_map = []
file_processing = True
file_id = 0
for i in range(0,len(line)):
    if file_processing:
        #disk_map += int(line[i])*str(file_id // 2)
        disk_map.extend([file_id//2 for i in range(0,int(line[i]))])
    else:
        #disk_map += int(line[i])*"."
        disk_map.extend(["." for i in range(0,int(line[i]))])
    file_processing = not file_processing
    file_id+=1 

disk_map = np.array(disk_map)
original_map = disk_map.copy()
total_to_rearrange = np.count_nonzero(disk_map != ".")

def check_finished(gap):
    global disk_map, total_to_rearrange
    i = find_first_gap(gap)
    return i == total_to_rearrange

def find_first_gap(start):
    global disk_map, total_to_rearrange
    i=start
    while disk_map[i] != "." and i < len(disk_map):
        i+=1
    return i

def find_last_digit(start):
    global disk_map, total_to_rearrange
    i=start
    while disk_map[i] == "." and i > -len(disk_map):
        i-=1
    return i

gap = 0
last = -1
while not check_finished(gap):
    gap = find_first_gap(gap)
    last = find_last_digit(last)
    disk_map[gap] = disk_map[last]
    disk_map[last] = "."



checksum = 0

for i in range(0,total_to_rearrange):
    checksum += i * int(disk_map[i])

print(checksum)

#part 2

def find_available_space(pos):
    global disk_map
    i=pos
    while disk_map[i] == ".":
        i+=1
    return i-pos

disk_map = original_map.copy()

file_id = int(max(disk_map))

#print(disk_map)
sp = np.where(disk_map==".")

gap_positions = {}
key = ""
for i in range(0, len(sp[0])):
    if i==0:
        key = str(sp[0][i])
        gap_positions[key] = 1
    elif sp[0][i]-sp[0][i-1] == 1:
        gap_positions[key] += 1
    else:
        key = str(sp[0][i])
        gap_positions[key] = 1

# =============================================================================
# while(file_id > 0):
#     if file_id % 100 == 0:
#         print(file_id)
#     gap = 0
#     pos = np.where(disk_map == str(file_id))    
#     gap = find_first_gap(gap)
#     found = False
#     while gap < pos[0][0] and not found:
#         space = find_available_space(gap)
#         num = len(pos[0])
#         if num <= space:
#             for i in range(0,num):
#                 disk_map[gap+i] = file_id
#                 disk_map[pos[0][0]+i] = "."
#             found = True
#         
#         if not found:
#             gap = find_first_gap(gap+num)
#     
#     #print(file_id, disk_map)
#     file_id -= 1
# 
# =============================================================================

# =============================================================================
# keys = list(gap_positions.keys())
# =============================================================================
#print(gap_positions)
def dprint(*_str):
    global NUM_DEBUG_MIN, NUM_DEBUG_MAX, file_id
    if file_id >= NUM_DEBUG_MIN and file_id <= NUM_DEBUG_MAX:
        _str_final = ",".join([str(x) for x in _str])
        print(_str_final)


NUM_DEBUG_MIN = 9990
NUM_DEBUG_MAX = 9990
dprint("hi",5,NUM_DEBUG_MIN)
print(f" {disk_map[0:20]}")
print(f" {gap_positions}")

while(file_id > 0):
    pos = np.where(disk_map == str(file_id))    
    found = False
    i = 0
    temp = [int(k) for k in list(gap_positions.keys())]
    temp.sort()
    keys = [str(k) for k in temp]
    dprint(file_id, gap_positions)
    while i < len(keys) and not found:
        dprint(f"trying with key at {i} {keys[i]}")
        space = gap_positions[keys[i]]
        num = len(pos[0])
        dprint(f" need {num} have {space} at {keys[i]}, this file id {file_id} is at {pos[0][0]}")
        dprint(f" here {disk_map[0:20]}")
        if num <= space and int(keys[i]) < pos[0][0]:
            for j in range(0,num):
                disk_map[int(keys[i])+j] = file_id
                disk_map[pos[0][0]+j] = "."
            
            dprint(disk_map)
            dprint("------------------")
            found = True
            
            
            gap_positions.pop(keys[i], None) # delete key
            if space-num > 0:
                gap_positions[str(int(keys[i])+num)] = space-num
            # consider space left by movement!!!
            gap_positions[str(pos[0][0])] = num
            
            temp = [int(k) for k in list(gap_positions.keys())]
            temp.sort()
            keys = [str(k) for k in temp]
            
        if not found:
            i+=1
    
    #print(file_id, disk_map)
    file_id -= 1



checksum = 0

for i in range(0,len(disk_map)):
    if disk_map[i] != ".":
        checksum += i * int(disk_map[i])
        if i < 200:
            print(i, disk_map[i], i*int(disk_map[i]), checksum)
    else:
        if i < 200:
            print(i,".")

print(checksum)

#part 2

print(f"Time: {time.time()-t} seconds")