## Distance Vector Algorithm Simulator
This project is an interactive web-based simulator for the Distance Vector algorithm, implemented using the Flask framework. 

The Distance Vector algorithm is used to calculate the least-cost path between nodes within a weighted graph. Nodes are only aware of link costs to adjacent neighbours and utilises iterative processes to learn and exchange information about the rest of the graph to recursively improve their understanding of the least-cost paths.

This simulator assumes that all distance vectors are sent to immediate neighbours at the same time, and thus updates are performed simultaneously. Users can input any number of link costs and specify the nature of their graph (directed or undirected), and the application will return the full sequence of routing tables at each node until convergence. A more detailed description of the algorithm and a set of instructions can be found in the application itself.

## Live app
Try the simulator here: https://distance-vector-algorithm-simulator.onrender.com

## How to run locally 
In the terminal:
1. Clone repository: `git clone https://github.com/MaddieMiyazaki/Distance-Vector-Algorithm.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Start the app: `python dv.py`

Then open `http://localhost:5000` in your browser

## Technologies used
- **Framework**: Flask (Python backend)
- **Frontend**: HTML, Javascript, CSS
- **Templating**: Jinja2
- **Mathematical rendering**: MathJax
- **WSGI Server**: Gunicorn (for production deployment)
- **Hosting platform**: Render


## Features

- **Backend Algorithm Implementation**: The Bellman-Ford algorithm is executed using multi-dimensional array handling and iterative updates in Python.
- **Interactive front-end design**: Users submit pairs of nodes and their link costs. This input data is handled and validated by Javascript in real time.
- **Dynamic forms**: An object oriented approach for dynamic DOM manipulation enables users to add or remove links.
- **Responsive Data Visualisation**: HTML tables styled with CSS Flexbox are used to return all iterations for a clear scrollable output.
- **Scalable and flexible input**: Supports graphs of any size as users can add or remove links. This application also lets users toggle between directed and undirected graphs. 

