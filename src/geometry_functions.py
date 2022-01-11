import numpy as np


# numpy can be used instead some of these functions


def InnerProduct(a, b):
    s = 0
    for j in range(len(a)):
        s += a[j]*b[j]
    return s

def norm(x):
    return np.sqrt(InnerProduct(x, x))

# vector rest
def rest_vec(a, b): 
    return [a[0]-b[0], a[1]-b[1]]

#Euclidean distance
def distanceBetweenPoints(a, b):
    return norm(rest_vec(a, b))


def determinant(a, b):
    return a[0]*b[1]-a[1]*b[0]

# 3pi rotation
def rotate_270(x):
    return [x[1], -x[0]]


# Distance from a point to a line 
def distanceToLine(a, b, p):
    r = rest_vec(b, a)
    return np.abs(InnerProduct(rotate_270(r), rest_vec(p, a)))/norm(r)


#Returns True if point p is to the left of directed segment ab, in other case it returns False
def IsLeft(a, b, p):
    if determinant(rest_vec(b, a), rest_vec(p, a)) > 0:
        return True
    else:
        return False

#Returns True if point p is to the right of directed segment ab, in other case it returns False
def IsRight(a, b, p):
    if determinant(rest_vec(b, a), rest_vec(p, a)) < 0:
        return True
    else:
        return False

### Next three functions are implemented to sort points in dictionary order using Quick sort algorithm

def swap_points(points, j, i):
    aux_x = points[i][0]
    aux_y = points[i][1]
    points[i][0] = points[j][0]
    points[i][1] = points[j][1]
    points[j][0] = aux_x
    points[j][1] = aux_y

def Partition_x(points, p, r):
    x = points[r][0]
    i = p - 1
    for j in range(p, r):
        if points[j][0] <= x:
            i += 1
            swap_points(points, i, j)
    swap_points(points, i+1, r)
    return i + 1
            
def QuickSort_x(points, p, r):
    if p < r:
        q = Partition_x(points, p, r)
        QuickSort_x(points, p, q-1)
        QuickSort_x(points, q+1, r)

################ Functions added for Art Gallery problem

#Returns True if the point p is inside the triangle T, it returns False otherwise
def IsInsideTriangle(T, p):
    b = IsRight(T[0], T[1], p) 
    if  IsRight(T[1], T[2], p) == b and IsRight(T[2], T[0], p) == b:
        return True
    else:
        return False


# Returns True if triangles T1 and T2 share an edge, otherwise it returns False
def AreAdjacentTriangles(T1, T2):
    equal_vertex = 0
    for j in range(3):
        for i in range(3):
            if T1[j][0] == T2[i][0] and T1[j][1] == T2[i][1]:
                equal_vertex += 1

    if equal_vertex == 2:
        return True
    else:
        return False


# Returns centroid of triangle T
def Gravicentro(T):
    return [ (T[0][0] + T[1][0] + T[2][0])/3 , (T[0][1] + T[1][1] + T[2][1])/3]


#Returns True if the point p is a vertex of the triangle T, else it returns False
def IsThePoint_a_vertex_of_triange(T, p): 
    if T[0][0] == p[0] and T[0][1] == p[1]:
        return True
    if T[1][0] == p[0] and T[1][1] == p[1]:
        return True
    if T[2][0] == p[0] and T[2][1] == p[1]:
        return True
    return False
