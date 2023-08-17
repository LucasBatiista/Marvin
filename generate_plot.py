import matplotlib.pyplot as plt

states = []

x_points = [x[1] for x in states]
y_points = [y[0] for y in states]
plt.plot(x_points, y_points, 'o', scalex=100, scaley=100)
plt.savefig('RRT_generation.png')

path_points = []
x_points = [x[1] for x in path_points]
y_points = [y[0] for y in path_points]
plt.plot(x_points, y_points, 'bo', linestyle="--", scalex=100, scaley=100)
plt.plot(x_points[0], y_points[0], 'go')
plt.plot(x_points[-1], y_points[-1], 'ro')
plt.savefig('RRT_path.png')
