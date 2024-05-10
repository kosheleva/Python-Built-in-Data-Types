print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(0, 20, 2) 
print(list(r)) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(list(r[2:5])) # [4, 6, 8]

for i in range(5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
