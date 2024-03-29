import matplotlib.pyplot as plt
from geopy.distance import great_circle

latitude_origem, longitude_origem = -3.0727958048845725, -59.991017392035396
latitude_destino, longitude_destino = -3.072764893793319, -59.99096969095618
conversao_latitude, conversao_longitude = 8.993203354940148e-06, 9.006152089787253e-06

primeira_geracao = [[-3.072679, -59.990995, 0],
                    [-3.072687944783805, -59.99099406669831, 0],
                    [-3.072696710722812, -59.99099205482102, 1],
                    [-3.072705402476889, -59.99098974257538, 2],
                    [-3.0727071832624206, -59.990980914754225, 3],
                    [-3.072715038485158, -59.9909765297306, 4],
                    [-3.072703263012381, -59.99097280931681, 4],
                    [-3.0727128254703175, -59.99099482697836, 3],
                    [-3.072676114457155, -59.99098647002889, 0],
                    [-3.072707577528725, -59.99096490728732, 6],
                    [-3.072669924988075, -59.990979936206195, 8],
                    [-3.072724007348497, -59.990977191891325, 5],
                    [-3.072731953763163, -59.99098140891615, 11],
                    [-3.072740391474336, -59.99098452510601, 12],
                    [-3.072663220143752, -59.99097393401652, 10],
                    [-3.0726991887140436, -59.990961661402665, 9],
                    [-3.07272428393877, -59.9909681900003, 11],
                    [-3.0726763279755884, -59.990973612095914, 10],
                    [-3.0727146619069443, -59.990970455054935, 9],
                    [-3.072748837952565, -59.990987617384796, 13],
                    [-3.072714082106039, -59.99095868801743, 9],
                    [-3.0726551253535193, -59.99097785783028, 14],
                    [-3.072719096925408, -59.99098837203622, 7],
                    [-3.0727233266085485, -59.990972866976946, 18],
                    [-3.0726963006673373, -59.990983058036576, 2],
                    [-3.0726722089803418, -59.99097365339284, 14],
                    [-3.072646135974537, -59.99097812045218, 21],
                    [-3.072730995229081, -59.99096219503946, 16],
                    [-3.0727578101175643, -59.99098823305596, 19],
                    [-3.072722002446599, -59.99095442208246, 20],
                    [-3.0727277519405454, -59.99099081858853, 22],
                    [-3.072735660087513, -59.990954495224216, 27],
                    [-3.072640530186269, -59.99098516284813, 26],
                    [-3.07265818506564, -59.99098632671097, 21],
                    [-3.0727154642662784, -59.9909966107573, 22],
                    [-3.0726971127156366, -59.99100105197038, 2],
                    [-3.0727644846991344, -59.99098219713409, 28],
                    [-3.07267774395756, -59.99098438573513, 10],
                    [-3.0727307051859163, -59.99099932529029, 30],
                    [-3.072687512029619, -59.99100306241636, 1],
                    [-3.0726975400463106, -59.99099411462462, 3],
                    [-3.0727646989847104, -59.99099402248819, 28],
                    [-3.0727255951780736, -59.99099191426205, 38],
                    [-3.072701455587743, -59.990952946057746, 15],
                    [-3.072653522699456, -59.990994028039374, 33],
                    [-3.072763492495157, -59.990973245962934, 36]]

caminho = [[-3.072687944783805, -59.99099406669831],
           [-3.072696710722812, -59.99099205482102],
           [-3.072705402476889, -59.99098974257538],
           [-3.0727071832624206, -59.990980914754225],
           [-3.072715038485158, -59.9909765297306],
           [-3.072724007348497, -59.990977191891325],
           [-3.072731953763163, -59.99098140891615],
           [-3.072740391474336, -59.99098452510601],
           [-3.072748837952565, -59.990987617384796],
           [-3.0727578101175643, -59.99098823305596],
           [-3.0727644846991344, -59.99098219713409],
           [-3.072763492495157, -59.990973245962934]]

caminho_cumprido = [[-3.0726804, -59.990995],
                    [-3.0726876, -59.9909947],
                    [-3.0726979, -59.9909934],
                    [-3.0727064, -59.9909877],
                    [-3.0727066, -59.9909823],
                    [-3.0727149, -59.9909748],
                    [-3.0727242, -59.9909766],
                    [-3.0727318, -59.9909825],
                    [-3.07274, -59.99099],
                    [-3.0727507, -59.9909887],
                    [-3.0727582, -59.9909878],
                    [-3.0727645, -59.99098],
                    [-3.0727646, -59.990974]]

# x_points = [(x[1] - longitude_origem) / conversao_longitude for x in primeira_geracao]
# y_points = [(y[0] - latitude_origem) / conversao_latitude for y in primeira_geracao]
# plt.plot(x_points, y_points, '.', color='darkorange', label='Coordenadas geradas')
# plt.plot(x_points[0], y_points[0], 'o', color='darkgreen', label='Coordenada inicial')
# x_destino = (longitude_destino - longitude_origem) / conversao_longitude
# y_destino = (latitude_destino - latitude_origem) / conversao_latitude
# plt.plot(x_destino, y_destino, 'o', color='red', label='Coordenada destino')
# center = x_destino, y_destino
# circle = plt.Circle(center, radius=1, fill=False, color='red', label='Região de Destino')
# plt.gcf().gca().add_patch(circle)
# plt.rc('axes', labelsize=4)
# plt.ylim(0, 20)
# plt.xlim(0, 20)
# plt.ylabel("Distância no sentido Norte em metros")
# plt.xlabel("Distância no sentido Leste em metros")
# plt.grid(color='b', linestyle='-', linewidth=0.1)
# plt.legend()
# plt.savefig('teste_02_coordenadas_geradas.png', dpi=300)
#
# x_points = [(x[1] - longitude_origem) / conversao_longitude for x in caminho]
# y_points = [(y[0] - latitude_origem) / conversao_latitude for y in caminho]
# plt.plot(x_points, y_points, 'o', color='greenyellow', linestyle="--", label='Caminho gerado')
# plt.legend()
# plt.savefig('teste_02_coordenadas_caminho.png', dpi=300)
#
# x_points = [(x[1] - longitude_origem) / conversao_longitude for x in caminho_cumprido]
# y_points = [(y[0] - latitude_origem) / conversao_latitude for y in caminho_cumprido]
# plt.plot(x_points[1:], y_points[1:], 'o', color='darkblue', linestyle="-", label='Caminho executado')
# plt.plot(x_points[0], y_points[0], 'v', color='darkblue', label='Posição inicial do VANT')
# plt.legend()
# plt.savefig('teste_02_coordenadas_cumpridas.png', dpi=300)

media = []
for i in range(len(caminho)):
    print(f"{great_circle(caminho[i], caminho_cumprido[i]).meters}")
    media.append(great_circle(caminho[i], caminho_cumprido[i]).meters)

print(f"media {round(sum(media)/len(media), 2)}")