import math

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

def farthest_from_origin(points):
    origin = (0, 0)

    farthest_point = points[0]
    max_distance = distance(farthest_point, origin)

    for point in points:
        d = distance(point, origin)

        if d > max_distance:
            max_distance = d
            farthest_point = point

    return farthest_point, max_distance

n = int(input("Enter number of points: "))

points = []

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    point = (x, y)
    points.append(point)

print("\nPoints entered:")
print(points)

p1_index = int(input("\nEnter index of first point: "))
p2_index = int(input("Enter index of second point: "))

p1 = points[p1_index]
p2 = points[p2_index]

print("Distance between points:", distance(p1, p2))

farthest, max_distance = farthest_from_origin(points)

print("Farthest point from origin:", farthest)
print("Distance from origin:", max_distance)