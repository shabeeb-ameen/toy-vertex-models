Basic Outline:

The conplete geometrical configuration of a valid vertex model requires spatial coordinates for all vertices, plus edge connections between them. However, a slight overspecification is helpful in both two and three dimensions. The code takes an  object-oriented approach to describing minimal vertex models and their dynamics using the following  the following:

1. Contents of classes.py:

These classes are modular and can be used for both 2D and 3D models.
(a) Vertex: These only serve as containers for vertex spatial coordinates; which can be 2 or 3D (but Cartesian!)
(b) Edge: For two vertices that are connected, we generate a single edge class. Attributes include an edge sptial center and length
(c) Polygon: This is an useful overspecification. The polygon class represents 
