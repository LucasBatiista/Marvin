from geopy.distance import great_circle

# -3.0727958048845725, -59.991017392035396 -> ponto inferior esquerdo -> origem
# -3.072621711952975, -59.99093759631886 -> ponto superior direito

# -3.0727958048845725, -59.99093759631886 -> ponto inferior direito
# -3.072621711952975, -59.991017392035396 -> ponto superior esquerdo
print("Distancia Latitude em metros")
dist_lat_metros = great_circle([-3.072621711952975, -59.991017392035396], [-3.0727958048845725, -59.991017392035396]).meters
print(dist_lat_metros)
print("Distancia Latitude")
dist_lat_graus = (-3.072621711952975)-(-3.0727958048845725)
print(dist_lat_graus)
print("Razao Latitude graus pra metros")
print(dist_lat_graus/dist_lat_metros)
print("----------------------------------------------------------------------------------------------")
print("Distancia Longitude em metros")
dist_long_metros = great_circle([-3.0727958048845725, -59.99093759631886], [-3.0727958048845725, -59.991017392035396]).meters
print(dist_long_metros)
print("Distancia Longitude")
dist_long_graus = (-59.99093759631886)-(-59.991017392035396)
print(dist_long_graus)
print("Razao Longitude graus pra metros")
print(dist_long_graus/dist_long_metros)
