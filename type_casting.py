x = 1.5
y = 2

sum = x + y
print(sum, type(sum)) # 3.5 <class 'float'>


# x1 = "abc"
# x2 = 5
# sum_x1_x2 = x1 + x2
# print(sum_x1_x2, type(sum_x1_x2))
# # TypeError: can only concatenate str (not "int") to str

# print(int("abc"))
# # ValueError: invalid literal for int() with base 10: 'abc'



print(int(10.2)) # 10
print(float(2)) # 2.0
print(complex(5)) # (5+0j)
print(str(5), type(str(5))) # 5 <class 'str'>
print(bool(1)) # True
print(bool(0)) # False
print(bool(0.7)) # True
print(bool(200)) # True
print(bool(-1)) # True
print(bool(-0.4)) # True
print(None) # None

x2 = list((1, 2, 3))
print(x2, type(x2)) # [1, 2, 3] <class 'list'>

x3 = list("abc")
print(x3, type(x3)) # ['a', 'b', 'c'] <class 'list'>