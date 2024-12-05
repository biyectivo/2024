import re
import math
import numpy as np


rules = []
orderings = []

with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_5.txt") as file:
    for line in file:
        if line.find(r"|") != -1:
            rules.append(line.strip().split("|"))
        elif len(line)>1:
            orderings.append(line.strip().split(","))

middle_page_number = 0
middle_page_number_incorrects = 0

for o in orderings:
    print(o)
    i=0
    wrong = False
    while i<len(o)-1 and not wrong:
        first = o[i]
        second = o[i+1]
        correct_rule = [rule for rule in rules if rule[0]==first and rule[1]==second]
        incorrect_rule = [rule for rule in rules if rule[0]==second and rule[1]==first]
        #print(f"  {correct_rule} {incorrect_rule}")
        wrong = len(incorrect_rule) > 0
        if (not wrong):
            i += 1
    
    if not wrong:
        print("CORRECT")
        middle_page_number += int(o[len(o)//2])
    else:
        print("WRONG")
        order = dict()
        for n in o:
            sorting_rules = [rule for rule in rules if rule[0]==n and rule[1] in o]
            order[len(sorting_rules)] = n
        middle_page_number_incorrects += int(order[len(o)//2])

print(middle_page_number)
print(middle_page_number_incorrects)
