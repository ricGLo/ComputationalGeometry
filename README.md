# Computational Geometry


This repository contains implementations to solve the next Computational Geometry problems. Implemented algorithms use a [module](src/geometry_functions.py) that contains geometry functions. This module requires [numpy](https://numpy.org/) in order to work. Each algorithm is animated using [manim](https://www.manim.community/), its instalation is neccesary. [Manim](https://www.manim.community/) is a community maintained [Python](https://www.python.org/) library for creating mathematical animations. It's why all implementations are in [Python](https://www.python.org/). [ConvexHull](src/ConvexHull) and [ArtGallery](src/ArtGallery) folders contain a media folder where animation videos are found. However, resulting videos are also found in [this YouTube playlist](https://youtube.com/playlist?list=PL0Tt1mQwusqRMgzO8DjtxT12ajNNG3YQu).

## Convex Hull

Both Quick Hull and Graham Scan algorithms were implemented. Graham scan implementation requires no points repeted in given INPUT. 

To create Quick Hull animation you must run in terminal
~~~
manim -p QuickHull.py QuickHull  
~~~
in [ConvexHull](src/ConvexHull) folder. Similarly to obtain Graham Scan video you must run
~~~
manim -p GrahamScan.py GrahamScan  
~~~
in same folder. You can use -pql instead of -p to create low quality video. 

## Art Gallery problem

It was solved using Ear Clipping algorithm to triangulate a polygon. Then, dual graph of triangulation is constructed. After that dual graph is explored coloring vertices of blue, green and red. Finally algotihm checks wich color is the least used to obtain the OUTPUT. 

Art Gallery animation requires a [LaTex](https://www.latex-project.org/) distribution. For example: [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/). 

To crate animation run 
~~~
manim -p ArtGallery.py ArtGallery  
~~~
in [ArtGallery](src/ArtGallery) folder. You can use -pql instead of -p to create low quality video. 

## Voronoi Diagram 

Besides, there is an implementation of Incremental Algorithm to solve Voronoi Diagram of given N points in the plane. However this implementation is not in this repository. It can be found [here](https://github.com/cruzjorgesalazar/VoronoiDiagram.git) (documentation in spanish). Doubly-connected edge list (DCEL) was implemented for this problem. Both DCEL and Incremental Algorithm were programmed in C++. Incremental Algorithm prints DCEL data in each iteration of the algorithm in an OUTPUT file. This OUTPUT file is used to animate algorithm using manim via a Python file. To generate animation is also necessary a [LaTex](https://www.latex-project.org/) distribution.