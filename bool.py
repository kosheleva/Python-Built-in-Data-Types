x1 = True # True
x2 = False # False
x3 = 1 == 1 # True
x4 = not True # False
x5 = not 1.8 # False
x6 = bool(2) # True
x7 = 9 < 7 # False
x8 = 9 != 7 # True

print(x1, x2, x3, x4, x5, x6, x7, x8)
 
x = None
print(bool(x)) # False

x = () 
print(bool(x)) # False 
  
x = {} 
print(bool(x)) # False 
  
x = 0.0
print(bool(x)) # False
  
x = 'abc'
print(bool(x)) # True

print(None or 20) # 20

print(None and 20) # None
print(30 and 20) # 20
print(not 0) # True

print(2 is 2) # True
print(2 is 3) # False
print(2 is '2') # False

animals = ['cat', 'dog', 'mouse']
print('cat' in animals) # True
print('elephant' in animals) # False