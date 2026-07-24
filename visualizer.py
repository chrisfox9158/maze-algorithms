# Library imports
import pygame
import sys

# Local imports
from generation import RecursiveBacktracking
from algorithms.bfs import BFS
from config import MAZE_SPECS

# Pygame visualizer
CELL_SIZE = MAZE_SPECS["cell_size"]

def main():
    pygame.init()

    # Maze instance and solution "runner" setup
    generator = RecursiveBacktracking()
    maze = generator.generate_maze()
    bfs = BFS()
    exploration, solution = bfs.run(1, 1, maze)
    solution_idx = 0
    explore_idx = 0
    solution_path = []

    # General clock and window setup
    clock = pygame.time.Clock()
    window_width = generator.width * CELL_SIZE
    window_height = generator.height * CELL_SIZE
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Maze Visualizer")

    # Color configurations
    COLOR_WALL = (92, 108, 124) # Slate gray
    COLOR_PATH = (255, 255, 255) # White

    # Rendering loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        screen.fill(COLOR_WALL)
        for (x, y), value in maze.items(): # Render maze
            pixel_x = x * CELL_SIZE
            pixel_y = y * CELL_SIZE
            if value == 0:
                color = COLOR_PATH 
            elif value == 1:
                color = COLOR_WALL
            elif value == 2: # entry
                color = (255, 0, 0)
            elif value == 3: # exit
                color = (0, 255, 0)
            pygame.draw.rect(screen, color, (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE))

        if explore_idx < len(exploration): # "Explorer" display (follows visited paths)
            SPEED = 100
            explore_idx += 1
                
        elif solution_idx < len(solution): # "Runner" display (follows solution path)
            SPEED = 30
            solution_path.append(solution[solution_idx])
            solution_idx += 1

        for cell in exploration[:explore_idx]:
            pygame.draw.rect(screen, (70, 70, 100), (cell[0]*CELL_SIZE, cell[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for step in solution_path:
            pygame.draw.rect(screen, (0, 0, 255), (step[0] * CELL_SIZE, step[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if explore_idx >= len(exploration) and solution_idx >= len(solution): # "Run complete" pop-up
            font = pygame.font.Font(None, 50)
            text = font.render("Run complete!", True, (0, 0, 0))
            text_box = text.get_rect()
            text_box.center = (window_width // 2, window_height // 2)
            screen.blit(text, text_box)

        pygame.display.flip()
        clock.tick(SPEED)

if __name__ == "__main__":
    main()