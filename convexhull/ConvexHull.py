## We are calculating the convex hull of a set of points
def jarvis_march(points):

    cross_product = lambda x1,y1,x2,y2 : x1 * y2 - x2 * y1;

    min_y_point = min(points, key = lambda point: point[1])
    indx = points.index(min_y_point)

    l = indx
    ch = []
    ch.append(min_y_point)
    while(True):
        q = (l+1) % len(points)
        for i in range(len(points)):
            if i == l:
                continue

            turn = cross_product(points[i][0], points[i][1], points[q][0], points[q][1])

## CONTINUE