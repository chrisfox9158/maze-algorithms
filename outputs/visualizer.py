# Library imports
import pygame
import sys

# Local imports
from config import MAZE_SPECS

CELL_SIZE = MAZE_SPECS["cell_size"]
MAZE_WIDTH = MAZE_SPECS["width"] if MAZE_SPECS["width"] % 2 != 0 else MAZE_SPECS["width"] + 1
MAZE_HEIGHT = MAZE_SPECS["height"] if MAZE_SPECS["height"] % 2 != 0 else MAZE_SPECS["height"] + 1
COLOR_WALL = (92, 108, 124)
COLOR_PATH = (255, 255, 255)
COLOR_ENTRY = (255, 0, 0)
COLOR_EXIT = (0, 255, 0)
COLOR_EXPLORE = (70, 70, 100)
COLOR_SOLUTION = (0, 0, 255)

class Visualizer:
    def __init__(self, maze, result):
        self.maze = maze
        self.exploration = result.exploration
        self.solution = result.solution or []

        self.explore_idx = 0
        self.solution_idx = 0
        self.solution_path = []
        self.speed = 100

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        window_width = MAZE_WIDTH * CELL_SIZE
        window_height = MAZE_HEIGHT * CELL_SIZE
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Maze Visualizer")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

            screen.fill(COLOR_WALL)
            self._draw_maze(screen)
            self._advance()
            self._draw_progress(screen)
            self._draw_complete(screen, window_width, window_height)

            pygame.display.flip()
            clock.tick(self.speed)

    def _draw_maze(self, screen):
        for (x, y), value in self.maze.items():
            color = COLOR_PATH
            if value == 1:
                color = COLOR_WALL
            elif value == 2:
                color = COLOR_ENTRY
            elif value == 3:
                color = COLOR_EXIT
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def _advance(self):
        if self.explore_idx < len(self.exploration):
            self.speed = 100
            self.explore_idx += 1
        elif self.solution_idx < len(self.solution):
            self.speed = 30
            self.solution_path.append(self.solution[self.solution_idx])
            self.solution_idx += 1

    def _draw_progress(self, screen):
        for cell in self.exploration[:self.explore_idx]:
            pygame.draw.rect(screen, COLOR_EXPLORE, (cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for step in self.solution_path:
            pygame.draw.rect(screen, COLOR_SOLUTION, (step[0] * CELL_SIZE, step[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def _draw_complete(self, screen, window_width, window_height):
        if self.explore_idx >= len(self.exploration) and self.solution_idx >= len(self.solution):
            font = pygame.font.Font(None, 50)
            text = font.render("Run complete!", True, (0, 0, 0))
            text_box = text.get_rect()
            text_box.center = (window_width // 2, window_height // 2)
            screen.blit(text, text_box)