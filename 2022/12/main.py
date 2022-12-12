from queue import Queue

class Node:
    def __init__(self, value, row, col):
        self.row = row
        self.col = col
        self.value = value
        self.neighbours = []

    def __repr__(self):
        description = self.value + ":" + str(self.row) + "," + str(self.col) + ":"
        for neighbour in self.neighbours:
            description += "(" + str(neighbour.row) + "," + str(neighbour.col) + ")"
        return description
    
    def intValue(self):
        if self.value == "S":
            return 0
        elif self.value == "E":
            return 25
        return ord(self.value) - ord('a')

class GraphParameters:
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.nodes = []

def readHeightMapNodes():
    height_map = []
    with open("./2022/12/input.txt", "r") as file:
        for line in file.read().splitlines():
            height_map.append([])
            for char in line:
                height_map[len(height_map)-1].append( \
                    Node(char, len(height_map)-1, len(height_map[len(height_map)-1])))
    return height_map

def addNeighbourIfValid(neighbours, row, col, height_map, max_value):
    if row >= 0 and col >= 0 and row < len(height_map) and col < len(height_map[0]):
        if height_map[row][col].intValue() <= max_value:
            neighbours.append(height_map[row][col])

def createGraphParameters():
    height_map = readHeightMapNodes()
    graph = GraphParameters()
    
    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            node = height_map[row][col]

            if node.value == 'S':
                graph.start_node = node
            if node.value == 'E':
                graph.end_node = node

            neighbours = []
            max_value = node.intValue() + 1
            addNeighbourIfValid(neighbours, row-1, col, height_map, max_value)
            addNeighbourIfValid(neighbours, row+1, col, height_map, max_value)
            addNeighbourIfValid(neighbours, row, col-1, height_map, max_value)
            addNeighbourIfValid(neighbours, row, col+1, height_map, max_value)
            node.neighbours = neighbours
            
            graph.nodes.append(node)
    
    return graph

def shortestPathLength(graph_parameters):
    num_steps = 0
    seen = set()
    seen.add(graph_parameters.start_node)
    nodes_to_check = set()
    nodes_to_check.add(graph_parameters.start_node)

    while len(nodes_to_check) > 0:
        new_nodes_to_check = set()
        
        for node in nodes_to_check:
            if node == graph_parameters.end_node:
                return num_steps

            for neighbour_node in node.neighbours:
                if neighbour_node not in seen:
                    new_nodes_to_check.add(neighbour_node)
                    seen.add(neighbour_node)

        num_steps += 1
        nodes_to_check = new_nodes_to_check
    
    return -1

def shortestPathLengthFromBottom(graph_parameters):
    result = -1
    for node in graph_parameters.nodes:
        if node.intValue() == 0:
            graph_parameters.start_node = node
            num_steps = shortestPathLength(graph_parameters)
            if num_steps != -1 and (result == -1 or num_steps < result):
                result = num_steps
    return result

def main():
    graph_parameters = createGraphParameters()
    print(shortestPathLength(graph_parameters))
    print(shortestPathLengthFromBottom(graph_parameters))

if __name__ == "__main__":
    main()