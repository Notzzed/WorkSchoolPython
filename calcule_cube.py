def calcule_cube(a):
    cube = a * a * a      # ou bien a**3
    return cube

x = 3
y = 4
z = calcule_cube(x) + calcule_cube(y)
print(z)
