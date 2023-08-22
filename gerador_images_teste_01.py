import matplotlib.pyplot as plt

altitudes = [0.0, -0.105, -0.178, 0.366, 1.647, 2.311, 2.258, 1.815, 1.323, 0.826, 0.327, -0.187]
seconds = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
y_points = [y for y in altitudes]
x_points = [x for x in seconds]
plt.plot(x_points, y_points, 'bo', linestyle="-", scalex=100, scaley=100)
plt.savefig('teste_01_altitude.png')
