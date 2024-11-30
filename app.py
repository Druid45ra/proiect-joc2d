import pygame
import random

# Inițializare Pygame
pygame.init()

# Dimensiuni fereastră
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc 2D Simplu")

# Culori
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Setări joc
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

clock = pygame.time.Clock()

# Funcție pentru detectarea coliziunii
def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos

    if (ex < px < ex + enemy_size or ex < px + player_size < ex + enemy_size) and \
       (ey < py < ey + enemy_size or ey < py + player_size < ey + enemy_size):
        return True
    return False

# Scor
score = 0
font = pygame.font.SysFont("monospace", 35)

# Loop principal
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Mișcarea jucătorului
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10

    # Mișcarea inamicilor
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        score += 1  # Crește scorul când inamicul a fost evitat

    # Verificare coliziune
    if detect_collision(player_pos, enemy_pos):
        game_over = True

    # Desenare ecran
    screen.fill(BLACK)

    # Desenare player și inamic
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Afișare scor
    score_text = font.render(f"Scor: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Actualizare ecran
    pygame.display.flip()
    clock.tick(30)

# Afișare mesaj final
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, RED)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
