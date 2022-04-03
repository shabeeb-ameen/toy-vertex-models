import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc
from classes import Vertex, Edge, Polygon


# A function that returns randomized positions for generator points, which respect 
# (a) a specified orientation of the driven edge
# (b) symmetry


def gen_rnd_2D(l,p,q,epsilon,state=None):
    p_f=copy.deepcopy(p)
    q_f=copy.deepcopy(q)
    rng_p=2*epsilon*np.subtract(np.random.rand(len(p),len(p[0])),np.full((len(p),len(p[0])),1/2))
    rng_q=2*epsilon*np.subtract(np.random.rand(len(q),len(q[0])),np.full((len(q),len(q[0])),1/2))

    p_f=np.add(p_f,rng_p)
    q_f=np.add(q_f,rng_q)


    #some values need to be fixed to preserve symmetry:
    q_f[1][1]=0

    #finally, the driven point needs to be on axis:
    if state==None: p_f[0]=[l/2,0]
    if state=="post": p_f[0]=[0,l/2]
    return p_f,q_f

def gen_rnd_3D(l,p,q,epsilon,state=None):
    pass

    
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

def fourcell_vertex_scatter(verts):
    p=[v.coordinates for v in verts]
    plt.scatter(*zip(*p))
    #plt.show
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

