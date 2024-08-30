import pygame
import sys
from common.game_entities import GameState, Territory
# Initialize Pygame
pygame.init()
state = GameState(10)
# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Territorial Conquest Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 24)
    
def draw_territory(surface, territory: Territory):
    color = RED if territory.owner_id == "Player 1" else BLUE
    pygame.draw.rect(surface, color, pygame.Rect(territory.x * 60, territory.y * 60, 60, 60))
    pygame.draw.rect(surface, WHITE, pygame.Rect(territory.x * 60, territory.y * 60, 60, 60), 2)
    text_surface = font.render(f"{territory.resources}", True, WHITE)
    screen.blit(text_surface, (territory.x * 60 + 2, territory.y * 60 + 2))

def is_mouse_over_territory(territory: Territory, pos):
    return pygame.Rect(territory.x * 60, territory.y * 60, 60, 60).collidepoint(pos)


# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw territories
    for territory in state.get_territories():
        draw_territory(screen, territory)

    # Check for mouse hover
    mouse_pos = pygame.mouse.get_pos()
    for territory in state.get_territories():
        if is_mouse_over_territory(territory, mouse_pos):
            # Display territory info
            info_text = f"Owner: {territory.owner_id}, Resources: {territory.resources}, Position: ({territory.x}, {territory.y})"
            text_surface = font.render(info_text, True, WHITE)
            screen.blit(text_surface, (10, HEIGHT - 30))

            for neighbor in territory.neighbors:
                text_surface = font.render("N", True, RED)
                screen.blit(text_surface, (neighbor.x * 60 + 30, neighbor.y * 60 + 30))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()