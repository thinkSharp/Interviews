import sys

def find_intersection_point(point1, point2, point3, point4):
        def find_slope_and_b(p1, p2):
            #find slope
            top = p2[1] - p1[1]
            bottom = p2[0] - p1[0]
            slope = None
            b = 0
            if top == 0:
                slope = 0
                b = p2[1]
            elif bottom == 0:
                slope = None
                b = p2[0]
            else:
                # m = y2- y1 / x2- x1
                # y = mx + b
                # b = y - mx
                slope = top / bottom
                b = p2[1] - (slope * p2[0])
            return slope, b

        l1_m, l1_b = find_slope_and_b(point1, point2)
        l2_m, l2_b = find_slope_and_b(point3, point4)
        x = y = sys.maxint

        if (l1_m is None or l1_m == 0) and (l2_m is None or l2_m == 0):
            if l1_m == 0:
                x = point1[1]
            elif l1_m is None:
                y = point1[0]

            if l2_m == 0:
                x = point3[1]
            elif l2_m is None:
                y = point3[0]

            if x == sys.maxint or y == sys.maxint:
                return None
            return x,y






