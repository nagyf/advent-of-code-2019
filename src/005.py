import intcode

def read_state():
    with open('input/005.txt') as f:
        return list(map(lambda x: int(x), f.readline().strip().split(',')))

def first():
    state = read_state()
    result = intcode.run(state)
    print(result)

first()