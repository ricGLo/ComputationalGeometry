from manim import *
import geometry_functions as gf
config.frame_width = 50


def QuickHalfHull(a, b, points, self):
    n = len(points)

    if n == 0:  #base case of recursion
        self.play(Create(Line([a[0], a[1],0],[b[0],b[1],0])),run_time=0.7)
        return [b]
    
    furthest = points[0]
    d = gf.distanceToLine(a, b, furthest)
    for j in range(1, n):
        d_aux = gf.distanceToLine(a, b, points[j])
        if d_aux > d: 
            furthest = points[j]
            d = d_aux

    self.play(Create(DashedLine([a[0],a[1],0],[furthest[0], furthest[1],0], dash_length = 0.7)),run_time=0.5)
    self.play(Create(DashedLine([b[0],b[1],0],[furthest[0], furthest[1],0], dash_length = 0.7)),run_time=0.5)

    LeftOf_ac = []
    RightOf_bc = []

    for j in range(n):
            if gf.IsLeft(a, furthest, points[j]):
                LeftOf_ac.append(points[j])
            if gf.IsRight(b, furthest, points[j]):
                RightOf_bc.append(points[j])
    return QuickHalfHull(a, furthest, LeftOf_ac, self) + QuickHalfHull(furthest, b, RightOf_bc, self)



class QuickHull(Scene): 
    def construct(self):
        points = [[0.5, 2], [1.5, 4], [5, 6], [10, 11], [-2, 11], [-20, 6], [10, -10], [15, -8], [-4, 6], [-7, -8], [-10, -10], [-1, -2], [0, 1], [4, 9], [1, 3], [-6, 8], [12, 0], [12,9], [-9, 6], [-10, 8], [15, 9], [-1, 0], [0, 0], [8, 8], [3, 1], [1, 1]]
        
        
        #Find Horizontal extrema where a is the left point and b the right one
        a = points[0] 
        b = points[0]

        n = len(points)
        for j in range(0, n):
            dot = Dot([points[j][0],points[j][1],0])
            self.add(dot)
            if points[j][0] < a[0]:
                a = points[j]
            if points[j][0] > b[0]:
                b = points[j]
            
        self.play( Create( DashedLine([a[0],a[1],0],[b[0],b[1],0], dash_length = 0.7)),run_time=0.5 )

        RightOf_ab = []
        LeftOf_ab = []

        for j in range(n):
            if gf.IsLeft(a, b, points[j]):
                LeftOf_ab.append(points[j])
            if gf.IsRight(a, b, points[j]):
                RightOf_ab.append(points[j])

        ConvexHull = [a] + QuickHalfHull(a, b, LeftOf_ab, self) + QuickHalfHull(b, a, RightOf_ab, self)
        ConvexHull.pop() #Evitar que a se repita en la solución

        self.wait(3)

        print(ConvexHull)



        #[[-20, 6], [-2, 11], [10, 11], [15, 9], [15, -8], [10, -10], [-10, -10]] 