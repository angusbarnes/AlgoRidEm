import pygame
import sys

# Initialize Pygame
pygame.init()

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

class Territory:
    def __init__(self, x, y, width, height, owner, troops):
        self.rect = pygame.Rect(x, y, width, height)
        self.owner = owner
        self.troops = troops

    def draw(self, surface):
        color = RED if self.owner == "Player 1" else BLUE
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, WHITE, self.rect, 2)

    def is_mouse_over(self, pos):
        return self.rect.collidepoint(pos)

# Create some example territories
territories = [
    Territory(100, 100, 100, 100, "Player 1", 10),
    Territory(250, 100, 100, 100, "Player 2", 15),
    Territory(400, 100, 100, 100, "Player 1", 5),
]

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
    for territory in territories:
        territory.draw(screen)

    # Check for mouse hover
    mouse_pos = pygame.mouse.get_pos()
    for territory in territories:
        if territory.is_mouse_over(mouse_pos):
            # Display territory info
            info_text = f"Owner: {territory.owner}, Troops: {territory.troops}"
            text_surface = font.render(info_text, True, WHITE)
            screen.blit(text_surface, (10, HEIGHT - 30))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()