import random
import math
import matplotlib.pyplot as plt

INTERACTIONS = 1000


class RRT:
    def __init__(self):
        self.start = [50, 50]
        self.map_dimensions = [100, 100]
        self.states = []
        self.parents = [0]
        self.states.append(self.start)

    def random_state(self):
        random_point = [random.randint(0, self.map_dimensions[0]), random.randint(0, self.map_dimensions[1])]
        return random_point

    def nearest_neighbor(self, random_point):
        distance_random_state = 1000
        state_parent_index = 0
        for i in range(len(self.states)):
            if math.dist(random_point, self.states[i]) < distance_random_state:
                distance_random_state = math.dist(random_point, self.states[i])
                state_parent_index = i
        self.parents.append(state_parent_index)
        nearest_neighbor = self.states[state_parent_index]
        return nearest_neighbor

    def normalize_vector(self, initial_point, final_point):
        """
        Normalize a vector
        :param initial_point, final_point:
        :return:
        """
        vector = [final_point[0] - initial_point[0], final_point[1] - initial_point[1]]
        vector_sqrt = math.sqrt(math.pow(vector[0], 2) + math.pow(vector[1], 2))
        vector_normalized = [vector[0] / vector_sqrt, vector[1] / vector_sqrt]
        return vector_normalized

    def new_state(self, neighbor, norm):
        new_point = [neighbor[0] + norm[0], neighbor[1] + norm[1]]
        self.states.append(new_point)

    def generate_rrt(self):
        for i in range(INTERACTIONS):
            random_point = self.random_state()
            neighbor = self.nearest_neighbor(random_point)
            norm = self.normalize_vector(neighbor, random_point)
            self.new_state(neighbor, norm)
        print(self.states)
        print(self.parents)
        x_points = [x[0] for x in self.states]
        y_points = [y[1] for y in self.states]
        plt.plot(x_points, y_points, 'o', scalex=100, scaley=100)
        plt.show()


print(RRT().generate_rrt())
