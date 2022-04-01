import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mcr
from classes import Vertex, Edge, Polygon

## initialize vertex objects for the 2D fourcell honeycomb:


cos_30=3**(1/2)/2
l=1

## Just a note: these points and their various reflections make up the four cells
#p=[]
#p.append([l/2,0])
#p.append([l,l*cos_30])
#p.append([l/2,2*l*cos_30])
#p.append([2*l,l*cos_30])
#p.append([5*l/2,0])



verts=[]


#Cell 0
verts.append(Vertex([l/2,0]))
verts.append(Vertex([-l/2,0]))
verts.append(Vertex([-l,l*cos_30]))
verts.append(Vertex([-l/2,2*l*cos_30]))
verts.append(Vertex([l/2,2*l*cos_30]))
verts.append(Vertex([l,l*cos_30]))



#Cell 1
verts.append(Vertex([2*l,l*cos_30]))
verts.append(Vertex([5*l/2,0]))
verts.append(Vertex([2*l,-l*cos_30]))
verts.append(Vertex([l,-l*cos_30]))



#Cell 2
verts.append(Vertex([l/2,-2*l*cos_30]))
verts.append(Vertex([-l/2,-2*l*cos_30]))
verts.append(Vertex([-l,-l*cos_30]))


#Cell 3
verts.append(Vertex([-2*l,-l*cos_30]))
verts.append(Vertex([-5*l/2,0]))
verts.append(Vertex([-2*l,l*cos_30]))


