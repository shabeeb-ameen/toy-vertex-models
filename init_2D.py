import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc
from classes import Vertex, Edge, Polygon, Polyhedron
from functions import *


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
#Edge assignments. The state variable is null by default. After the transition, use state="post" for the new edge assignments 
def edge_assignments(p_0,q_0, state=None):
    p=copy.deepcopy(p_0)
    q=copy.deepcopy(q_0)
    if state==None:
        edges_1=[]
        edges_1.append(Edge(Vertex(p[0]),Vertex.reflector(p[0],"-+")))
        edges_1.append(Edge(Vertex(p[0]),Vertex(p[1])))
        edges_1.append(Edge(Vertex(p[1]),Vertex(p[2])))
        edges_1.append(Edge(Vertex(p[2]),Vertex.reflector(p[2],"-+")))
        edges_1.append(Edge(Vertex.reflector(p[1],"-+"),Vertex.reflector(p[2],"-+")))
        edges_1.append(Edge(Vertex.reflector(p[1],"-+"),Vertex.reflector(p[0],"-+")))
        
        edges_2=[]
        edges_2.append(Edge(Vertex(p[0]),Vertex(p[1])))
        edges_2.append(Edge(Vertex(p[1]),Vertex(q[0])))
        edges_2.append(Edge(Vertex(q[0]),Vertex(q[1])))
        edges_2.append(Edge(Vertex(q[1]),Vertex.reflector(q[0],"+-")))
        edges_2.append(Edge(Vertex.reflector(p[1],"+-"),Vertex.reflector(q[0],"+-")))
        edges_2.append(Edge(Vertex.reflector(p[1],"+-"),Vertex(p[0])))

        edges_3=[]
        edges_3.append(Edge(Vertex.reflector(p[0],"+-"),Vertex.reflector(p[0],"--")))
        edges_3.append(Edge(Vertex.reflector(p[0],"+-"),Vertex.reflector(p[1],"+-")))
        edges_3.append(Edge(Vertex.reflector(p[1],"+-"),Vertex.reflector(p[2],"+-")))
        edges_3.append(Edge(Vertex.reflector(p[2],"+-"),Vertex.reflector(p[2],"--")))
        edges_3.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(p[2],"--")))
        edges_3.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(p[0],"--")))

        edges_4=[]
        edges_4.append(Edge(Vertex.reflector(p[0],"-+"),Vertex.reflector(p[1],"-+")))
        edges_4.append(Edge(Vertex.reflector(p[1],"-+"),Vertex.reflector(q[0],"-+")))
        edges_4.append(Edge(Vertex.reflector(q[0],"-+"),Vertex.reflector(q[1],"-+")))
        edges_4.append(Edge(Vertex.reflector(q[1],"-+"),Vertex.reflector(q[0],"--")))
        edges_4.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(q[0],"--")))
        edges_4.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(p[0],"-+")))

    if state=="post":
        edges_1=[]
        
        edges_1.append(Edge(Vertex(p[0]),Vertex(p[1])))
        edges_1.append(Edge(Vertex(p[1]),Vertex(p[2])))
        edges_1.append(Edge(Vertex(p[2]),Vertex.reflector(p[2],"-+")))
        edges_1.append(Edge(Vertex.reflector(p[1],"-+"),Vertex.reflector(p[2],"-+")))
        edges_1.append(Edge(Vertex.reflector(p[1],"-+"),Vertex.reflector(p[0],"-+")))
        
        edges_2=[]
        edges_2.append(Edge(Vertex(p[0]),Vertex(p[1])))
        edges_2.append(Edge(Vertex(p[1]),Vertex(q[0])))
        edges_2.append(Edge(Vertex(q[0]),Vertex(q[1])))
        edges_2.append(Edge(Vertex(q[1]),Vertex.reflector(q[0],"+-")))
        edges_2.append(Edge(Vertex.reflector(p[1],"+-"),Vertex.reflector(q[0],"+-")))
        edges_2.append(Edge(Vertex.reflector(p[1],"+-"),Vertex.reflector(p[0],"+-")))
        edges_2.append(Edge(Vertex(p[0]),Vertex.reflector(p[0],"+-")))


        edges_3=[]
        
        edges_3.append(Edge(Vertex.reflector(p[0],"+-"),Vertex.reflector(p[1],"+-")))
        edges_3.append(Edge(Vertex.reflector(p[1],"+-"),Vertex.reflector(p[2],"+-")))
        edges_3.append(Edge(Vertex.reflector(p[2],"+-"),Vertex.reflector(p[2],"--")))
        edges_3.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(p[2],"--")))
        edges_3.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(p[0],"--")))

        edges_4=[]
        edges_4.append(Edge(Vertex.reflector(p[0],"-+"),Vertex.reflector(p[1],"-+")))
        edges_4.append(Edge(Vertex.reflector(p[1],"-+"),Vertex.reflector(q[0],"-+")))
        edges_4.append(Edge(Vertex.reflector(q[0],"-+"),Vertex.reflector(q[1],"-+")))
        edges_4.append(Edge(Vertex.reflector(q[1],"-+"),Vertex.reflector(q[0],"--")))
        edges_4.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(q[0],"--")))
        edges_4.append(Edge(Vertex.reflector(p[1],"--"),Vertex.reflector(p[0],"--")))
        edges_4.append(Edge(Vertex(p[0]),Vertex.reflector(p[0],"+-")))



    return edges_1,edges_2,edges_3,edges_4

def polygon_assignments(p,q, state=None):

    e1,e2,e3,e4=edge_assignments(p,q,state)

    polys=[Polygon(e1),Polygon(e2),Polygon(e3),Polygon(e4)]
    return polys


cos_30=3**(1/2)/2
l=1
p=[]

p.append([l/2,0])
p.append([l,l*cos_30])
p.append([l/2,2*l*cos_30])

q=[]
q.append([2*l,l*cos_30])
q.append([5*l/2,0])

fig1=plt.figure()
plt.scatter(*zip(*p))
plt.scatter(*zip(*q))
plt.xlim(0,3*l)
plt.text(l/2,0,"  p_0")
plt.text(l,l*cos_30,"  p_1")
plt.text(l/2,2*l*cos_30,"  p_2")
plt.text(2*l,l*cos_30,"  q_0")
plt.text(5*l/2,0,"  q_1")

plt.savefig("Figures/2D/2D_generator_points.png",dpi=1080,bbox_inches="tight",transparent=False)
plt.close(fig1)

fig2=plt.figure()
plotter_2D(np.concatenate(edge_assignments(p,q),axis=0))
plt.savefig("Figures/2D/Initial_Configuration_2D.png",dpi=1080,bbox_inches="tight",transparent=False)
plt.close(fig2)