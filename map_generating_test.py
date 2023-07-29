import matplotlib.pyplot as plt
import random
import math

# plt.rcParams["figure.figsize"] = [5, 5]
# plt.rcParams["figure.autolayout"] = True
# x_values = [random.randint(1, 10) for i in range(5)]
# y_values = [random.randint(1, 10) for i in range(5)]
x_values = [2, 2.28, 10]
y_values = [3, 3.96, 30]
point_1 = [2, 3]
point_2 = [2.28, 3.96]
plt.plot(x_values, y_values, 'bo', linestyle=":")
plt.show()
print(math.dist(point_2, point_1))
math.sqrt(793)
28.160255680657446
norm = math.sqrt(793)
u = [8/norm, 27/norm]
zero_point = [2, 3]
new_point = zero_point + u
new_point = [zero_point[0] + u[0], zero_point[1] + u[1]]
math.dist(new_point, zero_point)

