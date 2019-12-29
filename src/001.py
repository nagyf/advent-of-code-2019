import math

def first():
    with open('input/001.txt') as f:
        modules = f.readlines()

    fuels = [mass(int(x)) for x in modules]
    print(sum(fuels))

def second():
    with open('input/001.txt') as f:
        modules = f.readlines()

    fuels = [mass(int(x)) + fuel_mass(int(x)) for x in modules]
    print(sum(fuels))

def fuel_mass(fuel):
    m = mass(fuel)
    result = 0
    while mass(m) > 0:
        m = mass(m)
        result += m
    return result

def mass(item):
    return math.floor(item / 3) - 2

first()
second()