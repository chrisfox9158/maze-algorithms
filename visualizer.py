# Library imports
import pygame
import sys

# Local imports
from generation import RecursiveBacktracking
from algorithms.bfs import BFS
from config import MAZE_SPECS, DISPLAY_SPECS

# Pygame visualizer
CELL_SIZE = MAZE_SPECS["cell_size"]
SPEED = DISPLAY_SPECS["tick_speed"]

def main():
    pygame.init()

    # Maze instance and solution "runner" setup
    bfs = BFS()
    generator = RecursiveBacktracking()
    maze = generator.generate_maze()
    solution = bfs.run(1, 1, maze)
    solution_idx = 0
    path = []

    # General clock and window setup
    clock = pygame.time.Clock()
    window_width = generator.width * CELL_SIZE
    window_height = generator.height * CELL_SIZE
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Maze Visualizer")

    # Color configurations
    COLOR_BORDER = (48, 48, 56) # Dark slate gray
    COLOR_WALL = (112, 128, 144) # Slate gray
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
            elif value == 2:
                color = COLOR_BORDER
            elif value == 3: # entry
                color = (255, 0, 0)
            elif value == 4: # exit
                color = (0, 255, 0)
            pygame.draw.rect(screen, color, (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE))

        if solution_idx < len(solution): # "Runner" display (follows solution path)
            runner_pos = solution[solution_idx]
            path.append(runner_pos)
            solution_idx += 1
            for step in path:
                pygame.draw.rect(screen, (0, 0, 255), (step[0] * CELL_SIZE, step[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        else: # "Run complete" pop-up
            font = pygame.font.Font(None, 50)
            text = font.render("Run complete!", True, (0, 0, 0))
            text_box = text.get_rect()
            text_box.center = (window_width // 2, window_height // 2)
            screen.blit(text, text_box)

        pygame.display.flip()
        clock.tick(SPEED)

if __name__ == "__main__":
    main()