import re
import math

mult = 0
mult2 = 0

with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_3.txt") as file:
    line = "".join(file.readlines())
    
    x = re.findall(r"mul\((\d+,\d+)\)", line, flags = re.S|re.MULTILINE)
    for n in x:
        q = n.split(",")
        mult += int(q[0])*int(q[1])
    
    #s = re.findall(r"don't\(\).*?do\(\)", line, flags = re.S|re.MULTILINE)
    
    s = re.subn(r"don't\(\).*?do\(\)", "", line, flags = re.S | re.MULTILINE)[0]
    s = re.subn(r"don't\(\).*?$", "", s, flags = re.S | re.MULTILINE)
    
    x = re.findall(r"mul\((\d+,\d+)\)", s[0], flags = re.S|re.MULTILINE)
    
    for n in x:
        q = n.split(",")
        mult2 += int(q[0])*int(q[1])
# =============================================================================
#         x = re.findall(r"mul\((\d+,\d+)\)", s[0], flags = re.S | re.MULTILINE)
#         for n in x:
#             q = n.split(",")
#             mult2 += int(q[0])*int(q[1])
# =============================================================================
        
print(mult)
print(mult2)
