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

def run(state, i=StandardInput(), o=StandardOutput(), ip=0, reladdr=0):
    running = True

    while running == True:
        (should_continue, next, halted, reladdr) = execute_op(state, ip, reladdr, i, o)
        running = should_continue
        ip = next

    return state, ip, halted

def read_parameter(state, param, param_mode, reladdr):
    if param_mode == 0:
        return state[param]
    elif param_mode == 1:
        return param
    elif param_mode == 2:
        return reladdr + state[param]
    else:
        raise Exception('Unknown parameter mode: %d' % param_mode)

def execute_op(state, ip, reladdr, input, output):
    instruction = '%05d' % state[ip]
    param_mode_1 = int(instruction[2])
    param_mode_2 = int(instruction[1])
    param_mode_3 = int(instruction[0])
    opcode = int(instruction[3:])

    if opcode == 1:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        y = state[read_parameter(state, ip + 2, param_mode_2, reladdr)]
        r = read_parameter(state, ip + 3, param_mode_3, reladdr)

        state[r] = x + y
        return (True, ip + 4, False, reladdr)
    elif opcode == 2:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        y = state[read_parameter(state, ip + 2, param_mode_2, reladdr)]
        r = read_parameter(state, ip + 3, param_mode_3, reladdr)

        state[r] = x * y
        return (True, ip + 4, False, reladdr)
    elif opcode == 3:
        r = read_parameter(state, ip + 1, param_mode_1, reladdr)
        value = input.read()
        state[r] = value

        return (True, ip + 2, False, reladdr)
    elif opcode == 4:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        output.write(x)
        
        return (True, ip + 2, False, reladdr)
    elif opcode == 5:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        y = state[read_parameter(state, ip + 2, param_mode_2, reladdr)]
        if x != 0:
            return (True, y, False, reladdr)
        else:
            return (True, ip + 3, False, reladdr)
    elif opcode == 6:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        y = state[read_parameter(state, ip + 2, param_mode_2, reladdr)]
        if x == 0:
            return (True, y, False, reladdr)
        else:
            return (True, ip + 3, False, reladdr)
    elif opcode == 7:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        y = state[read_parameter(state, ip + 2, param_mode_2, reladdr)]
        r = read_parameter(state, ip + 3, param_mode_3, reladdr)
        if x < y:
            state[r] = 1
            return (True, ip + 4, False, reladdr)
        else:
            state[r] = 0
            return (True, ip + 4, False, reladdr)
    elif opcode == 8:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        y = state[read_parameter(state, ip + 2, param_mode_2, reladdr)]
        r = read_parameter(state, ip + 3, param_mode_3, reladdr)
        if x == y:
            state[r] = 1
            return (True, ip + 4, False, reladdr)
        else:
            state[r] = 0
            return (True, ip + 4, False, reladdr)
    elif opcode == 9:
        x = state[read_parameter(state, ip + 1, param_mode_1, reladdr)]
        return (True, ip + 2, False, reladdr + x)
    elif opcode == 99:
        return (False, ip + 1, True, reladdr)
    else:
        raise Exception('Unknown opcode: %s' % state[ip])