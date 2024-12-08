import re
import math
import numpy as np
import itertools as it
import time

t = time.time()

def calc(a,b,op):
    if op == "+":
        return a+b
    elif op == "*":
        return a*b
    elif op == "||":
        return int(str(a)+str(b))
    
a = 0
operators_p1 = ["+","*"]
operators_p2 = ["+","*","||"]
operators = operators_p2

total = 0
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_7.txt") as file:
    for line in file:
       #print(line)
        data = line.strip().split(":")
        result = int(data[0])
        operands = [int(n) for n in data[1].split( )]
        
        n = [p for p in it.product(operators, repeat=len(operands)-1)]
        for nn in n:
            a = operands[0]
            op_result = 0
            for i in range(1,len(operands)):
                b=operands[i]
                #print(f"  calculating with {a} {b} {nn[i-1]}")
                op_result = calc(a,b,nn[i-1])
                a = op_result
                
                #print(f"{nn} {result} vs {op_result}")
            if result == op_result:
                #print(f" bingo {nn}")
                total += result
                break
            #else:
                #print(" this combo did not work")
print(total)
print(f"Time: {time.time()-t} seconds")