# --- Creating the list ---
a = ['a', 'b', 'c'] # ['a', 'b', 'c']
b = [] # []
c = list("123") # ['1', '2', '3']
print(a, b, c)

# --- Accessing items ---
print(c[0]) # 1
print(a[2]) # c
print(a[-1]) # c
# print(b[2]) # IndexError: list index out of range
# print(b[0]) # IndexError: list index out of rang

matrix = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
print(matrix[1][2]) # 0

# --- Splitting the string to a list ---
url = 'http://www.server.com/home'
parsed_url = url.split("/")
print(parsed_url) # ['http:', '', 'www.server.com', 'home']
print(type(parsed_url)) # <class 'list'>

# --- Adding to a list ---
seasons = ['summer', 'autumn', 'winter']
print(seasons) # ['summer', 'autumn', 'winter']
seasons.append('spring')
print(seasons) # ['summer', 'autumn', 'winter', 'spring']


seasons = ['summer', 'autumn', 'winter']
print(seasons) # ['summer', 'autumn', 'winter']
seasons.insert(0, 'spring')
print(seasons) # ['spring', 'summer', 'autumn', 'winter']


numbers = [0, 1, 2, 3]
print(numbers) # [0, 1, 2, 3]
numbers.extend([4, 5, 6, 7])
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7]

# --- Reversing ---
numbers.reverse()
print(numbers) # [7, 6, 5, 4, 3, 2, 1, 0]

# --- Removing ---
letters = ['a', 'b', 'c']
letters.remove('b')
print(letters) # ['a', 'c']


numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers[3:5]) # [3, 4]