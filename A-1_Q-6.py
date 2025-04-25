# Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
# of the points in your 3-D space and store them in a list. The final output is a list with each
# consisting of a point and its nearest neighbour. [Hint: Use distance between two points
# formula]

# points = []
# for i in range(10):
#     coordinate = int(input("Enter coordinate in 3-D \n"))
#     points.append(coordinate)
# print(points)
import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

points = []
for i in range(10):
    x, y, z = map(int, input("Enter coordinates in 3-D (x y z): ").split())
    points.append((x, y, z))

nearest_neighbours = []

for i in range(len(points)):
    min_distance = float('inf')
    nearest_point = None
    for j in range(len(points)):
        if i != j:
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                nearest_point = points[j]
    nearest_neighbours.append((points[i], nearest_point))

print(nearest_neighbours)