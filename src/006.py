def build_graph(orbits):
    vertices = set()
    for (a, b) in orbits:
        vertices.add(a)
        vertices.add(b)

    graph = {}
    for orbit in orbits:
        if orbit[0] not in graph:
            graph[orbit[0]] = set()
            graph[orbit[0]].add(orbit[1])
        else:
            graph[orbit[0]].add(orbit[1])

        if orbit[1] not in graph:
            graph[orbit[1]] = set()
            graph[orbit[1]].add(orbit[0])
        else:
            graph[orbit[1]].add(orbit[0])

    return (graph, vertices)

class Graph:
    def __init__(self, orbits):
        self.graph, self.vertices = build_graph(orbits)

def count_orbits(g, start_node):
    direct = 0
    indirect = 0
    queue = [(start_node, 0)]
    discovered = set(start_node)

    distances = {start_node: 0}

    while len(queue) > 0:
        (next, level) = queue.pop()
        discovered.add(next)
        if next in g:
            children = g[next].difference(discovered)
            direct += len(children)
            indirect += len(children) * level
            
            for child in children:
                distances[child] = level + 1

            queue.extend([(child, level + 1) for child in children])

    return direct + indirect, distances

def main():
    with open('data/006.txt', 'r') as f:
        orbits = [tuple(line.strip().split(')')) for line in f.readlines()]

    graph = Graph(orbits)
    print(count_orbits(graph.graph, 'COM')[0])
    print(count_orbits(graph.graph, 'YOU')[1]['SAN'] - 2) # -2 because we dont want to count the planet we are orbiting now, and SAN itself

if __name__ == '__main__':
    main()