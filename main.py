
import pandas as pd
from network_graphs import create_graph, reduce_graph_dijkstra, plot_graph


if __name__ == "__main__":
    df = pd.read_excel(r"Toy example_myopic policy.xlsx")
    trip_distance = [(int(df['origin'][i]), int(df['destination'][i]), float(df['trip_distance'][i])) for i in range(len(df))]
    #print(trip_distance)
    G = create_graph(trip_distance)

    # Plot the graph (uncomment if needed)
    #plot_graph(G)

    # Call the function to reduce the graph and store the result
    reduced_graph = reduce_graph_dijkstra(G)

    # Analyze or plot the reduced graph (uncomment if needed)
    # analyze_graph(reduced_graph)
    plot_graph(reduced_graph)
    print(G.number_of_edges())
    print(reduced_graph.number_of_edges())