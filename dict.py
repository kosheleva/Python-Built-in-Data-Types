table = {
    'width': 60,
    'height': 90,
    'lenght': 80,
    'code': "AXC120",
    'price': 15,
    'currency': 'USD'
}

print(table)
# {'width': 60, 'height': 90, 'lenght': 80, 'code': 'AXC120', 'price': 15, 'currency': 'USD'}

dct = dict([('x', 10), ('y', 20)])
print(dct)
# {'x': 10, 'y': 20}

dct['z'] = 30
print(dct)
# {'x': 10, 'y': 20, 'z': 30}

print(dct['y']) # 20
print(dct.get('y')) # 20