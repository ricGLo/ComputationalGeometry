from manim import *
import sys
sys.path.append('../')
import geometry_functions as gf



def Is_a_tip(Polygon, j):
    n = len(Polygon)

    if n <= 3:
        return True

    if gf.IsLeft(Polygon[(j-1)%n], Polygon[(j+1)%n], Polygon[j]) == True:
        T = [ Polygon[(j-1)%n], Polygon[j], Polygon[(j+1)%n]]

        i = (j+2)%n
        counter = 0
        while (gf.IsInsideTriangle(T, Polygon[i]) == False) and (counter < n -3):
            i = (i + 1)%n
            counter += 1
        if counter == n-3:
            return True
    return False


def EarClipping(Polygon, n, self):
    Triangles = []
    EarTipsStatus = []

    #Identify each vertex whether it is an ear tip or not 
    for j in range(n):
        dot = Dot([Polygon[j][0],Polygon[j][1],0])
        self.add(dot)
        EarTipsStatus.append(Is_a_tip(Polygon, j))
        self.add(Line([Polygon[j][0],Polygon[j][1],0],[Polygon[(j+1)%n][0],Polygon[(j+1)%n][1],0], stroke_width = 3.7))

    m = n
    while len(Triangles) < n - 2:
        #Find a tip to delate
        i = 0
        while EarTipsStatus[i] == False:
            i = (i + 1)%m

        i_prev = (i-1)%m
        i_next = (i+1)%m

        Triangles.append( [ Polygon[i_prev], Polygon[i], Polygon[i_next]  ])
        self.play( Create( Line([Polygon[i_prev][0],Polygon[i_prev][1],0],[Polygon[i_next][0],Polygon[i_next][1],0], stroke_width = 1.7 )),run_time=0.5 )

        Polygon.pop(i)
        EarTipsStatus.pop(i)
        m = m - 1

        if i == 0:
            i_prev = i_prev - 1
        EarTipsStatus[i_prev] = Is_a_tip(Polygon, i_prev)
        EarTipsStatus[i%m] = Is_a_tip(Polygon, i%m)
    return Triangles


#Function to make the graph edges
def make_link(G, v1, v2):
    if v1 not in G:
        G[v1] = {}
    (G[v1])[v2] = 1
    if v2 not in G:
        G[v2] = {}
    (G[v2])[v1] = 1
    return G


def MakeGraph(Triangles):
    n = len(Triangles)
    G = {0: {}}
    for j in range(n):
        i = 0
        equal_edges = 0 
        while i < n and equal_edges < 3:
            if gf.AreAdjacentTriangles(Triangles[j], Triangles[i]) == True:
                equal_edges += 1
                make_link(G, j, i)
            i += 1
    return G

def colorize(Triangles, colorized, to_colorate, colors_for_counting, counter, self):
    T1 = Triangles[colorized]
    c1 = colors_for_counting[colorized]
    T2 = Triangles[to_colorate]
    c2 = colors_for_counting[to_colorate]

    unused_colors = [PURE_BLUE, PURE_GREEN, PURE_RED]
    counter_locations = {PURE_BLUE : 11*LEFT + 3*DOWN, PURE_GREEN: 11*LEFT + 4*DOWN, PURE_RED: 11*LEFT + 5*DOWN}

    #T1 and T2 share an edge and therefore two vertices
    #Colorize the vertices of T1 that are shared with T2
    for j in range(3):
        for i in range(3):
            if T2[j][0] == T1[i][0] and T2[j][1] == T1[i][1]:
                c2[j] = c1[i]
                unused_colors.remove(c2[j])

    
    #Find the index of the different vertex
    if len(unused_colors) > 0:
        for j in range(3):
            if c2[j] == WHITE:
                c2[j] = unused_colors[0]
                
                self.play( Create(Dot([T2[j][0], T2[j][1],0], color= c2[j], radius = 0.15)),run_time=0.5 )
                new_number = Integer( (counter[c2[j]]).number + 1 ).shift(counter_locations[c2[j]])
                self.play( Transform( counter[c2[j]], new_number) )
                counter[c2[j]].number += 1



def DFS(G, Triangles, vertice, node_colors, cfc, counter, self):
    nodos_visitados = 0
    node_colors[vertice] = 'gray'
    gc = gf.Gravicentro(Triangles[vertice]) 
    dot = Dot([gc[0], gc[1],0], color= GRAY_B)
    self.play( Create(dot),run_time=0.5 )

    for v in G[vertice] :
        if node_colors[v] == 'white':
            gc2 = gf.Gravicentro(Triangles[v]) 
            self.play( Create( Line([gc[0], gc[1],0], [gc2[0], gc2[1],0], stroke_width = 1.4, color = GRAY )),run_time=0.5 )
            colorize(Triangles, vertice, v, cfc, counter, self)
            nodos_visitados = nodos_visitados + DFS(G, Triangles, v, node_colors, cfc, counter, self)

    node_colors[vertice] = 'black'
    gc = gf.Gravicentro(Triangles[vertice]) 
    dot = Dot([gc[0], gc[1],0], color= GRAY_D)
    self.play( Create(dot),run_time=0.5 )

    nodos_visitados = nodos_visitados + 1
    return nodos_visitados



