import re
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
p.append([L/2,3*L/2,2*L/(2)**(1/2)])
p.append([3*L/2,L/2,2*L/(2)**(1/2)])
p.append([L,L,3*L/(2)**(1/2)])
p.append([L/2,L/2,4*L/(2)**(1/2)])


q=[]
q.append([5*L/2,L/2,2*L/(2)**(1/2)])
q.append([3*L,L,L/(2)**(1/2)])
q.append([5*L/2,3*L/2,0])
q.append([3*L/2,3*L/2,0])
q.append([7*L/2,L/2,0])


fig = plt.figure(figsize=(4,4), dpi=1080)
ax  = fig.add_subplot(111, projection = '3d')
ax.scatter(*zip(*p))
ax.scatter(*zip(*q))
ax.set_xlim3d(0,3*L)
ax.set_ylim3d(0,3*L)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.text(L/2,L/2,0, "  p_0",size=2, zorder=1)
ax.text(L,L,L/(2)**(1/2), "  p_1",size=2, zorder=1)
ax.text(L/2,3*L/2,2*L/(2)**(1/2), "  p_2",size=2, zorder=1)
ax.text(3*L/2,L/2,2*L/(2)**(1/2), "  p_3",size=2, zorder=1)
ax.text(L,L,3*L/(2)**(1/2), "  p_4",size=2, zorder=1)
ax.text(L/2,L/2,4*L/(2)**(1/2), "  p_5",size=2, zorder=1)
ax.text(5*L/2,L/2,2*L/(2)**(1/2), "  q_0",size=2, zorder=1)
ax.text(3*L,L,L/(2)**(1/2), "  q_1",size=2, zorder=1)
ax.text(5*L/2,3*L/2,0, "  q_2",size=2, zorder=1)
ax.text(3*L/2,3*L/2,0, "  q_3",size=2, zorder=1)
ax.text(7*L/2,L/2,0, "  q_4",size=2, zorder=1)
plt.savefig("Figures/3D/3D_generator_points.png",dpi=1080,bbox_inches="tight",transparent=False)
plt.close(fig)

