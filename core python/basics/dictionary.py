'''
d = {1: 'may', 2: 'june', 3: 'july', 4: 'august', 5: 'september'}
print(d[1])
print(d[4])
del d[2]
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get(4))
print(d.copy())
print(len(d))
d2 = {'a': 'may', 'b': 'june', 'c': 'july', 'd': 'august'}
if d == d2:
    print("it is equal")
else:
    print("not equal")
'''