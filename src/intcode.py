class Input:
    def read(self):
        raise Exception('Input requested, but there are no input devices!')

class Output:
    def write(self, data):
        raise Exception('Output requested, but there are no output devices!')

class StandardInput(Input):
    def read(self):
        return int(input('Input: '))

class StandardOutput(Output):
    def write(self, data):
        print('> %s' % data)

def run(state, i=StandardInput(), o=StandardOutput()):
    ip = 0
    running = True

    while running == True:
        (should_continue, next) = execute_op(state, ip, i, o)
        running = should_continue
        ip = next

    return state[0]

def read_parameter(state, param, param_mode):
    if param_mode == 0:
        return state[state[param]]
    elif param_mode == 1:
        return state[param]
    else:
        raise Exception('Unknown parameter mode: %d' % param_mode)

def execute_op(state, ip, input, output):
    instruction = '%05d' % state[ip]
    param_mode_1 = int(instruction[2])
    param_mode_2 = int(instruction[1])
    param_mode_3 = int(instruction[0])
    opcode = int(instruction[3:])

    if opcode == 1:
        x = read_parameter(state, ip + 1, param_mode_1)
        y = read_parameter(state, ip + 2, param_mode_2)
        r = state[ip+3]

        state[r] = x + y
        print('= %d' % (state[r]))
        return (True, ip + 4)
    elif opcode == 2:
        x = read_parameter(state, ip + 1, param_mode_1)
        y = read_parameter(state, ip + 2, param_mode_2)
        r = state[ip+3]

        state[r] = x * y
        print('= %d' % (state[r]))
        return (True, ip + 4)
    elif opcode == 3:
        r = state[ip+1]
        value = input.read()
        state[r] = value

        return (True, ip + 2)
    elif opcode == 4:
        x = read_parameter(state, ip + 1, param_mode_1)
        output.write(x)
        
        return (True, ip + 2)
    elif opcode == 5:
        x = read_parameter(state, ip + 1, param_mode_1)
        y = read_parameter(state, ip + 2, param_mode_2)
        if x != 0:
            return (True, y)
        else:
            return (True, ip + 3)
    elif opcode == 6:
        x = read_parameter(state, ip + 1, param_mode_1)
        y = read_parameter(state, ip + 2, param_mode_2)
        if x == 0:
            return (True, y)
        else:
            return (True, ip + 3)
    elif opcode == 7:
        x = read_parameter(state, ip + 1, param_mode_1)
        y = read_parameter(state, ip + 2, param_mode_2)
        r = state[ip + 3]
        if x < y:
            state[r] = 1
            return (True, ip + 4)
        else:
            state[r] = 0
            return (True, ip + 4)
    elif opcode == 8:
        x = read_parameter(state, ip + 1, param_mode_1)
        y = read_parameter(state, ip + 2, param_mode_2)
        r = state[ip + 3]
        if x == y:
            state[r] = 1
            return (True, ip + 4)
        else:
            state[r] = 0
            return (True, ip + 4)
    elif opcode == 99:
        return (False, ip + 1)
    else:
        raise Exception('Unknown opcode: %s' % state[ip])