#Edge assignments. The state variable is null by default. After the transition, use state="post" for the new edge assignments 
def edge_assignments_cell_1(p_0,q_0, state=None):
    p=copy.deepcopy(p_0)
    q=copy.deepcopy(q_0)
    if state==None:
        e1_f0=[]
        e1_f0.append(Edge(Vertex(p[0]),Vertex.reflector(p[0],"+-+")))
        e1_f0.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex.reflector(p[0],"--+")))
        e1_f0.append(Edge(Vertex.reflector(p[0],"--+"),Vertex.reflector(p[0],"-++")))
        e1_f0.append(Edge(Vertex.reflector(p[0],"-++"),Vertex(p[0])))


        e1_f1a=[]
        e1_f1a.append(Edge(Vertex(p[0]),Vertex.reflector(p[0],"-++")))
        e1_f1a.append(Edge(Vertex(p[0]),Vertex(p[1])))
        e1_f1a.append(Edge(Vertex(p[1]),Vertex(p[2])))
        e1_f1a.append(Edge(Vertex(p[2]),Vertex.reflector(p[2],"-++")))
        e1_f1a.append(Edge(Vertex.reflector(p[2],"-++"),Vertex.reflector(p[1],"-++")))
        e1_f1a.append(Edge(Vertex.reflector(p[1],"-++"),Vertex.reflector(p[0],"-++")))
  

        e1_f1b=[]#(,"-++")
        e1_f1b.append(Edge(Vertex.reflector(p[0],"-++"),Vertex.reflector(p[0],"--+")))
        e1_f1b.append(Edge(Vertex.reflector(p[0],"-++"),Vertex.reflector(p[1],"-++")))
        e1_f1b.append(Edge(Vertex.reflector(p[1],"-++"),Vertex.reflector(p[3],"-++")))
        e1_f1b.append(Edge(Vertex.reflector(p[3],"-++"),Vertex.reflector(p[3],"--+")))
        e1_f1b.append(Edge(Vertex.reflector(p[3],"--+"),Vertex.reflector(p[1],"--+")))
        e1_f1b.append(Edge(Vertex.reflector(p[1],"--+"),Vertex.reflector(p[0],"--+")))
        
        
        e1_f1c=[]#(,"+-+")
        e1_f1c.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex.reflector(p[0],"--+")))
        e1_f1c.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex.reflector(p[1],"+-+")))
        e1_f1c.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(p[2],"+-+")))
        e1_f1c.append(Edge(Vertex.reflector(p[2],"+-+"),Vertex.reflector(p[2],"--+")))
        e1_f1c.append(Edge(Vertex.reflector(p[2],"--+"),Vertex.reflector(p[1],"--+")))
        e1_f1c.append(Edge(Vertex.reflector(p[1],"--+"),Vertex.reflector(p[0],"--+")))
        
        e1_f1d=[]
        e1_f1d.append(Edge(Vertex(p[0]),Vertex(p[1])))
        e1_f1d.append(Edge(Vertex(p[1]),Vertex(p[3])))
        e1_f1d.append(Edge(Vertex(p[3]),Vertex.reflector(p[3],"+-+")))
        e1_f1d.append(Edge(Vertex.reflector(p[3],"+-+"),Vertex.reflector(p[1],"+-+")))
        e1_f1d.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(p[0],"+-+")))
        e1_f1d.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex(p[0])))
        #e1_f1d.append(Edge(Vertex.reflector(p[1],"-++"),Vertex.reflector(p[3],"-++")))
        ##e1_f1d.append(Edge(Vertex.reflector(p[3],"-++"),Vertex.reflector(p[3],"--+")))
        #e1_f1d.append(Edge(Vertex.reflector(p[3],"--+"),Vertex.reflector(p[1],"--+")))
        #e1_f1d.append(Edge(Vertex.reflector(p[1],"--+"),Vertex.reflector(p[0],"--+")))
        
        
        e1_f2a=[]
        e1_f2a.append(Edge(Vertex(p[1]),Vertex(p[2])))
        e1_f2a.append(Edge(Vertex(p[1]),Vertex(p[3])))
        e1_f2a.append(Edge(Vertex(p[4]),Vertex(p[3])))
        e1_f2a.append(Edge(Vertex(p[4]),Vertex(p[2])))

        e1_f2b=[]
        e1_f2b.append(Edge(Vertex.reflector(p[1],"-++"),Vertex.reflector(p[2],"-++")))
        e1_f2b.append(Edge(Vertex.reflector(p[1],"-++"),Vertex.reflector(p[3],"-++")))
        e1_f2b.append(Edge(Vertex.reflector(p[4],"-++"),Vertex.reflector(p[3],"-++")))
        e1_f2b.append(Edge(Vertex.reflector(p[4],"-++"),Vertex.reflector(p[2],"-++")))

        e1_f2c=[]
        e1_f2c.append(Edge(Vertex.reflector(p[1],"--+"),Vertex.reflector(p[2],"--+")))
        e1_f2c.append(Edge(Vertex.reflector(p[1],"--+"),Vertex.reflector(p[3],"--+")))
        e1_f2c.append(Edge(Vertex.reflector(p[4],"--+"),Vertex.reflector(p[3],"--+")))
        e1_f2c.append(Edge(Vertex.reflector(p[4],"--+"),Vertex.reflector(p[2],"--+")))
        
        
        e1_f2d=[]
        e1_f2d.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(p[2],"+-+")))
        e1_f2d.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(p[3],"+-+")))
        e1_f2d.append(Edge(Vertex.reflector(p[4],"+-+"),Vertex.reflector(p[3],"+-+")))
        e1_f2d.append(Edge(Vertex.reflector(p[4],"+-+"),Vertex.reflector(p[2],"+-+")))

        e1_f3a=[]
        e1_f3a.append(Edge(Vertex(p[2]),Vertex(p[4])))
        e1_f3a.append(Edge(Vertex(p[4]),Vertex(p[5])))
        e1_f3a.append(Edge(Vertex(p[5]),Vertex.reflector(p[5],"-++")))
        e1_f3a.append(Edge(Vertex.reflector(p[5],"-++"),Vertex.reflector(p[4],"-++")))
        e1_f3a.append(Edge(Vertex.reflector(p[4],"-++"),Vertex.reflector(p[2],"-++")))
        e1_f3a.append(Edge(Vertex(p[2]),Vertex.reflector(p[2],"-++")))

        e1_f3b=[]
        e1_f3b.append(Edge(Vertex.reflector(p[3],"-++"),Vertex.reflector(p[4],"-++")))
        e1_f3b.append(Edge(Vertex.reflector(p[4],"-++"),Vertex.reflector(p[5],"-++")))
        e1_f3b.append(Edge(Vertex.reflector(p[5],"-++"),Vertex.reflector(p[5],"--+")))
        e1_f3b.append(Edge(Vertex.reflector(p[5],"--+"),Vertex.reflector(p[4],"--+")))
        e1_f3b.append(Edge(Vertex.reflector(p[4],"--+"),Vertex.reflector(p[3],"--+")))
        e1_f3b.append(Edge(Vertex.reflector(p[3],"--+"),Vertex.reflector(p[3],"-++")))
        
        e1_f3c=[]
        e1_f3c.append(Edge(Vertex.reflector(p[2],"+-+"),Vertex.reflector(p[4],"+-+")))
        e1_f3c.append(Edge(Vertex.reflector(p[4],"+-+"),Vertex.reflector(p[5],"+-+")))
        e1_f3c.append(Edge(Vertex.reflector(p[5],"+-+"),Vertex.reflector(p[5],"--+")))
        e1_f3c.append(Edge(Vertex.reflector(p[5],"--+"),Vertex.reflector(p[4],"--+")))
        e1_f3c.append(Edge(Vertex.reflector(p[4],"--+"),Vertex.reflector(p[2],"--+")))
        e1_f3c.append(Edge(Vertex.reflector(p[2],"+-+"),Vertex.reflector(p[2],"--+")))

        e1_f3d=[]
        e1_f3d.append(Edge(Vertex(p[3]),Vertex(p[4])))
        e1_f3d.append(Edge(Vertex(p[4]),Vertex(p[5])))
        e1_f3d.append(Edge(Vertex(p[5]),Vertex.reflector(p[5],"+-+")))
        e1_f3d.append(Edge(Vertex.reflector(p[5],"+-+"),Vertex.reflector(p[4],"+-+")))
        e1_f3d.append(Edge(Vertex.reflector(p[4],"+-+"),Vertex.reflector(p[3],"+-+")))
        e1_f3d.append(Edge(Vertex.reflector(p[3],"+-+"),Vertex(p[3])))

        e1_f4=[]
        e1_f4.append(Edge(Vertex(p[5]),Vertex.reflector(p[5],"+-+")))
        e1_f4.append(Edge(Vertex.reflector(p[5],"+-+"),Vertex.reflector(p[5],"--+")))
        e1_f4.append(Edge(Vertex.reflector(p[5],"--+"),Vertex.reflector(p[5],"-++")))
        e1_f4.append(Edge(Vertex.reflector(p[5],"-++"),Vertex(p[5])))
    return e1_f0,e1_f1a,e1_f1b,e1_f1c,e1_f1d,e1_f2a, e1_f2b, e1_f2c, e1_f2d, e1_f3a,e1_f3b, e1_f3c, e1_f3d, e1_f4


