import re
import math

safe = 0
safe_extended = 0

def sgn(i):
    return 1 if i>0 else (-1 if i<0 else 0)

def is_safe(nums):
    signos = []
    difs = []
    
    for i in range(0,len(nums)-1):
        signos.append(sgn(nums[i]-nums[i+1]))
        difs.append(abs(nums[i]-nums[i+1]))
    thissafe = True and len(set(signos)) == 1 and len([x for x in difs if x >=1 and x <= 3]) ==  len(difs)
    return thissafe

def is_safe_extended(nums: list):
# =============================================================================
#     print(f"  extended: {nums}")
#     i=0
#     found=False
#     sign = sgn(nums[0]-nums[1])
#     while(i<len(nums)-1 and not found):
#         found = abs(nums[i]-nums[i+1]) <1 or abs(nums[i]-nums[i+1]) > 3 or sgn(nums[i]-nums[i+1]) != sign
#         if (not found):
#             i+=1
#     print(f"  Found {found}:{i}")
#     if found:
#         print(f"  Removing {i}:{nums[i]}")
#         nums.pop(i)
#         return is_safe(nums)
#     else:
#         return True
# =============================================================================
    if is_safe(nums):
        return True
    
    safe_trimmed = []    
    for i in range(0, len(nums)):
        k = nums.copy()
        k.pop(i)
        if is_safe(k):
            #print(f"  safe if removing {i}")
            safe_trimmed.append(i)
    return len(safe_trimmed) >= 1
    
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2024\day_2.txt") as file:
    for line in file:
        nums = [int(n.strip()) for n in line.split()]
        
        print(f"Analyze: {nums}")
        
        if is_safe(nums):
            safe += 1
        if is_safe_extended(nums):
            safe_extended += 1
        print(f"Result {is_safe(nums)} {is_safe_extended(nums)}")   
        
            
print(safe)
print(safe_extended)

