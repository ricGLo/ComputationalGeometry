from manim import *
import geo_funcs as gf
config.frame_width = 35



class GrahamScan(Scene): 
    def construct(self):
        #points = [[0.5, 2], [1.5, 4], [5, 6], [10, 11], [-2, 11], [-20, 6], [10, -10], [15, -8], [-4, 6], [-7, -8], [-10, -10], [-1, -2], [0, 1], [4, 9], [1, 3], [-6, 8], [12, 0], [12,9], [-9, 6], [-10, 8], [15, 9], [-1, 0], [0, 0], [8, 8], [3, 1], [1, 1]]

        points = [[-6.5, 0], [6, 0], [0, 7], [1, 5], [-8, 6], [9, -5], [5.3, -6], [-3, 2], [-2, -2], [-3, -2], [-3, -3], [3, 5], [4, 6], [-2, -7], [4.5, 5.6], [5.89, -7], [-6.5, -7], [5, 5], [1.5, 1.5], [4, -5] ]
        

        n = len(points)
        gf.QuickSort_x(points, 0, n-1)
        for j in range(0, n):
            dot = Dot([points[j][0],points[j][1],0])
            self.add(dot)


        L_upper = []
        L_upper.append(points[0])
        L_upper.append(points[1])

        lines = []
        lines.append(Line([L_upper[0][0], L_upper[0][1],0], [L_upper[1][0], L_upper[1][1],0]))
        self.play(Create(lines[0]),run_time=0.5)

        
        for j in range(2, n):
                
            L_upper.append(points[j])
            lines.append(Line([L_upper[-2][0], L_upper[-2][1],0], [L_upper[-1][0], L_upper[-1][1],0]))
            self.play(Create(lines[-1]),run_time=0.5)

            while len(L_upper) > 2 and gf.IsRight(L_upper[-3], L_upper[-1], L_upper[-2]):
                p_aux = L_upper.pop()
                L_upper.pop()
                L_upper.append(p_aux)
                
                lines.append(Line([L_upper[-2][0], L_upper[-2][1],0], [L_upper[-1][0], L_upper[-1][1],0]))
                self.play(Create(lines[-1]),run_time=0.5)
                self.remove(lines[-2])
                self.remove(lines[-3])
                l_aux = lines.pop()
                lines.pop()
                lines.pop()
                lines.append(l_aux)
       

        L_lower = []
        L_lower.append(points[n-1])
        L_lower.append(points[n-2])

        lines = []
        lines.append(Line([L_lower[0][0], L_lower[0][1],0], [L_lower[1][0], L_lower[1][1],0]))
        self.play(Create(lines[0]),run_time=0.5)
     
        for i in range(2, n):
            j = n - i - 1

            L_lower.append(points[j])
            lines.append(Line([L_lower[-2][0], L_lower[-2][1],0], [L_lower[-1][0], L_lower[-1][1],0]))
            self.play(Create(lines[-1]),run_time=0.5)

            while len(L_lower) > 2 and gf.IsRight(L_lower[-3], L_lower[-1], L_lower[-2]):
                p_aux = L_lower.pop()
                L_lower.pop()
                L_lower.append(p_aux)
                lines.append(Line([L_lower[-2][0], L_lower[-2][1],0], [L_lower[-1][0], L_lower[-1][1],0]))
                self.play(Create(lines[-1]),run_time=0.5)
                self.remove(lines[-2])
                self.remove(lines[-3])
                l_aux = lines.pop()
                lines.pop()
                lines.pop()
                lines.append(l_aux)

        L_upper.pop()
        L_lower.pop()
        ConvexHull = L_upper + L_lower
        print(ConvexHull)
        self.wait(3)



       
        

            
    
'''[[-20, 6], [-2, 11], [10, 11], [15, 9], [15, -8], [10, -10], [-10, -10], [-20, 6]]
'''