def edge_assignments_cell_2(p_0,q_0, state=None):
    p=copy.deepcopy(p_0)
    q=copy.deepcopy(q_0)
    if state==None:
        e2_f0=[]
        e2_f0.append(Edge(Vertex(p[3]),Vertex(q[0])))
        e2_f0.append(Edge(Vertex(q[0]),Vertex.reflector(q[0],"+-+")))
        e2_f0.append(Edge(Vertex.reflector(q[0],"+-+"),Vertex.reflector(p[3],"+-+")))
        e2_f0.append(Edge(Vertex.reflector(p[3],"+-+"),Vertex(p[3])))

        #e1_f0.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex.reflector(p[0],"--+")))
        #e1_f0.append(Edge(Vertex.reflector(p[0],"--+"),Vertex.reflector(p[0],"-++")))
        #e1_f0.append(Edge(Vertex.reflector(p[0],"-++"),Vertex(p[0])))
        #e1_f1a=[]
        
        e2_f1a=[]
        e2_f1a.append(Edge(Vertex(p[3]),Vertex(q[0])))
        e2_f1a.append(Edge(Vertex(q[0]),Vertex(q[1])))
        e2_f1a.append(Edge(Vertex(q[1]),Vertex(q[2])))
        e2_f1a.append(Edge(Vertex(q[2]),Vertex(q[3])))
        e2_f1a.append(Edge(Vertex(q[3]),Vertex(p[1])))
        e2_f1a.append(Edge(Vertex(p[1]),Vertex(p[3])))

        

        e2_f1b=[]
        e2_f1b.append(Edge(Vertex(p[0]),Vertex(p[1])))
        e2_f1b.append(Edge(Vertex(p[1]),Vertex(p[3])))
        e2_f1b.append(Edge(Vertex(p[3]),Vertex.reflector(p[3],"+-+")))
        e2_f1b.append(Edge(Vertex.reflector(p[3],"+-+"),Vertex.reflector(p[1],"+-+")))
        e2_f1b.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(p[0],"+-+")))
        e2_f1b.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex(p[0])))

        e2_f1c=[]
        e2_f1c.append(Edge(Vertex.reflector(p[3],"+-+"),Vertex.reflector(q[0],"+-+")))
        e2_f1c.append(Edge(Vertex.reflector(q[0],"+-+"),Vertex.reflector(q[1],"+-+")))
        e2_f1c.append(Edge(Vertex.reflector(q[1],"+-+"),Vertex.reflector(q[2],"+-+")))
        e2_f1c.append(Edge(Vertex.reflector(q[2],"+-+"),Vertex.reflector(q[3],"+-+")))
        e2_f1c.append(Edge(Vertex.reflector(q[3],"+-+"),Vertex.reflector(p[1],"+-+")))
        e2_f1c.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(p[3],"+-+")))

        e2_f1d=[]
        e2_f1d.append(Edge(Vertex(q[0]),Vertex(q[1])))
        e2_f1d.append(Edge(Vertex(q[1]),Vertex(q[4])))
        e2_f1d.append(Edge(Vertex(q[4]),Vertex.reflector(q[4],"+-+")))
        e2_f1d.append(Edge(Vertex.reflector(q[4],"+-+"),Vertex.reflector(q[1],"+-+")))
        e2_f1d.append(Edge(Vertex.reflector(q[1],"+-+"),Vertex.reflector(q[0],"+-+")))
        e2_f1d.append(Edge(Vertex.reflector(q[0],"+-+"),Vertex(q[0])))

       
        e2_f2a=[]
        e2_f2a.append(Edge(Vertex(q[4]),Vertex(q[1])))
        e2_f2a.append(Edge(Vertex(q[1]),Vertex(q[2])))
        e2_f2a.append(Edge(Vertex(q[2]),Vertex.reflector(q[1],"++-")))
        e2_f2a.append(Edge(Vertex.reflector(q[1],"++-"),Vertex(q[4])))
        
        e2_f2b=[]
        e2_f2b.append(Edge(Vertex(p[0]),Vertex(p[1])))
        e2_f2b.append(Edge(Vertex(p[1]),Vertex(q[3])))
        e2_f2b.append(Edge(Vertex(q[3]),Vertex.reflector(p[1],"++-")))
        e2_f2b.append(Edge(Vertex.reflector(p[1],"++-"),Vertex(p[0])))
        
        e2_f2c=[]
        
        e2_f2c.append(Edge(Vertex.reflector(p[0],"+-+"),Vertex.reflector(p[1],"+-+")))
        e2_f2c.append(Edge(Vertex.reflector(p[1],"+-+"),Vertex.reflector(q[3],"+-+")))
        e2_f2c.append(Edge(Vertex.reflector(q[3],"+-+"),Vertex.reflector(p[1],"+--")))
        e2_f2c.append(Edge(Vertex.reflector(p[1],"+--"),Vertex.reflector(p[0],"+-+")))
        
        e2_f2d=[]              
        e2_f2d.append(Edge(Vertex.reflector(q[4],"+-+"),Vertex.reflector(q[1],"+-+")))
        e2_f2d.append(Edge(Vertex.reflector(q[1],"+-+"),Vertex.reflector(q[2],"+-+")))
        e2_f2d.append(Edge(Vertex.reflector(q[2],"+-+"),Vertex.reflector(q[1],"+--")))
        e2_f2d.append(Edge(Vertex.reflector(q[1],"+--"),Vertex.reflector(q[4],"+-+")))

        e2_f3a=[]
        e2_f3a.append(Edge(Vertex(q[2]),Vertex(q[3])))
        e2_f3a.append(Edge(Vertex(q[3]),Vertex.reflector(p[1],"++-")))
        e2_f3a.append(Edge(Vertex.reflector(p[1],"++-"),Vertex.reflector(p[3],"++-")))
        e2_f3a.append(Edge(Vertex.reflector(p[3],"++-"),Vertex.reflector(q[0],"++-")))
        e2_f3a.append(Edge(Vertex.reflector(q[0],"++-"),Vertex.reflector(q[1],"++-")))
        e2_f3a.append(Edge(Vertex.reflector(q[1],"++-"),Vertex(q[2])))
        
        


        e2_f3b=[]
        e2_f3b.append(Edge(Vertex(p[0]),Vertex.reflector(p[1],"++-")))
        e2_f3b.append(Edge(Vertex.reflector(p[1],"++-"),Vertex.reflector(p[3],"++-")))
        e2_f3b.append(Edge(Vertex.reflector(p[3],"++-"),Vertex.reflector(p[3],"+--")))
        e2_f3b.append(Edge(Vertex.reflector(p[3],"+--"),Vertex.reflector(p[1],"+--")))
        e2_f3b.append(Edge(Vertex.reflector(p[1],"+--"),Vertex.reflector(p[0],"+--")))
        e2_f3b.append(Edge(Vertex.reflector(p[0],"+--"),Vertex(p[0])))

        e2_f3c=[]
   
        e2_f3c.append(Edge(Vertex.reflector(p[3],"+--"),Vertex.reflector(q[0],"+--")))
        e2_f3c.append(Edge(Vertex.reflector(q[0],"+--"),Vertex.reflector(q[1],"+--")))
        e2_f3c.append(Edge(Vertex.reflector(q[1],"+--"),Vertex.reflector(q[2],"+--")))
        e2_f3c.append(Edge(Vertex.reflector(q[2],"+--"),Vertex.reflector(q[3],"+--")))
        e2_f3c.append(Edge(Vertex.reflector(q[3],"+--"),Vertex.reflector(p[1],"+--")))
        e2_f3c.append(Edge(Vertex.reflector(p[1],"+--"),Vertex.reflector(p[3],"+--")))

        e2_f3d=[]

        e2_f3d.append(Edge(Vertex.reflector(q[0],"++-"),Vertex.reflector(q[1],"++-")))
        e2_f3d.append(Edge(Vertex.reflector(q[1],"++-"),Vertex(q[4])))
        e2_f3d.append(Edge(Vertex(q[4]),Vertex.reflector(q[4],"+-+")))
        e2_f3d.append(Edge(Vertex.reflector(q[4],"+-+"),Vertex.reflector(q[1],"+--")))
        e2_f3d.append(Edge(Vertex.reflector(q[1],"+--"),Vertex.reflector(q[0],"+--")))
        e2_f3d.append(Edge(Vertex.reflector(q[0],"+--"),Vertex.reflector(q[0],"++-")))


        e2_f4=[]
        e2_f4.append(Edge(Vertex.reflector(p[3],"++-"),Vertex.reflector(q[0],"++-")))
        e2_f4.append(Edge(Vertex.reflector(q[0],"++-"),Vertex.reflector(q[0],"+--")))
        e2_f4.append(Edge(Vertex.reflector(q[0],"+--"),Vertex.reflector(p[3],"+--")))
        e2_f4.append(Edge(Vertex.reflector(p[3],"+--"),Vertex.reflector(p[3],"++-")))

    return e2_f0,e2_f1a,e2_f1b,e2_f1c,e2_f1d,e2_f2a, e2_f2b, e2_f2c, e2_f2d, e2_f3a,e2_f3b, e2_f3c, e2_f3d, e2_f4






def polygon_assignments_cell_1(p,q, state=None):
    polys=[]
    for e in edge_assignments_cell_1(p,q,state):
        polys.append(Polygon(e))
    return polys

def polygon_assignments_cell_2(p,q, state=None):
    polys=[]
    for e in edge_assignments_cell_2(p,q,state):
        polys.append(Polygon(e))
    return polys
        


def polyhedron_assignments (p,q, state=None):
    phdrons=[]
    phdrons.append(Polyhedron(polygon_assignments_cell_1(p,q,state)))
    phdrons.append(Polyhedron(polygon_assignments_cell_2(p,q,state)))
    return phdrons
    

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

