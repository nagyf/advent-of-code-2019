width = 25
height = 6

def first():
    with open('input/008.txt', 'r') as f:
        image = f.readline().strip()

    n = width * height
    layers = [image[i:i + n] for i in range(0, len(image), n)]
    
    best_count = None
    best_layer = None
    for layer in layers:
        count = layer.count('0')
        if best_layer == None or best_count > count:
            best_count = count
            best_layer = layer
    
    print(best_layer.count('1') * best_layer.count('2'))

first()

def display_image(ch):
    if ch == 2:
        return ' '
    elif ch == 1:
        return '+'
    else:
        return ' '

def second():
    with open('input/008.txt', 'r') as f:
        image = f.readline().strip()

    n = width * height
    layers = [image[i:i + n] for i in range(0, len(image), n)]
    
    result = []
    for (index, ch) in enumerate(layers[0]):
        ch = int(ch)
        if ch == 0 or ch == 1:
            result.append(ch)
        else:
            result.append(2)
            for layer in layers[1:]:
                if int(layer[index]) == 0 or int(layer[index]) == 1:
                    result[index] = int(layer[index])
                    break
    
    result = list(map(display_image, result))
    result = [result[i:i + width] for i in range(0, len(result), width)]
    result = list(map(lambda x: ''.join(x), result))

    for line in result:
        print(line)

second()