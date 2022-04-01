import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc


## Usage guide: create vertex instances with coordinates in the form [x,y] or [x,y,z] 


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

## Usage guide: create edge instances with vertex objects 
## ... don't put them in a list; eg if v1,v2 are connected vertex objects, 
## e1=Edge(v1,v2) makes the edge object.
## Note: e1=Edge(v2,v1) would also work! For this problem, it doesnt matter. its a choice we can make while inputting the data.
class Edge:
    num_edges=0
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
    p_0=None
    a_0=None
    k_a=None
    
    def __init__(self,edges):

        self.edges=edges
        #self.edge_centers=[e.edge_center for e in self.edges]
        self.polygon_center=np.mean([e.edge_center for e in self.edges],axis=0)
        Polygon.num_polygons+=1
        
    def perimeter(self):
        return np.sum([e.length() for e in self.edges])

    def area(self):
        ## Key idea: the area of a convex polygon is broken up into triangles. 
        ## Each triangle is made up of one edge and two lines to the center.
        area=0
        for edge in self.edges:

            v1=np.subtract(edge.vert_a.coordinates,self.polygon_center)
            v2=np.subtract(edge.vert_b.coordinates,self.polygon_center)
            area+=np.linalg.norm(np.cross(v1,v2))/2
        return area
    

    def energy(self):
        energy=0
        energy+= Polygon.k_a*(self.area()/Polygon.a_0-1)**2
        energy+= (self.perimeter()/(Polygon.a_0)**(1/2)-Polygon.p_0)**2
        return energy


class Polyhedron:
    num_polyhedrons=0
    def __init__(self,polygons):
        self.polygons=polygons

        ## this is not necessarily the center of mass of the polyhedron, its just a convenient inside-point
        self.polyhedron_center=np.mean([poly.polygon_center for poly in self.polygons],axis=0)
    
    def surface_area(self):
        return np.sum([poly.area for poly in self.polygons])

    ## The volume function breaks up the cocave hulls int    
    def volume(self):
        volume=0
        c=np.append(self.polyhedron_center,1)
        for poly in self.polygons:
            d=np.append(poly.polygon_center,1)
            for edge in poly.edges:
                e_1=np.append(edge.vert_a.coordinates,1)
                e_2=np.append(edge.vert_b.coordinates,1)
                volume+=abs(np.linalg.det([c,d,e_1,e_2]))/6
        return volume
   