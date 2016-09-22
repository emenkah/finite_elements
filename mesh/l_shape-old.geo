// Gmsh project created on Thu Sep 22 15:41:24 2016
ms = 0.1;
Point(1) = {0, 0, 0, ms};
Point(2) = {1, 0, 0, ms};
Point(3) = {1, .5, 0, ms};
Point(4) = {.5, .5, 0, ms};
Point(5) = {.5, 1, 0, ms};
Point(6) = {0, 1, 0, ms};
Line(1) = {6, 1};
Line(2) = {2, 2};
Line(3) = {1, 2};
Line(4) = {2, 3};
Line(5) = {3, 4};
Line(6) = {4, 5};
Line(7) = {5, 6};
Line Loop(8) = {1, 3, 4, 5, 6, 7};
Plane Surface(9) = {8};
