import intcode
import itertools

def read_state():
    with open('input/007.txt') as f:
        return list(map(lambda x: int(x), f.readline().strip().split(',')))

class ConfigurationInput(intcode.Input):
    def __init__(self, configurations, outputs, index):
        self.count = 0
        self.configurations = configurations
        self.outputs = outputs
        self.index = index

    def read(self):
        if self.count == 0:
            print('%d reads configuration' % self.index)
            self.count += 1
            return self.configurations[self.index]
        else:
            if self.index == 0 and not self.outputs[-1]:
                print('%d reads default value 0' % self.index)
                return 0
            else:
                if self.index == 0:
                    print('%d reads previous output %d' % (self.index, self.outputs[-1]))
                    return self.outputs[-1]
                else:
                    print('%d reads previous output %d' % (self.index, self.outputs[self.index - 1]))
                    return self.outputs[self.index - 1]

class ConfigurationOutput(intcode.Output):
    def __init__(self, outputs, index):
        self.outputs = outputs
        self.index = index

    def write(self, value):
        print('%d outputs value %d' % (self.index, value))
        self.outputs[self.index] = value

def first():
    a = b = c = d = e = range(0, 5)
    configurations = [(a, b, c, d, e) for (a, b, c, d, e) in itertools.product(a, b, c, d, e) if len(set([a, b, c, d, e])) == 5]
    
    result = []

    for config in configurations:
        outputs = [None, None, None, None, None]
        for (index, amp) in enumerate(config):
            print(index, outputs, config)
            state = read_state()
            intcode.run(state, ConfigurationInput(config, outputs, index), ConfigurationOutput(outputs, index))

        result.append(outputs[-1])

    print(max(result))

def second():
    a = b = c = d = e = range(5, 10)
    configurations = [(a, b, c, d, e) for (a, b, c, d, e) in itertools.product(a, b, c, d, e) if len(set([a, b, c, d, e])) == 5]
    
    result = []

    for config in configurations:
        outputs = [None, None, None, None, None]
        states = {}
        channels = {}
        index = 0

        while True:
            if index in states:
                (state, ip, halted) = states[index]
            else:
                state = read_state()
                ip = 0
            
            if index in channels:
                (input, output) = channels[index]
            else:
                input = ConfigurationInput(config, outputs, index)
                output = ConfigurationOutput(outputs, index)
                channels[index] = (input, output)

            print('#%d Starting' % index)
            states[index] = intcode.run(state, input, output, ip)
            print('#%d Stopped / %s' % (index, outputs))

            if index == len(config) - 1 and states[index][2] == True:
                break

            index += 1
            if index >= len(config):
                index = 0

        result.append(outputs[-1])

    print(max(result))

#first()
second()