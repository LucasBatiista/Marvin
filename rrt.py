import datetime
import math
import random
import csv

from geopy.distance import great_circle


class RRT:
    def __init__(self, start, arrival, logging_file, csv_filename):
        self.start = start
        self.arrival = arrival
        self.logging = logging_file
        self.generation_csv_file = f'{csv_filename}_generation_states.csv'
        self.path_csv_file = f'{csv_filename}_path_states.csv'
        self.map_dimensions = [[-3.072787, -59.991006], [-3.072635, -59.990953]]
        self.states = []
        self.states.append(self.start)
        self.generation_start_time = datetime.datetime.now()
        self.generation_finish_time = None
        if not self.start_is_in_map():
            raise Exception("Start point not in map!")
        self.generate_rrt()

    def start_is_in_map(self):
        """

        :return:
        """
        latitude_in_map = self.map_dimensions[0][0] < self.start[0] < self.map_dimensions[1][0]
        longitude_in_map = self.map_dimensions[0][1] < self.start[1] < self.map_dimensions[1][1]
        if latitude_in_map and longitude_in_map:
            return True
        else:
            return False

    def random_state(self):
        """
        Generate a new state in a given dimensions for a space
        :return:
        """
        random_point = [random.uniform(self.map_dimensions[0][0], self.map_dimensions[1][0]),
                        random.uniform(self.map_dimensions[0][1], self.map_dimensions[1][1])]
        return random_point

    def nearest_neighbor(self, random_point):
        """
        Get the closest point for a given set of points
        :param random_point:
        :return:
        """
        distance_random_state = 1000
        state_parent_index = 0
        for i in range(len(self.states)):
            state_coordinates = [self.states[i][0], self.states[i][1]]
            distance = math.dist(random_point, state_coordinates)
            if distance < distance_random_state:
                distance_random_state = distance
                state_parent_index = i
        nearest_neighbor = self.states[state_parent_index]
        return nearest_neighbor, state_parent_index

    @staticmethod
    def normalize_vector(initial_point, final_point):
        """
        Normalize a vector
        :param final_point:
        :param initial_point:
        :return:
        """
        try:
            vector = [final_point[0] - initial_point[0], final_point[1] - initial_point[1]]
            initial_point_coordinates = [initial_point[0], initial_point[1]]
            vector_sqrt = great_circle(final_point, initial_point_coordinates).meters
            vector_normalized = [vector[0] / vector_sqrt, vector[1] / vector_sqrt]
            return vector_normalized
        except ZeroDivisionError:
            raise Exception

    def new_state(self, neighbor, norm, neighbor_index):
        """
        Generate a new state based on a norm for two points
        :param neighbor_index:
        :param neighbor:
        :param norm:
        :return:
        """
        new_point = [neighbor[0] + norm[0], neighbor[1] + norm[1], neighbor_index]
        self.states.append(new_point)
        return new_point

    def is_in_arrival_region(self, point):
        """
        Verify if a certain point is at the arrival region
        :param point:
        :return:
        """
        node = [point[0], point[1]]
        distance = great_circle(self.arrival, node).meters
        if distance <= 1:
            return True
        else:
            return False

    def generate_rrt(self):
        """
        Generate a new set of points and plot them
        :return:
        """
        arrived = False
        while arrived is False:
            random_point = self.random_state()
            neighbor, neighbor_index = self.nearest_neighbor(random_point)
            norm = self.normalize_vector(neighbor, random_point)
            new_state = self.new_state(neighbor, norm, neighbor_index)
            arrived = self.is_in_arrival_region(new_state)
        self.generation_finish_time = datetime.datetime.now()
        print(f"Generation took: {self.generation_finish_time - self.generation_start_time}")
        print(f"Nodes:{len(self.states)}")
        with open(self.generation_csv_file, 'w', newline='') as csvfile:
            path_writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            for state in self.states:
                path_writer.writerow(state)

    def get_path(self):
        """
        Get path from point A to B using RRT algorithm
        """
        final_point = [self.states[-1][0], self.states[-1][1]]
        path_points = [final_point]
        point_parent = self.states[-1][2]
        while point_parent != 0:
            point = self.states[point_parent]
            point_parent = point[2]
            path_points.append([point[0], point[1]])
        path_points.reverse()
        print(f"Path has: {len(path_points)} nodes")
        print(f"Path points: {path_points}")
        with open(self.path_csv_file, 'w', newline='') as csvfile:
            path_writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
            for point in path_points:
                path_writer.writerow(point)
        return path_points
