import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 7.50]
plt.rcParams["figure.autolayout"] = True
point1 = [1, 1]
point2 = [2, 2]
point3 = [3, 4]
point4 = [5, 7]
x_values = [point1[0], point2[0], point3[0], point4[0]]
y_values = [point1[1], point2[1], point3[1], point4[1]]
plt.plot(x_values, y_values, 'bo', linestyle=":")
plt.show()
