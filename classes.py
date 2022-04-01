import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc



class Vertex:
    num_vertices=0

    def __init__(self, coordinates):
        self.coordinates=coordinates
        Vertex.num_vertices+=1

    @classmethod
    def reflector(cls, array, axis):
        if axis=="x":
            array[1]*=-1
        if axis=="y":
            array[0]*=-1
        if axis=="xy":
            array[2]*=-1
        if axis=="xz":
            array[1]*=-1
        if axis=="yz":
            array[0]*=-1

        return cls(array)


class Edge:
    num_edges=0

    ## there is  ambiguity on which vertex is a or b. 
    # For this problem, it doesnt matter. its a choice we can make while inputting the data.
    def __init__(self, vert_a, vert_b):
        self.vert_a=vert_a
        self.vert_b=vert_b
        self.edge_width=scipy.spatial.distance.euclidean(self.vert_a.coordinates,self.vert_b.coordinates)
        self.edge_center=np.mean([self.vert_a.coordinates,self.vert_b.coordinates],axis=0)
        Edge.num_edges+=1
    def length(self):
        return scipy.spatial.distance.euclidean(self.vert_a.coordinates,self.vert_b.coordinates)
        
class Polygon:
    num_polygons=0
    def __init__(self,edges):

        self.edges=edges
        self.edge_centers=[e.edge_center for e in self.edges]
        self.polygon_center=np.mean(self.edge_centers,axis=0)
        Polygon.num_polygons+=1
        
    def perimeter(self):
        return np.sum([e.edge_width for e in self.edges])

    def area(self):
        ## Key idea: the area of a convex polygon is broken up into triangles. 
        ## Each triangle takes one vertex, the center of a corresponding edge, and the center of the polygon.
        ## hence, for example, a hexagon is broken up into 12 triangles.
        area=0
        for edge in self.edges:
            c1=np.append(edge.vert_a.coordinates, 1)
            c2=np.append(edge.edge_center,1)
            c3=np.append(self.polygon_center,1)
            area+=abs(np.linalg.det([c1,c2,c3]))/2
            d1=np.append(edge.vert_b.coordinates, 1)
            d2=np.append(edge.edge_center,1)
            d3=np.append(self.polygon_center,1)
            area+=abs(np.linalg.det([d1,d2,d3]))/2

        return area
    
    p_0=None
    a_0=None
    
    k_A=100

    def energy(self):
        energy=0
        energy+= Polygon.k_A*(self.area()/Polygon.a_0-1)**2
        energy+= (self.perimeter()/(Polygon.a_0)**(1/2)-Polygon.p_0)**2
        return energy
