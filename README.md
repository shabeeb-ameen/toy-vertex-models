#############
Introduction:
#############

The geometrical configuration of a valid vertex model requires (i) spatial coordinates for all vertices, and(ii) edge connections between them. A slight overspecification, where the edges, and in 3D the polygonal surfaces constituing each cell is also specified, is helpful for calculating energy functionals. Here we take an object-oriented approach to describing minimal vertex models and calculate energy profiles for neighbor exchanges in these models.

#########################
Basic Layout of the code:
#########################

1. Contents of classes.py:

(The classes in this file were designed to be modular and can be used for both 2D and 3D models, even outside the scope of the current work.)


(a) Vertex: These only serve as containers for vertex spatial coordinates; which can be 2D or 3D (but must be Cartesian!). The vertex class has a useful alternate constructor: the reflector. This is helpful if the model has mirror symmeries upon choice of axes.
(b) Edge: For every two vertices that are connected, we generate a single edge class. Attributes in this class include an edge spatial center and length.
(c) Polygon: One useful overspecification. The polygon objects store the edges that make up a given polygon. 
The polygon class has 
(d) Polyhedron: A further useful overrepresentation for 3D, storing the polygons that make up a given cell surface. Contains the following three parameters (i)shape parameter s_0 (ii) volume stiffness constant k_v, (iii)target volume v_0. These are again to be initialized before the evaluation of the included energy functional.


Further basic usage guides for these classes are commented on the code in classes.py

2. Contents of functions.py

Contains useful functions for, e.g visualization tools (plotting,gif making), debugging tools etc. Right now it mainly has plotting functions and some test scripts. I plan develop this further. The guiding philosophy is to keep functions.py modular

3. init_2D.py, 2D_toy_model.ipynb, init_3D.py, 3d_toy_model.ipynb:

The code here is project-specific. Contains project-specific routines (eg the "monte carlo routine"), initializations (e.g generator points and randomizers) and lots of "not-general-purpose" debugging scripts.


###########################################
How the randomized evolution process works:
###########################################

(i) Start with the initial configuration of generator points.
(ii) Feed in a prescription for how edges between generator points (and perhaps their reflections) should connected by edges. Additionally, feed in prescriptions for how these edges make up polygons (and in 3D, how these polygons further make up polyhedrons.)
(iii) The first half of a driven neighbor exchange drives involves driving an edge to a length of 0 (and in 3D, a polygon to an area of 0). This is achieved by driving the generator point(s) for this edge (polygon) on a predetermined path. Implement a infinitesimal change  for these generator points along the path.
(iii) Add small, random-valued changes to all the other generators points. Note that, to preserve spatial symmetries during the transition, some components of some generator points should remain unchanged.
(iv) Keep checking the corresponding new configuration for the lowest energy one. In this project we place a high cost on area(volume) deformations by magnifying the corresponding stiffness constant; so the smallest cost is (possibly) via preserving area. Pick the smallest energy configuration you can find within a given number of trials. 
(v)  Repeat the process until the the neighbour-separating edge/polygon has shrunk to zero.
(vi) The second-half of the neighbor exchange involves separating out the old neighbours. This requires some edge (and polygon and polyhedron) represecription. Upon represction, the rest of the process is similar.



#########################
Further dvelopment ideas:
#########################


(i) Exception handling in the dynamics code to avoid geometrically inconsistent cells. Currently we are doing this "by eye" but that wouldnt work in large models.
(ii) Automate the reconnection event reconnection process. Requires more thought!
