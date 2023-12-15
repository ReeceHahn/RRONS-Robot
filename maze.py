class Node:
    def __init__(self):
        self.position = None
        self.adjacent_nodes = {}

    def add_edge(self, neighbour, distance):
        self.adjacent_nodes[neighbour] = distance
        
maze = []
coordinates = (0,0)
current_node = None
previous_node = None

def add_node(time, direction):
    global coordinates, current_node, previous_node
    
    previous_node = current_node

    coordinate_displacement = int(round(time / 1.1))

    #update coordinates
    if direction == 'up':
        coordinates = (coordinates[0] + coordinate_displacement, coordinates[1])
    elif direction == 'down':
        coordinates = (coordinates[0] - coordinate_displacement, coordinates[1])
    elif direction == 'right':
        coordinates = (coordinates[0], coordinates[1] + coordinate_displacement)
    elif direction == 'left':
        coordinates = (coordinates[0], coordinates[1] - coordinate_displacement)
        
    #check if a node with the same coordinates already exists in the maze
    try:
        existing_node = next(node for node in maze if node.position == coordinates)
    except StopIteration:
        existing_node = None

    if existing_node is not None:
        current_node = existing_node
    else:
        current_node = Node()
        current_node.position = coordinates
        maze.append(current_node)

def add_edge():
    global previous_node, current_node

    if previous_node is not None and current_node is not None:
        
        #check if the edge already exists
        if not (current_node in previous_node.adjacent_nodes and previous_node in current_node.adjacent_nodes):

            #calculate distance using pythagoras
            x1, y1 = previous_node.position
            x2, y2 = current_node.position
            distance = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5)

            previous_node.add_edge(current_node, distance)
            current_node.add_edge(previous_node, distance)
            
def find_end_node():
    #create a list to store potential end nodes
    potential_end_nodes = []

    #iterate through each node of the maze with 2 or 3 adjacent nodes
    for node in maze:
        
        #check if the node has 2 or 3 adjacent nodes
        if len(node.adjacent_nodes) in {2, 3}:
            
            # Identify all possible diagonal nodes
            diagonal_nodes = [
                neighbour for neighbour in maze
                if abs(node.position[0] - neighbour.position[0]) == 1 and abs(node.position[1] - neighbour.position[1]) == 1
            ]

            #check if the node and its diagonal node share exactly TWO common neighbours
            for diagonal_node in diagonal_nodes:
                common_neighbours = set(node.adjacent_nodes.keys()) & set(diagonal_node.adjacent_nodes.keys())
                if len(common_neighbours) == 2:
                    # Append the node to the potential end nodes
                    potential_end_nodes.append(node)
                    break  # Break to the next diagonal node

    # Iterate through the potential end nodes and return the one with three neighbours
    for potential_end_node in potential_end_nodes:
        if len(potential_end_node.adjacent_nodes) == 3:
            return potential_end_node

    return None  # Return None if no end node is found

def dijkstra_shortest_path(start_node, end_node):
    #initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in maze}
    distances[start_node] = 0

    #set to keep track of visited nodes
    visited = set()

    #dictionary to store the previous node in the optimal path
    previous_nodes = {node: None for node in maze}

    #iterate until all nodes are visited
    while visited != set(maze):
        
        #find the unvisited node with the smallest distance
        current_node = min(
            (node for node in maze if node not in visited),
            key=lambda x: distances[x]
        )
        visited.add(current_node)

        #update distances to neighbours through the current node
        for neighbour, distance in current_node.adjacent_nodes.items():
            new_distance = distances[current_node] + distance
            
            #check if the new distance is shorter than the existing one
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous_nodes[neighbour] = current_node

    #reconstruct the path
    path = []
    current = end_node
    while current is not None:
        path.insert(0, current.position)  #insert at the beginning to maintain the correct order
        current = previous_nodes[current]

    return path

def show_maze():
    for node in maze:
        print(f"Node at position: {node.position}\n")
        for neighbour, distance in node.adjacent_nodes.items():
            print(f"Connected to node at position {neighbour.position} with distance {distance}\n")
        print()
