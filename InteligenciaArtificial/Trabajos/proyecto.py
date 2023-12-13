import pygame
import math
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

# Lista de nodos con sus coordenadas asociadas
nodes = {
    'A': (100, 150),
    'B': (200, 400),
    'C': (300, 100),
    'D': (430, 70),
    'E': (430, 500),
    'F': (600, 350),
    'G': (830, 75),
    'H': (750, 550),
    'I': (900, 200),
    'J': (1000, 380),
    'K': (1100, 550),
    'L': (1200, 100),
    # Agrega más nodos según sea necesario
}

# Representación del grafo (conexiones entre nodos y costos)
graph = {
    'A': {'B': 0, 'C': 0, 'D': 0},
    'B': {'A': 0, 'C': 0, 'E': 0},
    'C': {'A': 0, 'B': 0, 'F': 0},
    'D': {'A': 0, 'E': 0, 'G': 0},
    'E': {'B': 0, 'D': 0, 'F': 0, 'H': 0},
    'F': {'C': 0, 'E': 0, 'G': 0, 'I': 0},
    'G': {'D': 0, 'F': 0, 'H': 0, 'J': 0},
    'H': {'E': 0, 'G': 0, 'I': 0, 'K': 0},
    'I': {'F': 0, 'H': 0, 'J': 0, 'L': 0},
    'J': {'G': 0, 'I': 0, 'K': 0},
    'K': {'H': 0, 'J': 0, 'L': 0},
    'L': {'I': 0, 'K': 0},
    # Agrega más conexiones según sea necesario
}

# Funciones auxiliares
def dis_manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# Función de distancia ajustada para usar la métrica de Manhattan
def dis2(a, b):
    return dis_manhattan(a, b)

# Función A* para encontrar la ruta más corta
def astar(graph, start, goal):
    open_set = [(0, start)]
    closed_set = set()

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    came_from = {}

    while open_set:
        current_g, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return path

        closed_set.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor in closed_set:
                continue

            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + dis_manhattan(nodes[neighbor], nodes[goal]), neighbor))
                came_from[neighbor] = current

    return None

# Obtener la ruta más corta
shortest_path = astar(graph, 'A', 'K')

# Bucle principal
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.blit(background_image, (0, 0))

    # Dibuja nodos en la pantalla
    for node, (x, y) in nodes.items():
        color = red
        if node == 'A':
            color = cyan
        elif node == 'K':
            color = yellow
        pygame.draw.circle(display, color, (x, y), 10)
        text = pygame.font.Font(None, 20).render(node, True, white)
        display.blit(text, (x - 5, y - 10))

    # Dibuja conexiones entre nodos
    for node, connections in graph.items():
        for neighbor, costo in connections.items():
            line_color = blue
            if (node, neighbor) in zip(shortest_path, shortest_path[1:]):
                line_color = yellow  # Cambia el color de la ruta más corta
                # Pinta las líneas de la ruta más corta de un color diferente
                pygame.draw.line(display, line_color, nodes[node], nodes[neighbor], 4)
            else:
                pygame.draw.line(display, line_color, nodes[node], nodes[neighbor], 2)
            # Muestra el costo en cada conexión
            text = pygame.font.Font(None, 15).render(str(costo), True, green)
            display.blit(text, ((nodes[node][0] + nodes[neighbor][0]) // 2, (nodes[node][1] + nodes[neighbor][1]) // 2))

    pygame.display.update()
    clock.tick(framerate)

pygame.quit()
