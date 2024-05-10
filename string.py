# --- String creation ---
s1 = 'Hello' # Hello <class 'str'> 
s2 = str(100.00) # 100.0 <class 'str'>
s3 = str("abc") # abc <class 'str'>
s4 = str(False) # False <class 'str'>

print(s1, type(s1), s2, type(s2), s3, type(s3), s4, type(s4))

print(s4 == False) # False

a = 'Hello'
b = "Hello"
c = '''Hello'''
d = '''
A
B
C
'''
e = "It's a program"

print(a, b, c, d, e)


# --- Accessing string characters ---
word = 'programming'
print(len(word)) # 11
print(word[0], word[4], word[10]) # p r g
print(word[-2]) # n
print(word[0:5]) # progr
print(word[3:-3]) # gramm
print(word[::-1]) # gnimmargorp
print(''.join(reversed(word))) # gnimmargorp
print(word[0:5] + 'A' + word[6:11]) # progrAmming

# del word[2] # TypeError: 'str' object doesn't support item deletion

# --- Escaping ---
print('It\'s a program') # It's a program


# --- Formatting ---
str1 = 'My name is: {}'.format('Maria') # My name is: Maria
str2 = 'My name is: {1} {0}'.format('Maria', 'Ko') # My name is: Ko Maria
str3 = 'My name is: {name} {surname}'.format(name = 'Maria', surname = 'Ko') # My name is: Maria Ko

print(str1, str2, str3)


str1 = "{0:b}".format(16) # 10000
str2 = "{0:e}".format(165.6458) # 1.656458e+02
str3 = "{0:.5f}".format(1/6) # 0.16667

print(str1, str2, str3)


# --- Alignment ---
str1 = "|{:<10}|{:^10}|{:>10}|".format('A','B','C') # |A         |    B     |         C| 
str2 = "\n{0:^16} was invented in {1:<4}!".format("Radio", 1897) 
#      Radio       was invented in 1897!
print(str1, str2)
