import pygame
import sys
import random

# Inicialización
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 150, 150
CELL_SIZE = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Viborita")

# Colores
LIGHT_BG = (240, 240, 240)
SNAKE_COLOR = (0, 180, 0)
FOOD_COLOR = (200, 0, 0)

# Reloj
clock = pygame.time.Clock()
FPS = 10

# Función para generar comida
def random_food():
    return [
        random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    ]

# Inicializar serpiente
snake = [[200, 200]]
direction = "RIGHT"
food = random_food()

# Bucle principal
running = True
while running:
    screen.fill(LIGHT_BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Mover la cabeza
    head = list(snake[0])
    if direction == "UP":
        head[1] -= CELL_SIZE
    elif direction == "DOWN":
        head[1] += CELL_SIZE
    elif direction == "LEFT":
        head[0] -= CELL_SIZE
    elif direction == "RIGHT":
        head[0] += CELL_SIZE

    # Comprobar colisión con bordes
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("¡Perdiste!")
        running = False
        continue

    # Insertar nueva cabeza
    snake.insert(0, head)

    # Comer comida o moverse
    if head == food:
        food = random_food()
    else:
        snake.pop()

    # Dibujar comida
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Dibujar serpiente
    for block in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (block[0], block[1], CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
