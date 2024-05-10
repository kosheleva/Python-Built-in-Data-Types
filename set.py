s1 = set()

# --- Creating ---
s2 = set("word")
print(s2) # {'o', 'd', 'r', 'w'}

s3 = set(['a', 'b', 'c', 'b'])
print(s3) # {'c', 'a', 'b'}

s4 = set({'x': 1, 'y': 2})
print(s4) # {'y', 'x'}

s5 = {1, 2, 3}
print(s5) # {1, 2, 3}

# --- Add/update/remove elements ---
s5.add(8)
print(s5) # {8, 1, 2, 3}

set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print(set1) # {4, 5, 10, 11, (6, 7)}

for i in set1:
    print(i)
    # 4
    # 5
    # 10
    # 11
    # (6, 7)

set1.remove((6, 7))
print(set1) # {4, 5, 10, 11}
set1.discard(10)
print(set1) # {4, 5, 11}
set1.pop()
print(set1) # {5, 11}
set1.clear()
print(set1) # set()

# --- Frozenset ---
tpl = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
fset1 = frozenset(tpl)
# (immutable):
# fset1.add(2) # AttributeError: 'frozenset' object has no attribute 'add'