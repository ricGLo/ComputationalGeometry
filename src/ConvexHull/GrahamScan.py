from manim import *

import sys
sys.path.append('../')
import geometry_functions as gf

config.frame_width = 35


class GrahamScan(Scene): 
    def construct(self):

        ##########################         INPUT         ###############################
        
        # IMPORTANT: Assume there is no repeated points
        points = [[-6.5, 0], [6, 0], [0, 7], [1, 5], [-8, 6], [9, -5], [5.3, -6], [-3, 2], [-2, -2], [-3, -2], [-3, -3], [3, 5], [4, 6], [-2, -7], [4.5, 5.6], [5.89, -7], [-6.5, -7], [5, 5], [1.5, 1.5], [4, -5] ]
        #points = [[0.5, 2], [1.5, 4], [5, 6], [10, 11], [-2, 11], [-20, 6], [10, -10], [15, -8], [-4, 6], [-7, -8], [-10, -10], [-1, -2], [0, 1], [4, 9], [1, 3], [-6, 8], [12, 0], [12,9], [-9, 6], [-10, 8], [15, 9], [-1, 0], [0, 0], [8, 8], [3, 1], [1, 1]]

        ################################################################################


        n = len(points)
        gf.QuickSort_x(points, 0, n-1) # sort input using quick sort

        #Add input points to animation
        for j in range(n):
            dot = Dot([points[j][0],points[j][1],0])
            self.add(dot)


        # List for points in the upper part of convex hull
        L_upper = []
        # Add first two points to the list L_upper
        L_upper.append(points[0]) 
        L_upper.append(points[1])


        lines = [] #Array to store lines in animation
        #Add first line to the list 
        lines.append(Line([L_upper[0][0], L_upper[0][1],0], [L_upper[1][0], L_upper[1][1],0]))
        self.play(Create(lines[0]),run_time=0.5)

        
        for j in range(2, n):
            L_upper.append(points[j]) #Append p_i to the list

            #Draw the line in animation
            lines.append(Line([L_upper[-2][0], L_upper[-2][1],0], [L_upper[-1][0], L_upper[-1][1],0]))
            self.play(Create(lines[-1]),run_time=0.5)

            #while L_upper contains more than two points and the last three points in the list dont make a right turn
            while len(L_upper) > 2 and gf.IsRight(L_upper[-3], L_upper[-1], L_upper[-2]):

                ###########  Delete the middle of the las three points using pop() and an auxiliar point
                p_aux = L_upper.pop()
                L_upper.pop()
                L_upper.append(p_aux)
                
                #Add a line joining the last two points in L_upper
                lines.append(Line([L_upper[-2][0], L_upper[-2][1],0], [L_upper[-1][0], L_upper[-1][1],0]))
                self.play(Create(lines[-1]),run_time=0.5)

                self.remove(lines[-2]) #Animation: remove line joining the delated point and the last point in the list
                self.remove(lines[-3]) #Animation: remove line joining the delated point and L_upper[-2]

                #Update list of lines
                l_aux = lines.pop() 
                lines.pop()
                lines.pop()
                lines.append(l_aux)
       
        # List for points in the lower part of convex hull
        L_lower = []
        # Add the last two points to the list L_lower
        L_lower.append(points[n-1])
        L_lower.append(points[n-2])

        lines = [] #Array to store lines in animation
        #Add first line to the list 
        lines.append(Line([L_lower[0][0], L_lower[0][1],0], [L_lower[1][0], L_lower[1][1],0]))
        self.play(Create(lines[0]),run_time=0.5)
     
        for i in range(2, n):
            j = n - i - 1 #change of index variable 

            L_lower.append(points[j])#Append p_i to the list


            #Draw the line in animation
            lines.append(Line([L_lower[-2][0], L_lower[-2][1],0], [L_lower[-1][0], L_lower[-1][1],0]))
            self.play(Create(lines[-1]),run_time=0.5)

            #while L_lower contains more than two points and the last three points in the list dont make a right turn
            while len(L_lower) > 2 and gf.IsRight(L_lower[-3], L_lower[-1], L_lower[-2]):

                ###########  Delete the middle of the last three points using pop() and an auxiliar point
                p_aux = L_lower.pop()
                L_lower.pop()
                L_lower.append(p_aux)

                #Add a line joining the last two points in L_lower
                lines.append(Line([L_lower[-2][0], L_lower[-2][1],0], [L_lower[-1][0], L_lower[-1][1],0]))
                self.play(Create(lines[-1]),run_time=0.5)
                
                self.remove(lines[-2]) #Animation: remove line joining the delated point and the last point in the list
                self.remove(lines[-3]) #Animation: remove line joining the delated point and L_upper[-2]

                #Update list of lines
                l_aux = lines.pop()
                lines.pop()
                lines.pop()
                lines.append(l_aux)

        #Avoid repeted points in solution 
        L_upper.pop() 
        L_lower.pop()
        ConvexHull = L_upper + L_lower #Concatenate to get the solution
        print(ConvexHull) #print solution in terminal
        self.wait(3) #Wait 3 seconds before end