import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc
from classes import Vertex, Edge, Polygon
from functions import *
from initial_configuration import verts

print ("initialization")

edges_initial=edge_assignments(verts)
polygons_initial=polygon_assignment(edges_initial)

Polygon.a_0=polygons_initial[0].area()
Polygon.p_0=3.7

print("polygon areas", [p.area() for p in polygons_initial])
print("polygon energy", [p.energy() for p in polygons_initial])
fourcell_plotter(verts,edges_initial)

print([v.coordinates for v in verts])

l_vals,epsilon=np.linspace(2,0,10,retstep=True)
print("ep",epsilon)
l_vals=np.delete(l_vals,[0])
vertex_final=copy.deepcopy(verts)
e=[]

for l in l_vals:
    
    verts_test=vertex_monte_carlo(vertex_final,l,epsilon,10000)
    
    
    edges_test=edge_assignments(verts_test)
    polygons_test=polygon_assignment(edges_test)

    
    if True:
        fourcell_plotter(verts_test,edges_test)
        print("polygon areas", [p.area() for p in polygons_test])
        print("polygon energy", [p.energy() for p in polygons_test])
        print("total energy",np.sum( [p.energy() for p in polygons_test]))
        e.append(np.sum( [p.energy() for p in polygons_test]))
    vertex_final=verts_test    


plt.plot(l_vals,e)