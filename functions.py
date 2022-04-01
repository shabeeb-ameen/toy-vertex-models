import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc
from classes import Vertex, Edge, Polygon




## Pre configuration edge and polygon assignments

def edge_assignments(verts):
    edges=[]
    edges.append(Edge(verts[0],verts[1]))
    edges.append(Edge(verts[1],verts[2]))
    edges.append(Edge(verts[2],verts[3]))
    edges.append(Edge(verts[3],verts[4]))
    edges.append(Edge(verts[4],verts[5]))
    edges.append(Edge(verts[5],verts[0]))

    edges.append(Edge(verts[5],verts[6]))
    edges.append(Edge(verts[6],verts[7]))
    edges.append(Edge(verts[7],verts[8]))
    edges.append(Edge(verts[8],verts[9]))
    edges.append(Edge(verts[9],verts[0]))

    edges.append(Edge(verts[9],verts[10]))
    edges.append(Edge(verts[10],verts[11]))
    edges.append(Edge(verts[11],verts[12]))
    edges.append(Edge(verts[12],verts[1]))

    
    edges.append(Edge(verts[12],verts[13]))
    edges.append(Edge(verts[13],verts[14]))
    edges.append(Edge(verts[14],verts[15]))
    edges.append(Edge(verts[15],verts[2]))

    return edges


def polygon_assignment(edges):
    polygons=[]
    polygons.append(Polygon([edges[0],edges[1],edges[2],edges[3],edges[4],edges[5]]))
    polygons.append(Polygon([edges[5],edges[6],edges[7],edges[8],edges[9],edges[10]]))
    polygons.append(Polygon([edges[0],edges[10],edges[11],edges[12],edges[13],edges[14]]))
    polygons.append(Polygon([edges[14],edges[15],edges[16],edges[17],edges[18],edges[1]]))
    return polygons


#plotting functions in two dimentsions


def fourcell_plotter(verts,edges):
    lines = [[e.vert_a.coordinates,e.vert_b.coordinates]for e in edges]
    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    p=[v.coordinates for v in verts]
    plt.scatter(*zip(*p))
    plt.show
    return

def fourcell_vertex_scatter(verts):
    p=[v.coordinates for v in verts]
    plt.scatter(*zip(*p))
    plt.show
    return



def vertex_randomizer(v,l,epsilon):
    verts=copy.deepcopy(v)
    d=len(verts[0].coordinates)
    random=np.random.rand(d,len(verts))
    
    verts[0].coordinates[0]=l/2
    verts[1].coordinates[0]=-l/2
    
    random=2*epsilon*np.random.rand(len(verts),d)-np.full((len(verts),d),epsilon)
    for i in range (2,len(verts)):
        verts[i].coordinates=np.add(verts[i].coordinates,random[i])

    return verts


def vertex_monte_carlo(verts,l,epsilon,trials):
    n=0
    verts_final=vertex_randomizer(verts,l,epsilon)
    edges_test=edge_assignments(verts_final)
    polygons_test=polygon_assignment(edges_test)
    
    energy=np.sum( [p.energy() for p in polygons_test])
    while n<trials:
        verts_test=vertex_randomizer(verts,l,epsilon)
    
    
        edges_test=edge_assignments(verts_test)
        polygons_test=polygon_assignment(edges_test)

        if np.sum([p.energy() for p in polygons_test])<energy:
            verts_final=copy.deepcopy(verts_test)
            energy=np.sum( [p.energy() for p in polygons_test])
        n+=1
    
    return verts_final