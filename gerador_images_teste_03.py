import matplotlib.pyplot as plt

latitude_origem, longitude_origem = -3.0727958048845725, -59.991017392035396
latitude_destino, longitude_destino = -3.072764893793319, -59.99096969095618
conversao_latitude, conversao_longitude = 8.993203354940148e-06, 9.006152089787253e-06

primeira_geracao = [[-3.0726447, -59.990993, 0],
                    [-3.0726536215392146, -59.99099186530002, 0],
                    [-3.072661925236923, -59.99099532372112, 1],
                    [-3.0726707894250875, -59.990993803683786, 2],
                    [-3.072679740400093, -59.99099293194038, 3],
                    [-3.0726884914424004, -59.99099500783708, 4],
                    [-3.0726823418143585, -59.990984310809246, 4],
                    [-3.0726854278992306, -59.99097585153058, 6],
                    [-3.0726972272280664, -59.990997147207565, 5],
                    [-3.072705721130544, -59.990994188071234, 8],
                    [-3.07271455199175, -59.990995891577974, 9],
                    [-3.0727204578318084, -59.99098909957458, 10],
                    [-3.0727130920703094, -59.99098902827949, 9],
                    [-3.0727128673912105, -59.990980024939184, 12],
                    [-3.072729215076516, -59.99099114907236, 11],
                    [-3.0726891049169818, -59.990986022664536, 5],
                    [-3.072736224383921, -59.990985506484186, 14],
                    [-3.072744701905574, -59.99098851236095, 16],
                    [-3.072753503940296, -59.99099035943821, 17],
                    [-3.0727424520408984, -59.99097900915436, 16],
                    [-3.0727587928268663, -59.99098307535684, 18],
                    [-3.072651578399768, -59.99098309464975, 1],
                    [-3.072726517512998, -59.99099974051851, 14],
                    [-3.0727039360899426, -59.990978970064056, 13],
                    [-3.0726939466621856, -59.990978738107316, 7],
                    [-3.0726473108201113, -59.990975167100416, 21],
                    [-3.0727509073833894, -59.99098207704189, 19],
                    [-3.072735036379103, -59.99100262679005, 22],
                    [-3.0727555284498322, -59.990974350789365, 26],
                    [-3.0727615775806476, -59.990994326712226, 18],
                    [-3.072770512156463, -59.99099535340128, 29],
                    [-3.0727770374544665, -59.991001550865, 30],
                    [-3.0726995494309577, -59.99098578291299, 24],
                    [-3.0727673449946753, -59.99098028960178, 20],
                    [-3.0727781977185775, -59.990990676576374, 30],
                    [-3.0726605715911015, -59.99098310937538, 21],
                    [-3.072695263042954, -59.99096982895985, 24],
                    [-3.072760037867194, -59.99096655865702, 28]]

x_points = [(x[1] - longitude_origem) / conversao_longitude for x in primeira_geracao]
y_points = [(y[0] - latitude_origem) / conversao_latitude for y in primeira_geracao]
plt.plot(x_points, y_points, 'o', color='darkorange', label='Coordenadas geradas')
plt.plot(x_points[0], y_points[0], 'o', color='darkgreen', label='Coordenada inicial')
x_destino = (longitude_destino - longitude_origem) / conversao_longitude
y_destino = (latitude_destino - latitude_origem) / conversao_latitude
plt.plot(x_destino, y_destino, 'o', color='red', label='Coordenada destino')
center = x_destino, y_destino
circle = plt.Circle(center, radius=1, fill=False, color='red', label='Região de Destino')
plt.gcf().gca().add_patch(circle)
plt.rc('axes', labelsize=4)
plt.ylim(0, 20)
plt.xlim(0, 20)
plt.ylabel("Distância no sentido Norte em metros")
plt.xlabel("Distância no sentido Leste em metros")
plt.grid(color='b', linestyle='-', linewidth=0.1)
plt.legend()
plt.savefig('teste_03_coordenadas_geradas.png', dpi=300)

primeiro_caminho = [[-3.0726536215392146, -59.99099186530002],
                    [-3.072661925236923, -59.99099532372112],
                    [-3.0726707894250875, -59.990993803683786],
                    [-3.072679740400093, -59.99099293194038],
                    [-3.0726884914424004, -59.99099500783708],
                    [-3.0726972272280664, -59.990997147207565],
                    [-3.072705721130544, -59.990994188071234],
                    [-3.07271455199175, -59.990995891577974],
                    [-3.0727204578318084, -59.99098909957458],
                    [-3.072729215076516, -59.99099114907236],
                    [-3.072736224383921, -59.990985506484186],
                    [-3.0727424520408984, -59.99097900915436],
                    [-3.0727509073833894, -59.99098207704189],
                    [-3.0727555284498322, -59.990974350789365],
                    [-3.072760037867194, -59.99096655865702]]

