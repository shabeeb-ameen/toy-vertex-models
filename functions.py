import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc
from classes import Vertex, Edge, Polygon





## Further development idea: Frankly I am not too fond of how these  plotters output currently. Need to study matplotlib and get back on this case.
    
def plotter_2D(edges):
    lines = [[e.vert_a.coordinates,e.vert_b.coordinates]for e in edges]
    lc = mc.LineCollection(lines, linewidths=2)
    
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    for line in lines:     
        plt.scatter(*zip(*line))
    #plt.show()
    return

#def fourcell_plotter(verts,edges):
##    lines = [[e.vert_a.coordinates,e.vert_b.coordinates]for e in edges]
 #   lc = mc.LineCollection(lines, linewidths=2)
 #   fig, ax = pl.subplots()
 #   ax.add_collection(lc)
 #   ax.autoscale()
 #   ax.margins(0.1)
 #   p=[v.coordinates for v in verts]
 #   plt.scatter(*zip(*p))
 #   return

#plotting function in 3 dimensions. Can these two be incorporated into a single function? (is it necessary?)
#def plotter_3D(verts, edges):
#    points=[v.coordinates for v in verts]
#
#    fig = plt.figure(figsize=(8,8), dpi=80)
#    ax  = fig.add_subplot(111, projection = '3d')
#
#    ax.scatter(*zip(*points))
#
#    for e in edges:
#    
#        nodes=[e.vert_a.coordinates,  e.vert_b.coordinates]
#        ax.plot(*zip(*nodes), color = 'b')


#    ax.set_xlabel('$X$')
#    ax.set_ylabel('$Y$')
#    ax.set_zlabel('$Z$')
#    ax.yaxis._axinfo['label']['space_factor'] = 4.0
#    #plt.show()
#    return


def plotter_3D(edges):
    lines=[[e.vert_a.coordinates, e.vert_b.coordinates] for e in edges]

    fig = plt.figure(figsize=(8,8), dpi=1080)
    ax  = fig.add_subplot(111, projection = '3d')
    for line in lines:
        ax.scatter(*zip(*line))

    for e in edges:
    
        nodes=[e.vert_a.coordinates,  e.vert_b.coordinates]
        ax.plot(*zip(*nodes), color = 'b')


    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')
    ax.yaxis._axinfo['label']['space_factor'] = 4.0
    
    return 


#def fourcell_vertex_scatter(verts):
#    p=[v.coordinates for v in verts]
#    plt.scatter(*zip(*p))
#    #plt.show
#    return

