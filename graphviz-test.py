from graphviz import Digraph
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

dot = Digraph()

dot.subgraph()

dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')
dot.node('N0', 'N0')
dot.node('N1', 'N1')
dot.node('N2', 'N2')
dot.node('N3', 'N3')
dot.node('N4', 'N4')
dot.node('N5', 'N5')
dot.node('N6', 'N6')
dot.node('N7', 'N7')

edges = [('A', 'B'), ('A', 'C'), ('A', 'N0'), ('A', 'N2'), ('B', 'A'), ('B', 'D'), ('B', 'N1'), ('B', 'N3'), ('C', 'A'),
         ('C', 'D'), ('C', 'N4'), ('C', 'N6'), ('D', 'C'), ('D', 'N5'), ('D', 'N7'), ('N0', 'A'), ('N1', 'B'),
         ('N2', 'A'), ('N3', 'B'), ('N4', 'C'), ('N5', 'D'), ('N6', 'C'), ('N7', 'D')]

for e in edges:
    dot.edge(e[0], e[1])

# dot.edge('A', 'B', penwidth='3', color='#c0c0c0', pos="0,0!")
# dot.edges(
#     ['AB', 'AC', 'AN0', 'AN2', 'BA', 'BD', 'BN1', 'BN3', 'CA', 'CD', 'CN4', 'CN6', 'DC', 'DN5', 'DN7', 'N0A', 'N1B',
#      'N2A', 'N3B', 'N4C', 'N5D', 'N6C', 'N7D'])
# dot.edge('D', 'B', penwidth='3', color='#c0c0c0')
# dot.edge('D', 'B', penwidth='3', color='#c0c0c0')

# printing dot source code to
print(dot.source)

dot.render('outputs/graph-viz', view=True)
