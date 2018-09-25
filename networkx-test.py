from __future__ import division

import matplotlib.pyplot as plt
import networkx as nx

G = nx.MultiDiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('A', 'N0'), ('A', 'N2'), ('B', 'A'), ('B', 'D'), ('B', 'N1'), ('B', 'N3'), ('C', 'A'),
     ('C', 'D'), ('C', 'N4'), ('C', 'N6'), ('D', 'C'), ('D', 'N5'), ('D', 'N7'), ('N0', 'A'), ('N1', 'B'), ('N2', 'A'),
     ('N3', 'B'), ('N4', 'C'), ('N5', 'D'), ('N6', 'C'), ('N7', 'D')])

# pos = nx.layout.kamada_kawai_layout(G)
pos = {
    'A': (0, 0),
    'B': (1, 0),
    'C': (0, 1),
    'D': (1, 1),
    'N0': (0, -1),
    'N1': (1, -1),
    'N2': (-1, 0),
    'N3': (2, 0),
    'N4': (-1, 1),
    'N5': (2, 1),
    'N6': (0, 2),
    'N7': (1, 2),
}

node_sizes = [10 for i in range(len(G))]
node_colors = ['blue' if e in ('A', 'B', 'C', 'D') else 'red' for e in G.nodes]

M = G.number_of_edges()

edge_colors = [255]*M
# edge_alphas = [0.9 for _ in range(M)]

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)
edge_labels = nx.draw_networkx_labels(G, {k: (p[0] + 0.1, p[1]+0.1) for k, p in pos.items()})
edges = nx.draw_networkx_edges(G, pos, node_size=node_sizes, arrowstyle='->',
                               arrowsize=10, edge_color=edge_colors,
                               width=2)
# set alpha value for each edge
# for i in range(M):
#     edges[i].set_alpha(edge_alphas[i])

# pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
# pc.set_array(edge_colors)
# plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()
plt.show()
