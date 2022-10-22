#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:33:58 2022

@author: gess
in progress
solving the elevator challenge using a network model
"""


import networkx as nx
import numpy as np

class elevator(object):

    def __init__(self, ID, floors, currentFloor,plan):
        self.ID = ID
        self.floors = floors
        self.currentFloor = currentFloor
        self.plan = nx.path_graph((floors[1]-floors[0])+1)
        
        
        
