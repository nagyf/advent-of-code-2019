from enum import Enum

class Direction(Enum):
    Left = 1,
    Right = 2,
    Up = 3,
    Down = 4

class LineDirection(Enum):
    Horizontal = 1,
    Vertical = 2

class Segment:
    def __init__(self, from_x, from_y, to_x, to_y):
        self.x1 = min(from_x, to_x)
        self.y1 = min(from_y, to_y)
        self.x2 = max(from_x, to_x)
        self.y2 = max(from_y, to_y)
        self.direction = LineDirection.Vertical if self.x1 == self.x2 and self.y1 != self.y2 else LineDirection.Horizontal
        self.original_vector = (from_x, from_y, to_x, to_y)

    def intersect(self, other):
        # They are parallel, so there cannot be any intersection
        if self.direction == other.direction:
            return None
        
        horizontal = self if self.direction == LineDirection.Horizontal else other
        vertical = self if self.direction == LineDirection.Vertical else other

        if horizontal.x1 <= vertical.x1 and horizontal.x2 >= vertical.x1 and vertical.y1 <= horizontal.y1 and vertical.y2 >= horizontal.y1:
            return (vertical.x1, horizontal.y1)
        else:
            return None

    def length(self):
        return manhattan_distance(self.x1, self.y1, self.x2, self.y2)
    
    def has_point(self, x, y):
        if self.direction == LineDirection.Horizontal:
            return self.y1 == y and self.x1 <= x and self.x2 >= x
        else:
            return self.x1 == x and self.y1 <= y and self.y2 >= y

    def __str__(self):
        dir = 'H' if self.direction == LineDirection.Horizontal else 'V'
        return '%s (%d,%d) -> (%d,%d)' % (dir, self.x1, self.y1, self.x2, self.y2)
    
    def __repr__(self):
        return self.__str__()

def parse_direction(str):
    dir = str[0]
    distance = int(str[1:])
    if dir == 'L':
        dir = Direction.Left
    elif dir == 'R':
        dir = Direction.Right
    elif dir == 'U':
        dir = Direction.Up
    elif dir == 'D':
        dir = Direction.Down
    return (dir, distance)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def parse_segments(wire):
    start = (0, 0)
    segment = []

    for (direction, distance) in wire:
        if direction == Direction.Left:
            next = (start[0] - distance, start[1])
        elif direction == Direction.Right:
            next = (start[0] + distance, start[1])
        elif direction == Direction.Up:
            next = (start[0], start[1] + distance)
        elif direction == Direction.Down:
            next = (start[0], start[1] - distance)

        segment.append(Segment(start[0], start[1], next[0], next[1]))
        start = next
    
    return segment

# Calculates how much steps you need on the given wire to reach a certain point
def steps_to_reach(wire, intersection):
    steps = 0
    for segment in wire:
        if segment.has_point(intersection[0], intersection[1]):
            # If the current segment contains the intersection
            if segment.direction == LineDirection.Horizontal:
                steps += abs(segment.original_vector[0] - intersection[0])
            else:
                steps += abs(segment.original_vector[1] - intersection[1])
            break
        else:
            # Otherwise just increase the steps with the segment length
            steps += segment.length()

    return steps

def main():
    with open('data/003.txt', 'r') as f:
        wires = [line.strip().split(',') for line in f.readlines()]
        directions = [list(map(parse_direction, wire)) for wire in wires]

    # Parse all the line segments
    wires = []
    for wire in directions:
        wires.append(parse_segments(wire))

    # Check all the intersections
    intersections = []
    for segmentA in wires[0]:
        for rest in wires[1:]:
            for segmentB in rest:
                intersection = segmentA.intersect(segmentB)
                if intersection and intersection != (0, 0):
                    intersections.append(intersection)

    # First excercise
    print(min([manhattan_distance(0,0,x,y) for (x,y) in intersections]))

    # Second excercise
    result = []
    for intersection in intersections:
        steps = 0
        for wire in wires:
            steps += steps_to_reach(wire, intersection)
        result.append(steps)
    print(min(result))

main()