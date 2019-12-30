import intcode

def read_state():
    with open('input/009.txt') as f:
        return list(map(lambda x: int(x), f.readline().strip().split(',')))

def first():
    state = read_state()
    state = state + ([0] * 100000)
    result = intcode.run(state)

first()