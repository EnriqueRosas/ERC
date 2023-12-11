import pygame
import math
import random
import heapq

# Definición de colores
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# Inicialización de Pygame
pygame.init()

# Cargar la imagen del mapa
background_image = pygame.image.load('busqueda.jpg')

# Obtener el tamaño de la imagen
image_width, image_height = background_image.get_size()

# Inicialización de la ventana de Pygame
display = pygame.display.set_mode((image_width, image_height))
pygame.display.set_caption('A* Algorithm')

# Otros parámetros del programa
framerate = 30
clock = pygame.time.Clock()

# Lista de nodos con sus coordenadas aleatorias
nodes = {}
for node in range(15):  # Ajusta la cantidad deseada de nodos
    nodes[f'Node {node}'] = (random.randint(50, image_width - 50), random.randint(50, image_height - 50))

# Establecer un punto de partida y un punto de destino
start_node = random.choice(list(nodes.keys()))
end_node = random.choice(list(nodes.keys()))
while start_node == end_node:
    end_node = random.choice(list(nodes.keys()))

# Representación del grafo (conexiones entre nodos y costos)
graph = {}
for node in nodes:
    # Asigna conexiones y costos basados en la distancia euclidiana
    connections = {}
    for other_node, other_coords in nodes.items():
        if other_node != node and random.random() < 0.7:  # Ajusta el umbral para tener más conexiones
            distance = math.sqrt((nodes[node][0] - other_coords[0])**2 + (nodes[node][1] - other_coords[1])**2)
            cost = int(distance * 2)  # Puedes ajustar el factor multiplicativo según tu preferencia
            connections[other_node] = cost
    graph[node] = connections

# Algoritmo A* para encontrar la ruta más corta
def astar(graph, start, end):
    def flatten(L):
        while len(L) > 0:
            yield L[0]
            L = L[1]

    q = [(0, start, ())]
    visited = set()
    while True:
        cost, v1, path = heapq.heappop(q)
        if v1 not in visited:
            visited.add(v1)
            if v1 == end:
                return list(flatten(path))[::-1] + [v1]
            path = (v1, path)
            for v2, cost2 in graph[v1].items():
                if v2 not in visited:
                    heapq.heappush(q, (cost + cost2 + dis2(nodes[v2], nodes[end]), v2, path))

def dis2(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Encuentra la ruta más corta
shortest_path = astar(graph, start_node, end_node)

# Bucle principal
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.blit(background_image, (0, 0))

    # Dibuja nodos en la pantalla
    for node, (x, y) in nodes.items():
        pygame.draw.circle(display, red if node == start_node else blue if node == end_node else green, (x, y), 10)
        text = pygame.font.Font(None, 20).render(node, True, white)
        display.blit(text, (x - 5, y - 10))

    # Dibuja conexiones entre nodos
    for node, connections in graph.items():
        for neighbor, costo in connections.items():
            pygame.draw.line(display, yellow, nodes[node], nodes[neighbor], 2)
            # Muestra el costo en cada conexión
            text = pygame.font.Font(None, 15).render(str(costo), True, yellow)
            display.blit(text, ((nodes[node][0] + nodes[neighbor][0]) // 2, (nodes[node][1] + nodes[neighbor][1]) // 2))

    # Dibuja la ruta más corta
    if shortest_path:
        for i in range(len(shortest_path) - 1):
            pygame.draw.line(display, cyan, nodes[shortest_path[i]], nodes[shortest_path[i + 1]], 4)

    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
