import numpy as np
import scipy.spatial
import copy
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections  as mc


## Usage guide: initialize vertex instances with Vertex([x,y]) or Vertex([x,y,z])


## Use the reflector as an alternate constructor to implement reflection symmetries from generator points.

## Further development idea: maybe the edge, polygon and polyhedron classes should also have such alternate constructors!


class Vertex:
    num_vertices=0

    def __init__(self, coordinates):
        self.coordinates=coordinates
        Vertex.num_vertices+=1

    @classmethod
    def reflector(cls, arr, axis=None):
        array=copy.deepcopy(arr)
        #Identity Mapping:
        if axis==None:
            return cls(array)
        #2D reflectors:
        if axis=="++":
            return cls(array)
        if axis=="+-":
            array[1]*=-1
            return cls(array)
        if axis=="-+":
            array[0]*=-1
            return cls(array)
        if axis=="--":
            array[0]*=-1
            array[1]*=-1
            return cls(array)
        #3D reflectors:
        if axis=="+++":
            return cls(array)
        if axis=="++-":
            array[2]*=-1
            return cls(array)
        if axis=="+-+":
            array[1]*=-1
            return cls(array)
        if axis=="+--":
            array[2]*=-1
            array[1]*=-1
            return cls(array)
        
        if axis=="-++":
            array[0]*=-1
            return cls(array)

        if axis=="-+-":
            array[2]*=-1
            array[0]*=-1
        if axis=="--+":
            array[1]*=-1
            array[0]*=-1   
            return cls(array)
        if axis=="---":
            array[2]*=-1
            array[1]*=-1
            array[0]*=-1   
            return cls(array)
                
## Usage guide: create edge instances with vertex objects 
## ... don't put them in a list; eg if v1,v2 are connected vertex objects, 
## e1=Edge(v1,v2) makes the edge object.

## Note: e1=Edge(v2,v1) would also work! For this problem, this ambiguity doesnt matter. 
## its just a choice we can make while inputting the data.

class Edge:
    num_edges=0
    def __init__(self, vertices):
        self.vertices=vertices
        Edge.num_edges+=1
    def length(self):
        return scipy.spatial.distance.euclidean(self.vertices[0].coordinates,self.vertices[1].coordinates)
    def edge_center(self):
        return np.mean([self.vertices[0].coordinates,self.vertices[1].coordinates],axis=0)

    
    
## Usage guide: Initialization with Polygon([<list of edge objects>])
# Warning: in order to use the energy function, you need to initialize the parameters! 
class Polygon:
    num_polygons=0
    p_0=None
    a_0=None
    k_a=None
    
    def __init__(self,edges):

        self.edges=edges
        #self.edge_centers=[e.edge_center for e in self.edges]
        #self.polygon_center=np.mean([e.edge_center() for e in self.edges],axis=0)
        Polygon.num_polygons+=1
    
    def polygon_center(self):
        return np.mean([e.edge_center() for e in self.edges],axis=0)
    def perimeter(self):
        return np.sum([e.length() for e in self.edges])

    def area(self):
        ## Key idea: the area of a convex polygon is broken up into triangles. 
        ## Each triangle is made up of one edge and two lines to the center.
        area=0
        for edge in self.edges:

            v1=np.subtract(edge.vertices[0].coordinates,self.polygon_center())
            v2=np.subtract(edge.vertices[1].coordinates,self.polygon_center())
            area+=np.linalg.norm(np.cross(v1,v2))/2
        return area
    

    def energy(self):
        energy=0
        energy+= Polygon.k_a*(self.area()/Polygon.a_0-1)**2
        energy+= (self.perimeter()/(Polygon.a_0)**(1/2)-Polygon.p_0)**2
        return energy

## Usage guide: Initialization with Polygon([<list of edge objects>])

## Warning: in order to use the energy function, you need to initialize the s_0, v_0, k_v parameters! 
class Polyhedron:
    num_polyhedrons=0

    s_0=None
    v_0=None
    k_v=None

    def __init__(self,polygons):
        self.polygons=polygons
        self.v_0=None
    
        #self.polyhedron_center=np.mean([poly.polygon_center() for poly in self.polygons],axis=0)
        Polyhedron.num_polyhedrons+=1

    ## this is not necessarily the center of mass of the polyhedron, its just a convenient inside-point
    def polyhedron_center(self):
        return np.mean([poly.polygon_center() for poly in self.polygons],axis=0)
    def surface_area(self):
        return np.sum([poly.area() for poly in self.polygons])

    ## The volume function works by reaking up the cells into tetrahedra (edge,polygon center, polyhedron center.    
    def volume(self):
        volume=0
        c=np.append(self.polyhedron_center(),1)
        for poly in self.polygons:
            d=np.append(poly.polygon_center(),1)
            for edge in poly.edges:
                e_1=np.append(edge.vertices[0].coordinates,1)
                e_2=np.append(edge.vertices[1].coordinates,1)
                volume+=abs(np.linalg.det([c,d,e_1,e_2]))/6
        return volume

    #def energy(self):
    #    #dimensionless volume, surface area
    #    dls_vol=self.volume()/Polyhedron.v_0
    #    dls_sa=self.surface_area()/(Polyhedron.v_0)**(2/3)
    #    energy=0
    #    energy+= Polyhedron.k_v*(dls_vol-1)**2
    #    energy+= (dls_sa-Polyhedron.s_0)**2
    #    return energy

    def volume_energy(self):
        #dimensionless volume, surface area
        dls_vol=self.volume()/self.v_0
        energy=Polyhedron.k_v*(dls_vol-1)**2
        #energy+= (dls_sa-Polyhedron.s_0)**2
        return energy
    def surface_energy(self):
        #dimensionless volume, surface area
        #dls_vol=self.volume()/self.v_0
        dls_sa=self.surface_area()/(self.v_0)**(2/3)
        energy=(dls_sa-Polyhedron.s_0)**2
        return energy
    def energy(self):
        return self.volume_energy()+self.surface_energy()
        #return self.volume_energy()
        #return self.surface_energy()