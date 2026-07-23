# Library imports
import pygame
import sys

# Local imports
from generation import RecursiveBacktracking
from config import MAZE_SPECS

# Pygame visualizer
CELL_SIZE = MAZE_SPECS["cell_size"]

def main():
    pygame.init()
    
    generator = RecursiveBacktracking()
    maze = generator.generate_maze()
    
    window_width = generator.width * CELL_SIZE
    window_height = generator.height * CELL_SIZE
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Maze Visualizer")

    COLOR_BORDER = (48, 48, 56) # Dark slate gray
    COLOR_WALL = (112, 128, 144) # Slate gray
    COLOR_PATH = (255, 255, 255) # White
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLOR_WALL)
        for (x, y), value in maze.items():
            pixel_x = x * CELL_SIZE
            pixel_y = y * CELL_SIZE
            if value == 0:
                color = COLOR_PATH 
            elif value == 1:
                color = COLOR_WALL
            elif value == 2:
                color = COLOR_BORDER
            elif value == 3:
                color = (255, 0, 0)
            elif value == 4:
                color = (0, 255, 0)
            
            pygame.draw.rect(screen, color, (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE))
            
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()