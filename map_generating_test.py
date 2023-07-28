import matplotlib.pyplot as plt
import random

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True
x_values = [random.randint(1, 10) for i in range(5)]
y_values = [random.randint(1, 10) for i in range(5)]
plt.plot(x_values, y_values, 'bo', linestyle=":")
plt.show()

