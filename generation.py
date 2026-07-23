# Library imports
import random

# Local imports
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

    def carve(self, start_x, start_y, maze):
        """Given a blank maze and starting positions, uses Recursive Backtracking to build paths."""
        maze[(start_x, start_y)] = 0

        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        current_x, current_y = start_x, start_y

        for dx, dy in directions:
            new_x, new_y = current_x + dx, current_y + dy

            if 0 <= new_x < self.width and 0 <= new_y < self.height and maze[(new_x, new_y)] == 1:
                maze[(current_x + dx // 2, current_y + dy // 2)] = 0
                self.carve(new_x, new_y, maze)

        return maze

    def add_entry_exit(self, start_x, start_y, maze):
        maze[(start_x, start_y - 1)] = 0
        maze[(self.width - 2, self.height - 1)] = 0
        return maze

    def generate_maze(self, start_x, start_y):
        blank_maze = self.build()
        carved_maze = self.carve(start_x, start_y, blank_maze)
        complete_maze = self.add_entry_exit(start_x, start_y, carved_maze)
        return complete_maze