class ArtGallery(Scene): 
    def construct(self):

        #Poligons given clockwise

        #Ejemplo 1:
        #P = [ [-8, 3.38], [-4.18, 4.34], [0.8, 3.52], [-1, 0], [5.22, -0.82], [0.82, -3.94], [-4.04, -0.64], [-4.16, -4.22], [-8.86, -2.96]     ]

        ## Ejemplo 2: (Peine)
        #P = [ [-10, -2], [-8, 3], [-7, 0], [-5, 0], [-4, 3], [-3, 0], [-1, 0], [0, 3], [1, 0], [3, 0], [4, 3], [5, 0], [7, 0], [8, 3], [10, -2] ]

        ## Ejemplo 3: 
        P = [ [-8.0452498315983,2.7710737972853], [-4.376732784892,4.7229129952125], [-2.4954419917093,1.0779120834209], [1.0554943804232,4.0409450826837], [3.3130433322424,3.4060094399845], [3.47765627, 0], [6.7463990298009,-2.3554436141376], [6.9110119742044,-5.0362829944231], [3.7833660305381,-5.4125411530596], [4.7240114271295,-3.3196051456438], [2.8897529037763,-1.6499595666941], [2.0431720468441,1.6187831864609], [-1.202054571, -4.6365], [-4.8705716181025,-5.2244120737413], [-5.4349588560573,-0.897443249421], [-7.2927335143252,-5.3890250181448], [-9.2210565773375,-5.3184766134005] ]

        self.add( Text(" Art gallery problem  ").shift(5.5*UP).scale(1.5) ) 
        Triangles = EarClipping(P, len(P), self)
        
        
        G = MakeGraph(Triangles)
        colors = {} #Node colors
        for v in G:
            colors[v] = 'white'

        #The colors of each vertex of the triangles are allocated here
        colors_for_counting = []
        for j in range(len(Triangles)):
            c = [WHITE, WHITE, WHITE]
            colors_for_counting.append(c)

        #Couter of each color (red, blue and green)
        counter = {PURE_BLUE: Integer(number= 1).shift(11*LEFT + 3*DOWN), PURE_GREEN : Integer(number= 1).shift(11*LEFT + 4*DOWN), PURE_RED: Integer(number= 1).shift(11*LEFT + 5*DOWN)}

        
        #Colorize the first triangle
        colors_for_counting[0][2] = PURE_BLUE
        self.play( Create(Dot([Triangles[0][2][0], Triangles[0][2][1],0], color= PURE_BLUE, radius = 0.15)),run_time=0.5 )
        self.play( Create(Square(side_length=0.4, color = PURE_BLUE, fill_opacity = 1).shift(12*LEFT + 3*DOWN)  )  )
        self.play(Create(counter[PURE_BLUE]), run_time = 0.5)
    
        colors_for_counting[0][1] = PURE_GREEN
        self.play( Create(Dot([Triangles[0][1][0], Triangles[0][1][1],0], color= PURE_GREEN, radius = 0.15)),run_time=0.5 )
        self.play( Create(Square(side_length=0.4, color = PURE_GREEN, fill_opacity = 1).shift(12*LEFT + 4*DOWN)  )  )
        self.play(Create(counter[PURE_GREEN]), run_time = 0.5)

        colors_for_counting[0][0] = PURE_RED
        self.play( Create(Dot([Triangles[0][0][0], Triangles[0][0][1],0], color= PURE_RED, radius = 0.15)),run_time=0.5 )
        self.play( Create(Square(side_length=0.4, color = PURE_RED, fill_opacity = 1).shift(12*LEFT + 5*DOWN)  )  )
        self.play(Create(counter[PURE_RED]), run_time = 0.5 )


        DFS(G, Triangles, 0, colors, colors_for_counting, counter, self)

        #Find the number of vertices colored by the least used color
        min = counter[PURE_BLUE].number
        if min > counter[PURE_GREEN].number:
            min = counter[PURE_GREEN].number
        if min > counter[PURE_RED].number:
            min = counter[PURE_RED].number

        print("\n\n\nThe number of security cameras that shall be used is: ", min, "\n\n\n")

        self.play(Create( Text(" OUTPUT: ").shift(5.5*DOWN) )  )
        self.play(Create( Integer(number=min ).shift(5.5*DOWN+2*RIGHT).scale(1.8) )  )
        self.wait(3)