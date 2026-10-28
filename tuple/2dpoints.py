import math

points = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    points.append((x, y))

p1 = points[0]
p2 = points[1]

distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print("Distance:", distance)

farthest = max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))

print("Farthest point:", farthest)