# Library imports
import random

# Local imports
from generation.result import GenerationResult
from config import MAZE_SPECS

# Blank maze generation
class RecursiveBacktracking:
    """Generates a maze via Recursive Backtracking."""
    def __init__(self):
        self.width = MAZE_SPECS["width"] if MAZE_SPECS["width"] % 2 != 0 else MAZE_SPECS["width"] + 1
        self.height = MAZE_SPECS["height"] if MAZE_SPECS["height"] % 2 != 0 else MAZE_SPECS["height"] + 1

    def build(self):
        """Build a maze populated entirely closed cells."""
        maze = {(x, y): 1 for x in range(self.width) for y in range(self.height)}
        return maze

    def carve(self, start_x, start_y, maze, carved_paths=None):
        """Given a blank maze and starting positions, uses Recursive Backtracking to build paths."""
        if carved_paths is None:
            carved_paths = []

        maze[(start_x, start_y)] = 0
        carved_paths.append((start_x, start_y))

        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        current_x, current_y = start_x, start_y

        for dx, dy in directions:
            new_x, new_y = current_x + dx, current_y + dy

            if 0 <= new_x < self.width and 0 <= new_y < self.height and maze[(new_x, new_y)] == 1:
                connector = (current_x + dx // 2, current_y + dy // 2)
                maze[connector] = 0
                carved_paths.append(connector)
                self.carve(new_x, new_y, maze, carved_paths)

        return maze, carved_paths

    def add_entry_exit(self, maze):
        """Add entry and exit point cell values."""
        algorithm_entry = (1, 1) # Entry for the ALGORITHM (player), NOT the generator
        algorithm_exit = (self.width - 2, self.height - 2) # Exit for the ALGORITHM (player)
        maze[algorithm_entry] = 2
        maze[algorithm_exit] = 3
        return maze

    def generate_maze(self):
        """Orchestrate full maze generation."""
        blank_maze = self.build()
        carved_maze, carved_paths = self.carve(1, 1, blank_maze)
        complete_maze = self.add_entry_exit(carved_maze)
        return GenerationResult(carved_paths=carved_paths, maze=complete_maze)