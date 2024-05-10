# --- Creating ---
t1 = () # ()
t2 = (1, 'word', 0.7, ['x', 'y']) # (1, 'word', 0.7, ['x', 'y'])
t3 = tuple([1, 2, 3]) # (1, 2, 3)
print(t1, t2, t3)


# --- Accessing ---
print(t2[2]) # 0.7
a, b, c, d = t2
print(a, b, c, d) # 1 word 0.7 ['x', 'y']


# --- Concatenation ---
print(t2 + t3) # (1, 'word', 0.7, ['x', 'y'], 1, 2, 3)


# --- Slicing ---
x = tuple('ABCDEFG')
print(x)  # ('A', 'B', 'C', 'D', 'E', 'F', 'G')
x1 = x[1:]
print(x, x1)
# ('A', 'B', 'C', 'D', 'E', 'F', 'G') ('B', 'C', 'D', 'E', 'F', 'G')
