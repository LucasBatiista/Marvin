# import random
#
# space_dimensions = [[-3.072665, -59.990999], [-3.072722, -59.990948]]
#
# print(random.uniform(space_dimensions[0][0], space_dimensions[1][0]))
# print(random.uniform(0, 100))
from geopy.distance import great_circle, geodesic
import math
point1 = [-3.072628, -59.991000]
point2 = [-3.072786, -59.990999]
norm = great_circle(point2, point1).meters
print(great_circle(point2, point1).meters)
vector = [point2[0] - point1[0], point2[1] - point1[1]]
u = [vector[0]/norm, vector[1]/norm]
new_point = [point1[0] + u[0], point1[1] + u[1]]
print(new_point)
print(great_circle(new_point, point1).meters)
print(geodesic(point2, point1).m)
