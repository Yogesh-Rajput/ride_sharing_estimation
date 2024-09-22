import networkx as nx
import matplotlib.pyplot as plt

def create_graph(trip_distance: list) -> nx.DiGraph:
    """
    Creates a directed graph based on the trip distances.

    Args:
        trip_distance: A list of tuples (origin, destination, distance).

    Returns:
        A NetworkX DiGraph object representing the graph.
    """

    G = nx.DiGraph()

    # Get maximum origin and destination for node creation
    max_origin = min(trip_distance, key=lambda x: x[0])[0]
    max_destination = max(trip_distance, key=lambda x: x[1])[1]
    nodes_range = range(max_origin, max_destination + 1)  # Include max_destination

    # Add nodes
    G.add_nodes_from(nodes_range)

    # Add edges with distances using a loop
    for start, end, distance in trip_distance:
        G.add_edge(start, end, weight=distance)

    return G


def plot_graph(G: nx.DiGraph):
    """
    Visualizes the graph.

    Args:
        G: A NetworkX DiGraph object.
    """

    # Visualize the graph
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_size=500, font_size=12, node_color='lightblue',
            edge_color='gray', pos=nx.spring_layout(G))
    plt.title("Your Graph")
    plt.show()

def reduce_graph_dijkstra(G):
    """
    Reduces a graph by removing edges that are longer than the shortest paths between their nodes using Dijkstra's algorithm.

    Args:
        G: A NetworkX DiGraph object.

    Returns:
        The reduced graph.
    """

    reduced_graph = G.copy()

    # Check if the graph is connected
    #if not nx.is_connected(reduced_graph):
    #    print("Warning: Graph is disconnected.")
        # You might want to handle disconnected components separately

    for node in G.nodes():
        try:
            shortest_paths = {v: nx.dijkstra_path_length(reduced_graph, node, v) for v in G.nodes()}
        except nx.NetworkXNoPath:
            # Handle disconnected components or other exceptions
            continue

        for u, v in G.edges(node):
            if G[u][v]['weight'] > shortest_paths[v]:
                reduced_graph.remove_edge(u, v)

    return reduced_graph


def analyze_graph(G: nx.DiGraph):
    """
    Analyzes the graph by printing nodes and their incoming edges.

    Args:
        G: A NetworkX DiGraph object.
    """

    for node in G.nodes():
        print(f"Node: {node}")
        print(f"Incoming edges: {G.in_edges(node)}")