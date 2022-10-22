#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:33:58 2022

experimenting with networkx

@author: gess
"""


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

floors = [1,50]
numNodes = floors[-1]-floors[0]+1
G = nx.path_graph(numNodes)

for i in range(numNodes):
    
    G.nodes[i]['floorNum'] = i + floors[0]


options = {
    'node_color': G.nodes['floorNum'],
    'node_size': 100,
    'width': 3,
}
nx.draw(G, with_labels=True, font_weight='bold', **options)


plt.show()

        
        



