import math

from matplotlib import pyplot as plt

# lat1 = -3.072766
# long1 = -59.990972
# lat2 = -3.073212
# long2 = -59.990871
# # latitude é y e longitude é x
# long_points = [long1, long2]  # x
# lat_points = [lat1, lat2]  # y
#
# """ Calculating Bearing """
# lat1 = math.radians(lat1)
# long1 = math.radians(long1)
# lat2 = math.radians(lat2)
# long2 = math.radians(long2)
# bearing = math.atan2(math.sin(long2 - long1) * math.cos(lat2),
#                      math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(long2 - long1))
#
# bearing = math.degrees(bearing)
# bearing = (bearing + 360) % 360
# print(bearing)

points = [[-3.0726500010085402, -59.99097762921535], [-3.072658523489693, -59.99098050476389],
          [-3.072664857797194, -59.99097411166698], [-3.0726737982305576, -59.99097313745715],
          [-3.0726801106675095, -59.990966722702495], [-3.0726885287619305, -59.99096355375206],
          [-3.0726854403030006, -59.99095509534234], [-3.0726829147554566, -59.990946451616935],
          [-3.0726902880246754, -59.990941295164255], [-3.072690868623803, -59.990932307801316],
          [-3.0726940741230937, -59.99092389317566], [-3.0726948357291355, -59.990914919377985],
          [-3.072701430649716, -59.9909087962697], [-3.0727020841416572, -59.990899813927086],
          [-3.0727101720018224, -59.990895875807674], [-3.0727188196083084, -59.990893403121675],
          [-3.072722504684141, -59.99090161846363], [-3.0727278443226145, -59.990908865315305],
          [-3.0727321526063682, -59.99091677075449], [-3.072727150630915, -59.99092425533278],
          [-3.072728231377025, -59.99093319621566], [-3.072733291480645, -59.99094064150483],
          [-3.0727365955172594, -59.990949017819574], [-3.072738077449334, -59.99095790085475],
          [-3.072746294786958, -59.99096156030109], [-3.072754559963634, -59.99096511005695]]
points.reverse()

long_points = [x[1] for x in points]
lat_points = [y[0] for y in points]

plt.plot(long_points, lat_points, 'bo', linestyle="--")
plt.plot(long_points[0], lat_points[0], 'go')
plt.plot(long_points[-1], lat_points[-1], 'ro')
plt.show()
