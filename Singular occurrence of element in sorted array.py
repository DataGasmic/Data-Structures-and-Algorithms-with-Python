l1 = [1,1,2,2,3,3,4,5,5,6,6,7,7]

res = l1[0]

for i in range(1,len(l1)):
    res = res^l1[i] # ^ signifies XOR Operation  - If both numbers are same - 0, if different 1