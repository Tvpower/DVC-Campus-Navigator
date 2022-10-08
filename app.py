# importing Flask and other modules
from flask import Flask, request, render_template

# External functions for implementing Dijkstra's Algorithm
from graph_functions import retrace_routes, calculate_distance, get_path_info
from instance import Graph
from campus_data import get_init_main
import json

path_json_path = "static/path.json"


# open_json:
# Used to create the all_nodes dictionary with coordinate data
def open_json(target_json):
    with open(target_json, 'r') as f:
        content = json.load(f)
    f.close()
    return content


def write_json(content, target_json):
    with open(target_json, 'w') as f:
        json.dump(content, f, indent=4)
    f.close()


# coordinate_data.json path
coord_data_path = "static/coordinate_data.json"
building_names_path = "static/building_names.json"

building_names = open_json(building_names_path)

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    return render_template("base.html")


@app.route('/shortestPath', methods=["GET", "POST"])
def dfd():
    data = request.get_json(force=True)

    if request.method == "POST":
        # getting input with name = currentLoc in HTML form
        source = data["currentLoc"]
        # getting input with name = dest in HTML form
        destination = data["dest"]
        # all_nodes = get_all_nodes()
        all_nodes = open_json(coord_data_path)
        init_main = get_init_main()

        # Make the one-way routes two-way
        retrace_routes(init_main)

        # Calculate the distance between each edge
        calculate_distance(init_main, all_nodes)

        # Create Graph Object
        graph = Graph(all_nodes, init_main)

        # starting_node = "PAC"
        # target_node = "HSF"

        # Convert the Building Name inputs to the Map Acronyms
        starting_node = building_names[source]
        target_node = building_names[destination]

        path, path_length = get_path_info(graph, starting_node, target_node)

        # Path is reversed because main.js pushes path[0] into a stack
        path.reverse()

        file1 = open("static/file.txt", "a")
        file1.truncate(0)
        for x in path:
            file1.write(x + " ")
        file1.close()

        # Write JSON path.json
        # write_json(path_dict, path_json_path)

        return source + "\n" + destination


if __name__ == '__main__':
    app.run()
