Basic Outline:

The geometrical configuration of a valid vertex model requires (i) spatial coordinates for all vertices, and(ii) edge connections between them. A slight overspecification (where edges/ polygonal surfaces constituing each cell is also specified) is helpful in the energy-evaluation context, for both two and three dimensions for the . Here we take an object-oriented approach to describing minimal vertex models and their dynamics using the contents in the following code:


1. Contents of classes.py:

(The classes in this file were designed to be modular and can be used for both 2D and 3D models, even outside the scope of the current work.)


(a) Vertex: These only serve as containers for vertex spatial coordinates; which can be 2 or 3D (but Cartesian!)
(b) Edge: For two vertices that are connected, we generate a single edge class. Attributes include an edge sptial center and length
(c) Polygon: One useful overspecification. The polygon objects store the edges that make up a given polygon. We note that this composition changes in the "second half" of a reconnection event.
The polygon class is equipped with shape parameter and stiffness constsnts, and an energy functional - this energy is for 2D woek only.
(d) Polyhedron: A further useful overrepresentation for 3D, storing the polygons that make up a given cell surface. The/shape parameter constsnts and energy function in this class is relevant in 3D.

Basic usage guides for these classes are commented on the code.



#######################################

Further dvelopment ideas:

(i) Exception handling in the dynamics code to avoid geometrically inconsistent cells. Currently we are doing this "by eye" but that wouldnt work in large models.

(ii) Automate the reconnection event reconnection process. Requires more thought!
