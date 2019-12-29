def first():
    state = read_state()
    state[1] = 12
    state[2] = 2

    result = run(state)
    print(result)


def second():
    state = read_state()

    for (noun, verb) in [(noun, verb) for noun in range(1, 100) for verb in range(1, 100)]:
        s = state[:]
        s[1] = noun
        s[2] = verb

        result = run(s)
        if result == 19690720:
            print(100 * noun + verb)


def run(state):
    ip = 0
    running = True

    while running:
        (running, next) = execute_op(state, ip)
        ip += next

    return state[0]


def read_state():
    with open('input/002.txt') as f:
        return list(map(lambda x: int(x), f.readline().strip().split(',')))


def execute_op(state, ip):
    if state[ip] == 1:
        x = state[ip+1]
        y = state[ip+2]
        r = state[ip+3]
        state[r] = state[x] + state[y]
        return (True, 4)
    elif state[ip] == 2:
        x = state[ip+1]
        y = state[ip+2]
        r = state[ip+3]
        state[r] = state[x] * state[y]
        return (True, 4)
    elif state[ip] == 99:
        return (False, 1)
    else:
        print('Unknown opcode: %s' % state[ip])
        return (True, 0)


first()
second()
