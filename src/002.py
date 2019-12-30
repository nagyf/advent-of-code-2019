import intcode

def first():
    state = read_state()
    state[1] = 12
    state[2] = 2

    result = intcode.run(state)
    print(result)


def second():
    state = read_state()

    for (noun, verb) in [(noun, verb) for noun in range(1, 100) for verb in range(1, 100)]:
        s = state[:]
        s[1] = noun
        s[2] = verb

        result = intcode.run(s)
        if result == 19690720:
            print(100 * noun + verb)



def read_state():
    with open('input/002.txt') as f:
        return list(map(lambda x: int(x), f.readline().strip().split(',')))

first()
second()
