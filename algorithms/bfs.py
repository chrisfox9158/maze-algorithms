# Library imports
from collections import deque

# Local imports
from generation import RecursiveBacktracking
from config import MAZE_SPECS

# Breadth-first search algorithm
class BFS:
    def __init__(self):
        self.x, self.y = 1, 1
        self.maze_width = MAZE_SPECS["width"]
        self.maze_height = MAZE_SPECS["height"]
        self.prev = {}

    def get_open_neighbors(self, x, y, maze):
        open_neighbors = []
        N, S, E, W = (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)
        for direction in (N, S, E, W):
            if maze.get(direction) in (0, 3, 4):
                open_neighbors.append(direction)
        return open_neighbors

    def get_frontier(self, visited, x, y, maze):
        open_neighbors = self.get_open_neighbors(x, y, maze)
        frontier = []
        for cell in open_neighbors:
            if cell not in visited:
                frontier.append(cell)
        return frontier

    def run(self, start_x, start_y, maze):
        visited = set()
        visit_order = []
        self.x, self.y = start_x, start_y

        queue = deque([[(self.x, self.y)]])
        visited.add((self.x, self.y))
        visit_order.append((self.x, self.y))

        while queue:
            current_path = queue.popleft()
            self.x, self.y = current_path[-1]

            if maze[(self.x, self.y)] == 3:
                return visit_order, current_path
            
            for cell in self.get_frontier(visited, self.x, self.y, maze):
                visited.add(cell)
                visit_order.append(cell)
                new_path = list(current_path)
                new_path.append(cell)
                queue.append(new_path)

        return visit_order, None