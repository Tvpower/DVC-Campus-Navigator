import math
import sys


# Helper Print Function
def return_path_array(previous_nodes, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    # print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    # print(" -> ".join(reversed(path)))

    return path


# Dijkstra's Algorithm Function
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


# function: retrace_routes()
# purpose: edits init_main, making one-way edges into two-way edges
def retrace_routes(init_main):
    for first_node in init_main:
        for adj_node in init_main[first_node]:
            init_main[adj_node][first_node] = -1


# function: calculate_distance()
# purpose: changes init_main[a][b] to the pixel distance
def calculate_distance(init_main, all_nodes):
    for first_node in init_main:
        for adj_node in init_main[first_node]:
            ax = all_nodes[first_node][0]
            ay = all_nodes[first_node][1]
            bx = all_nodes[adj_node][0]
            by = all_nodes[adj_node][1]
            dist_decimal = math.sqrt(((ax - bx) ** 2) + ((ay - by) ** 2))

            init_main[first_node][adj_node] = round(dist_decimal, 1)


# function: get_path_info()
# purpose: take in
# returns: path, path_length
def get_path_info(graph, starting_node, target_node):
    previous_nodes, shortest_path = dijkstra_algorithm(graph, starting_node)
    path = return_path_array(previous_nodes, starting_node, target_node)
    path_length = round(shortest_path[target_node], 1)

    return path, path_length
