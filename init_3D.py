from tkinter import E
import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc
from classes import Vertex, Edge, Polygon, Polyhedron
from functions import *

L=1

p=[]
p.append([L/2,L/2,0])
p.append([L,L,L/(2)**(1/2)])
p.append([3*L/2,L/2,2*L/(2)**(1/2)])
p.append([L,L,3*L/(2)**(1/2)])
p.append([L/2,L/2,4*L/(2)**(1/2)])
p.append([L/2,3*L/2,2*L/(2)**(1/2)])

q=[]
q.append([3*L/2,3*L/2,0])
q.append([L,L,-L/(2)**(1/2)])
q.append([3*L/2,5*L/2,0])
q.append([L,3*L,L/(2)**(1/2)])
q.append([L,3*L,-L/(2)**(1/2)])
q.append([L/2,5*L/2,2*L/(2)**(1/2)])
q.append([L/2,3*L/2,-2*L/(2)**(1/2)])
q.append([L/2,5*L/2,-2*L/(2)**(1/2)])
q.append([L/2,7*L/2,0])

#Edge assignments. The state variable is null by default. After the transition, use state="post" for the new edge assignments 
def edge_assignments_3D(p_0,q_0, state=None):
    p=copy.deepcopy(p_0)
    q=copy.deepcopy(q_0)
    if state==None:
        e1_f1=[]
        e1_f1.append(Edge(Vertex(p[0]),Vertex.reflector(p[0],"+-+")))
        e1_f1.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex.reflector(p[0],"--+")))
        e1_f1.append(Edge(Vertex.reflector(p[0],"--+"),Vertex.reflector(p[0],"-++")))
        e1_f1.append(Edge(Vertex.reflector(p[0],"-++"),Vertex(p[0])))
        return e1_f1

def polygon_assignments_3D(p_0,q_0, state=None):
    pass

def polyhedron_assignments (p_0,q_0, state=None):
    pass

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
    #plt.show()
    return

fig = plt.figure(figsize=(4,4), dpi=1080)
ax  = fig.add_subplot(111, projection = '3d')
ax.scatter(*zip(*p))
#ax.scatter(*zip(*q))
ax.set_xlim3d(0,2*L)
ax.set_ylim3d(0,2*L)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.text(L/2,L/2,0, "  p_0",size=2, zorder=1)
ax.text(L,L,L/(2)**(1/2), "  p_1",size=2, zorder=1)

ax.text(3*L/2,L/2,2*L/(2)**(1/2), "  p_2",size=2, zorder=1)

ax.text(L,L,3*L/(2)**(1/2), "  p_3",size=2, zorder=1)

ax.text(L/2,L/2,4*L/(2)**(1/2), "  p_4",size=2, zorder=1)
ax.text(L/2,3*L/2,2*L/(2)**(1/2), "  p_5",size=2, zorder=1)



#ax.set_zlim=(0,3*L)
plt.show()
