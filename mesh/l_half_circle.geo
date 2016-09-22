// Gmsh project created on Thu Sep 22 16:48:01 2016
ms=0.1;
Point(1) = {0, 0, 0, ms};
Point(2) = {0.5, 0, 0, ms};
Point(3) = {1.0, 0, 0, ms};
Point(4) = {0.5, 0.5, 0, ms};
Line(1) = {1, 2};
Line(2) = {2, 3};
Circle(3) = {3, 2, 4};
Circle(4) = {4, 2, 1};
Line Loop(5) = {4, 1, 2, 3};
Plane Surface(6) = {5};
