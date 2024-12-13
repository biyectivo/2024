import re
import math
import numpy as np
import itertools as it
import time


total = 0
buttons = []
prizes = []
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_13.txt") as file:
    for line in file:
        regex = re.findall(r"X\+(\d+), Y\+(\d+)", line)
        if regex != []:
            buttons.append(regex[0])
        else:
            regex = re.findall(r"X=(\d+), Y=(\d+)", line)
            if regex != []:
                prizes.append(regex[0])
                
t = time.time()

print(buttons)
print(prizes)

min_tokens = 0
for p in range(0, len(prizes)):
    button_a = buttons[2*p]
    button_b = buttons[2*p+1]
    
    solutions = []
    for num_a in range(0,100):
        for num_b in range(0,100):
            result_x = int(button_a[0]) * num_a + int(button_b[0]) * num_b
            result_y = int(button_a[1]) * num_a + int(button_b[1]) * num_b
            
            if result_x == int(prizes[p][0]) and result_y == int(prizes[p][1]):
                print(f"Found solution for prize {p}: {num_a} {num_b}")
                solutions.append((num_a, num_b))
    
    if len(solutions) != 0:
        min_tokens_solution = 99999999999999
        
        for s in solutions:
            cost = 3 * s[0] + 1 * s[1]
            if cost < min_tokens_solution:
                min_tokens_solution = cost
        
        min_tokens += min_tokens_solution

print(min_tokens)
print(f"Time: {time.time()-t} s")



#part 2

new_prizes = []
for p in prizes:
    new_prizes.append( (str(int(p[0])+10000000000000),str(int(p[1])+10000000000000)) )
prizes = new_prizes    

min_tokens = 0
for p in range(0, len(prizes)):
    button_a = buttons[2*p]
    button_b = buttons[2*p+1]
    
    solutions = []
    
    num_a = (int(button_b[1]) * int(prizes[p][0]) - int(button_b[0]) * int(prizes[p][1])) / (int(button_b[1]) * int(button_a[0]) - int(button_b[0]) * int(button_a[1]))
    num_b = (int(prizes[p][0]) - int(button_a[0]) * num_a) / int(button_b[0])
    
    # check the solution is actually an integer number of button presses
    if int(num_a) == num_a and int(num_b) == num_b:
        print(f"Found p2 solution for prize {p}: {num_a} {num_b}")
        solutions.append((num_a, num_b))

        min_tokens += 3 * num_a + num_b
print(min_tokens)
