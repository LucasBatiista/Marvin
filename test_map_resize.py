from geopy.distance import great_circle

map_dimensions = [[-3.072787, -59.991006], [-3.072635, -59.990953]]

distance_long = great_circle([map_dimensions[0][0], map_dimensions[1][1]], [map_dimensions[0][0],map_dimensions[0][1]])
# distance_lat = great_circle(map_dimensions[1][0], map_dimensions[0][0])

print(distance_long.meters)
