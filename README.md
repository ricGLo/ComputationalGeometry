# Computational Geometry


This repository contains implementations to solve the next Computational Geometry problems. Implemented algorithms use a [module](src/geometry_functions.py) that contains geometry functions. This module requires [numpy](https://numpy.org/) in order to work. Each algorithm is animated using [manim](https://www.manim.community/), its instalation is neccesary. Manim is a community maintained [Python](https://www.python.org/) library for creating mathematical animations. It's why all implementations are in [Python](https://www.python.org/). 

## Convex Hull

Both Quick Hull and Graham Scan algorithms were implemented. 

## Art Gallery problem

It was solved using Ear Clipping algorithm to triangulate a polygon. 

## Voronoi Diagram 

Besides, there is an implementation of Incremental Algorithm to solve Voronoi Diagram of given N points in the plane. However this implementation is not in this repository. It can be found in [this repository](https://github.com/cruzjorgesalazar/VoronoiDiagram.git) (documentation in spanish). Doubly-connected edge list (DCEL) was implemented for this problem. Both DCEL and Incremental Algorithm were programmed in C++. Incremental Algorithm prints DCEL data in each iteration of the algorithm in an OUTPUT file. This OUTPUT file is used to animate the algorithm using manim via a python file.  