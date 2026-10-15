#  2D plane
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def farthest_point(points):
    return max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))

points = [(2, 3), (5, 7), (1, 1), (-4, 6)]

print("Points:", points)

p1 = tuple(map(int, input("Enter first point (x y): ").split()))
p2 = tuple(map(int, input("Enter second point (x y): ").split()))

print("Distance:", calculate_distance(p1, p2))
print("Farthest point from origin:", farthest_point(points))