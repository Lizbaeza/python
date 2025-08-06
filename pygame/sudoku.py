import pygame
import time

pygame.init()

# Configuración pantalla
WIDTH, HEIGHT = 540, 660  # altura un poco más para los números
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku con Cronómetro y Vidas")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)

# Fuente
font = pygame.font.SysFont("comicsans", 40)
font_small = pygame.font.SysFont("comicsans", 20)

# Tablero Sudoku inicial (0 = vacío)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Variables para selección
selected_cell = None
selected_number = None
user_input = {}

# Vidas
lives = 3

# Función para dibujar líneas del tablero
def draw_grid():
    gap = WIDTH // 9
    for i in range(10):
        thick = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap), thick)
        pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, WIDTH), thick)

# Función para dibujar números en el tablero
def draw_numbers():
    gap = WIDTH // 9
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(text, (j * gap + 15, i * gap + 10))
            elif (i, j) in user_input:
                text = font.render(str(user_input[(i, j)]), True, BLUE)
                screen.blit(text, (j * gap + 15, i * gap + 10))

# Función para validar si número es válido en el tablero
def is_valid(num, pos):
    row, col = pos
    # Chequear fila
    for j in range(9):
        if board[row][j] == num and col != j:
            return False
    # Chequear columna
    for i in range(9):
        if board[i][col] == num and row != i:
            return False
    # Chequear caja 3x3
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Función para dibujar selección
def draw_selection():
    if selected_cell:
        gap = WIDTH // 9
        pygame.draw.rect(screen, RED, (selected_cell[1] * gap, selected_cell[0] * gap, gap, gap), 3)

# Función para chequear si el tablero está completo
def is_board_complete():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 and (i, j) not in user_input:
                return False
    return True

# Función para dibujar vidas
def draw_lives():
    text = font_small.render(f"Vidas: {lives}", True, RED)
    screen.blit(text, (WIDTH - 100, WIDTH + 10))

# Función para dibujar números para elegir
def draw_number_buttons():
    gap = WIDTH // 9
    for i in range(9):
        rect = pygame.Rect(i * gap, WIDTH + 40, gap, gap)
        pygame.draw.rect(screen, GREY if selected_number != i+1 else BLUE, rect)
        num_text = font.render(str(i+1), True, BLACK)
        screen.blit(num_text, (i * gap + 20, WIDTH + 40 + 5))
    # Botón borrar (X)
    del_rect = pygame.Rect(9 * gap, WIDTH + 40, gap, gap)
    pygame.draw.rect(screen, GREY, del_rect)
    del_text = font.render("X", True, BLACK)
    screen.blit(del_text, (9 * gap + 20, WIDTH + 40 + 5))
    return del_rect

# Main loop
start_time = time.time()
running = True
while running:
    screen.fill(WHITE)
    elapsed_time = int(time.time() - start_time)
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    timer_text = font_small.render(f"Tiempo: {minutes:02d}:{seconds:02d}", True, BLACK)
    screen.blit(timer_text, (10, WIDTH + 10))

    draw_grid()
    draw_numbers()
    draw_selection()
    draw_lives()
    del_rect = draw_number_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Selección con click en celda
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            gap = WIDTH // 9
            x, y = pos[0] // gap, pos[1] // gap
            if y < 9:
                selected_cell = (y, x)
            else:
                # Click en números para elegir
                if pos[1] >= 0 and pos[1] < WIDTH and pos[1] // gap < 9 and pos[1] // gap == x:
                    # Si clickeó en el rango horizontal de números
                    if WIDTH <= pos[1] <= WIDTH + 90:
                        pass # por si se necesita más adelante
                clicked_button = pos[0] // gap
                if pos[1] >= WIDTH + 40:
                    # números están en y desde WIDTH+40 a WIDTH+80
                    btn_idx = pos[0] // gap
                    pass

                # Mejor forma: detectamos cuál botón se clickeó
                btn_idx = pos[0] // gap
                mouse_x, mouse_y = pos
                # Número para elegir
                for i in range(9):
                    rect = pygame.Rect(i * gap, WIDTH + 40, gap, gap)
                    if rect.collidepoint(pos):
                        selected_number = i + 1
                        break
                # Botón borrar
                if del_rect.collidepoint(pos):
                    selected_number = None

        # Poner número seleccionado en la celda
        if event.type == pygame.MOUSEBUTTONDOWN and selected_cell and selected_number:
            row, col = selected_cell
            if board[row][col] == 0:
                if is_valid(selected_number, (row, col)):
                    user_input[(row, col)] = selected_number
                    board[row][col] = selected_number
                else:
                    lives -= 1
                    if lives <= 0:
                        # Juego terminado por perder
                        running = False

        # También permitir borrar con click en celda vacía si seleccionaste borrar
        if event.type == pygame.MOUSEBUTTONDOWN and selected_cell and selected_number is None:
            row, col = selected_cell
            if (row, col) in user_input:
                del user_input[(row, col)]
                board[row][col] = 0

    # Revisar si terminaste el Sudoku
    if is_board_complete():
        complete_text = font.render("¡Completado!", True, GREEN)
        screen.blit(complete_text, (WIDTH // 3, WIDTH // 2))

    pygame.display.update()

pygame.quit()
def draw_number_buttons():
    gap = WIDTH // 9
    for i in range(9):
        rect = pygame.Rect(i * gap, WIDTH + 40, gap, gap)
        pygame.draw.rect(screen, GREY if selected_number != i+1 else BLUE, rect)
        num_text = font.render(str(i+1), True, BLACK)
        screen.blit(num_text, (i * gap + 20, WIDTH + 40 + 5))
    del_rect = pygame.Rect(9 * gap, WIDTH + 40, gap, gap)
    # Aquí falta dibujar el botón de borrar, por ejemplo:
    pygame.draw.rect(screen, GREY, del_rect)
    del_text = font.render("X", True, BLACK)
    screen.blit(del_text, (9 * gap + 20, WIDTH + 40 + 5))
    return del_rect
    if solution[selected_row][selected_col] == selected_number:
        board[selected_row][selected_col] = selected_number


