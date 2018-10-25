import random

from graphviz import Digraph
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

dot = Digraph()

dot.attr(rankdir='TB', size="7.75,10.25")

dot.node('N0', 'N0', pos="2,6!")
dot.node('N1', 'N1', pos="4,6!")

dot.node('N2', 'N2', pos="0,4!")
dot.node('A', 'A', pos="2,4!")
dot.node('B', 'B', pos="4,4!")
dot.node('N3', 'N3', pos="6,4!")

dot.node('N4', 'N4', pos="0,2!")
dot.node('C', 'C', pos="2,2!")
dot.node('D', 'D', pos="4,2!")
dot.node('E', 'E', pos="6,2!")
dot.node('N5', 'N5', pos="8,2!")

dot.node('N6', 'N6', pos="2,0!")
dot.node('N7', 'N7', pos="4,0!")

# from, to, weight, saturation
edges = [
    ('A', 'B', 5, random.uniform(0, 1)),
    ('A', 'C', 2, random.uniform(0, 1)),
    ('A', 'N0', 1, random.uniform(0, 1)),
    ('A', 'N2', 1, random.uniform(0, 1)),
    ('B', 'A', 1, random.uniform(0, 1)),
    ('B', 'D', 1, random.uniform(0, 1)),
    ('B', 'N1', 1, random.uniform(0, 1)),
    ('B', 'N3', 1, random.uniform(0, 1)),
    ('B', 'E', 1, random.uniform(0, 1)),
    ('C', 'A', 1, random.uniform(0, 1)),
    ('C', 'D', 1, random.uniform(0, 1)),
    ('C', 'N4', 1, random.uniform(0, 1)),
    ('C', 'N6', 1, random.uniform(0, 1)),
    ('D', 'C', 1, random.uniform(0, 1)),
    ('D', 'E', 1, random.uniform(0, 1)),
    ('D', 'N7', 1, random.uniform(0, 1)),
    ('E', 'D', 1, random.uniform(0, 1)),
    ('E', 'N5', 1, random.uniform(0, 1)),
    ('N0', 'A', 1, random.uniform(0, 1)),
    ('N1', 'B', 1, random.uniform(0, 1)),
    ('N2', 'A', 1, random.uniform(0, 1)),
    ('N3', 'B', 1, random.uniform(0, 1)),
    ('N4', 'C', 1, random.uniform(0, 1)),
    ('N5', 'E', 1, random.uniform(0, 1)),
    ('N6', 'C', 1, random.uniform(0, 1)),
    ('N7', 'D', 1, random.uniform(0, 1))
]

# 00ff00 = 0 green
# ff0000 = 1 red
# 256 values 1/256
# dot.edge('A', 'B', penwidth='3', color='#c0c0c0', pos="0,0!")

for e in edges:
    start = e[0]
    end = e[1]
    capacity = e[2]
    saturation = e[3]

    saturation_color_red = round(saturation * 256)
    saturation_color_green = 256 - round(saturation * 256)

    color = '#%02x%02x%02x' % (saturation_color_red, saturation_color_green, 0)

    dot.edge(start, end, penwidth=str(capacity), color=color)

# printing dot source code to
dot.render('outputs/graph-viz', view=False)
