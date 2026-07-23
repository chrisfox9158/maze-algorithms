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
    maze = generator.generate_maze(1, 1)
    
    window_width = generator.width * CELL_SIZE
    window_height = generator.height * CELL_SIZE
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Maze Visualizer")
    
    COLOR_WALL = (40, 44, 52)     # Dark slate gray
    COLOR_PATH = (255, 255, 255)  # White
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill(COLOR_WALL)
        
        for (x, y), value in maze.items():
            pixel_x = x * CELL_SIZE
            pixel_y = y * CELL_SIZE
            color = COLOR_PATH if value == 0 else COLOR_WALL
            
            pygame.draw.rect(screen, color, (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE))
            
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()