x_points = [(x[1] - longitude_origem) / conversao_longitude for x in primeiro_caminho]
y_points = [(y[0] - latitude_origem) / conversao_latitude for y in primeiro_caminho]
plt.plot(x_points, y_points, 'o', color='greenyellow', linestyle="--", label='Primeiro caminho gerado')
plt.legend()
plt.savefig('teste_03_primeiro_caminho.png', dpi=300)

primero_caminho_cumprido = [[-3.0726501, -59.9909915],
                            [-3.0726551, -59.9909928],
                            [-3.0726634, -59.9909956],
                            [-3.0726719, -59.990994]]

x_points = [(x[1] - longitude_origem) / conversao_longitude for x in primero_caminho_cumprido]
y_points = [(y[0] - latitude_origem) / conversao_latitude for y in primero_caminho_cumprido]
plt.plot(x_points, y_points, 'o', color='darkblue', linestyle="-", label='Primeiro caminho executado')
plt.legend()
plt.savefig('teste_03_primeiro_caminho_cumprido.png', dpi=300)

segunda_geracao = [[-3.0726808, -59.990994, 0],
                   [-3.0726896726601356, -59.99099253036923, 0],
                   [-3.072698083435522, -59.990989341988225, 1],
                   [-3.07270700056049, -59.9909905109687, 2],
                   [-3.0726718186529296, -59.99099446230452, 0],
                   [-3.0727152179762047, -59.99098685169822, 3],
                   [-3.0727242111646724, -59.9909868680853, 5],
                   [-3.0727306588616927, -59.99098058969601, 6],
                   [-3.0727254784341302, -59.99097322786188, 7],
                   [-3.072670354340788, -59.990985576339874, 4],
                   [-3.072726778771604, -59.990964316351636, 8],
                   [-3.0727068697559186, -59.990983502496086, 5],
                   [-3.072663138876874, -59.9909921053668, 4],
                   [-3.072739321321782, -59.99098300967931, 7],
                   [-3.0726980243153226, -59.99099834794488, 2],
                   [-3.0726745600475898, -59.99097761569798, 9],
                   [-3.0727425489691087, -59.99099141581041, 13],
                   [-3.0726779366905683, -59.99096926847177, 15],
                   [-3.0727116433282227, -59.99099822416237, 3],
                   [-3.0726745000491054, -59.99100305882437, 4],
                   [-3.0727514978394854, -59.99099230896085, 16],
                   [-3.0726816036610134, -59.99098502988151, 0],
                   [-3.0726892825139296, -59.990991194377195, 2],
                   [-3.0727353315571606, -59.990961532499284, 10],
                   [-3.072756769402691, -59.99098501229648, 20],
                   [-3.072761320607623, -59.99097724456741, 24]]

x_points = [(x[1] - longitude_origem) / conversao_longitude for x in segunda_geracao]
y_points = [(y[0] - latitude_origem) / conversao_latitude for y in segunda_geracao]
plt.plot(x_points, y_points, 'o', color='darkcyan', label='Novas coordenadas geradas')
plt.legend()
plt.savefig('teste_03_segunda_geracao.png', dpi=300)

segundo_caminho = [[-3.0726808, -59.990994],
                   [-3.0726896726601356, -59.99099253036923],
                   [-3.072698083435522, -59.990989341988225],
                   [-3.07270700056049, -59.9909905109687],
                   [-3.0727152179762047, -59.99098685169822],
                   [-3.0727242111646724, -59.9909868680853],
                   [-3.0727306588616927, -59.99098058969601],
                   [-3.072739321321782, -59.99098300967931],
                   [-3.0727425489691087, -59.99099141581041],
                   [-3.0727514978394854, -59.99099230896085],
                   [-3.072756769402691, -59.99098501229648],
                   [-3.072761320607623, -59.99097724456741]]

x_points = [(x[1] - longitude_origem) / conversao_longitude for x in segundo_caminho]
y_points = [(y[0] - latitude_origem) / conversao_latitude for y in segundo_caminho]
plt.plot(x_points, y_points, 'o', color='deepskyblue', linestyle="--", label='Segundo caminho gerado')
plt.legend()
plt.savefig('teste_03_segundo_caminho.png', dpi=300)

segundo_caminho_cumprido = [[-3.0726719, -59.990994],
                            [-3.0726808, -59.990994],
                            [-3.0727004, - 59.9909882],
                            [-3.0727067, -59.9909876],
                            [-3.0727164, -59.9909881],
                            [-3.0727254, -59.9909901],
                            [-3.0727307, -59.9909821],
                            [-3.07274, -59.9909817],
                            [-3.0727419, -59.9909886],
                            [-3.0726931, -59.9909715],
                            [-3.0727278, -59.991005]]

x_points = [(x[1] - longitude_origem) / conversao_longitude for x in segundo_caminho_cumprido]
y_points = [(y[0] - latitude_origem) / conversao_latitude for y in segundo_caminho_cumprido]
plt.plot(x_points, y_points, 'o', color='steelblue', linestyle="-", label='Segundo caminho executado')
plt.legend()
plt.savefig('teste_03_segundo_caminho_cumprido.png', dpi=300)


