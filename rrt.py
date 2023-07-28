import random
import math
import matplotlib.pyplot as plt


class RRT:
    def __init__(self):
        self.start = [50, 50]
        self.map_dimensions = [100, 100]
        self.states = []
        self.parents = [0]
        self.states.append(self.start)

    def random_state(self):
        return [random.randint(0, self.map_dimensions[0]), random.randint(0, self.map_dimensions[1])]

    def nearest_neighbor(self, random_point):
        distance_random_state = 1000
        state_parent_index = 0
        for i in range(len(self.states)):
            if math.dist(random_point, self.states[i]) < distance_random_state:
                distance_random_state = math.dist(random_point, self.states[i])
                state_parent_index = i
        self.parents.append(state_parent_index)
        self.states.append(random_point)

    def generate_rrt(self):
        for i in range(5):
            random_point = self.random_state()
            self.nearest_neighbor(random_point)
        print(self.states)
        print(self.parents)
        x_points = [x[0] for x in self.states]
        y_points = [y[1] for y in self.states]
        # plt.plot(x_points, y_points, 'o', scalex=100, scaley=100)
        # plt.show()


print(RRT().generate_rrt())
